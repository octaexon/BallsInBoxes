import os
import re
from subprocess import run

from bibtools.container import ParameterDict
from bibtools.parameter import Parameter

from bibtools.defaults  import (VOLUME, TIME, PERIOD, BURN, X, Y, BATCH)
from bibtools.defaults  import (MINIMUM_VOLUME, MATRIX_DIMENSION, SAVE_INTERVAL)
from bibtools.defaults  import (MINIMUM_VOLUME_VALUE, MATRIX_DIMENSION_VALUE, SAVE_INTERVAL_VALUE)
from bibtools.defaults  import (OUTPUT_PATH, SEED)


class Configuration(ParameterDict):
    def __init__(self):
        # initialize empty ParameterDict
        super().__init__()
        # load default parameters
        self[VOLUME]           = Parameter(VOLUME)
        self[TIME]             = Parameter(TIME)
        self[PERIOD]           = Parameter(PERIOD)
        self[BURN]             = Parameter(BURN)
        self[X]                = Parameter(X)
        self[Y]                = Parameter(Y)
        self[BATCH]            = Parameter(BATCH)
        self[MINIMUM_VOLUME]   = Parameter(MINIMUM_VOLUME  , MINIMUM_VOLUME_VALUE)
        self[MATRIX_DIMENSION] = Parameter(MATRIX_DIMENSION, MATRIX_DIMENSION_VALUE)
        self[SAVE_INTERVAL]    = Parameter(SAVE_INTERVAL   , SAVE_INTERVAL_VALUE)
        self[OUTPUT_PATH]      = Parameter(OUTPUT_PATH)
        self[SEED]             = Parameter(SEED)


    def simulate(self, simulation_exec, indexed_seed, output_path, seed_burn = None):
        ''' simulate data samples/burn

            arguments:
            ----------
            indexed_seed : list
                indexed seed

            output_path : string
                path to save simulated data
        '''
        if seed_burn is None:
            seed_burn = self[BURN].values[0]

        if not indexed_seed or seed_burn > self[BURN].values[0]:
            # run simulator to write one sample, with sample number 1
            # simulator should run for burn * period
            self[PERIOD].values = self[PERIOD].values[0] * self[BURN].values[0]
            self[BATCH].values  = 1

        elif seed_burn < self[BURN].values[0]:
            # there is a seed, but from an ealier burn
            # burn in the rest of the way
            self[PERIOD].values = self[PERIOD].values[0] * (self[BURN].values[0] - seed_burn)
            self[BATCH].values  = 1

            # assign seed
            self[SEED].values = indexed_seed
            # reassign seed index (would prefer this to be -1, so that seed has
            # index 0, but must alter mcmc also)
            self[SEED].values[0] = 1

        else:
            # only complete to specified batch size
            remaining = self[BATCH].values[0] - indexed_seed[0]

            # check if enough samples already generated
            if remaining <= 0:
                return

            # only strings may be passed to run
            self[BATCH].values = remaining
            self[SEED].values  = indexed_seed

        self[OUTPUT_PATH].values = output_path

        # pass arguments to simulator
        run([simulation_exec] + self.to_command_line())



    def to_command_line(self):
        ''' presents parameters as a valid command line '''
        holder = []
        for key, parameter in self.items():
            if not key in [BURN]:
                holder += parameter.to_command_line()
        return holder



    def generate_full_path(self, base_path):
        ''' generates folder structure

            arguments:
            -----------
            base_path : string
                relative path to base of task at hand

            methodology:
            ------------
            generate/ensure folder structure

            notes:
            ------
            generates directory structure:
                base_path -> params_path -> points_path -> files
        '''

        # subpath specified by parameters (volume, time, period, burn)
        params_sub = '_'.join([str(self[VOLUME]), str(self[TIME]), str(self[PERIOD]), str(self[BURN])])
        # subpath specified by points (x,y)
        points_sub = '_'.join([str(self[X]), str(self[Y])])


            # path to parameters directory
        params_path  = os.path.join(base_path, params_sub)
        # path to point directory
        points_path  = os.path.join(params_path, points_sub)

        try:
            os.mkdir(params_path)
        except FileExistsError:
            pass
        except FileNotFoundError as err:
            logger = logging.getLogger(__name__)
            logger.error('unable to generate parameters path {}'.format(params_path))
            raise err

        try:
            os.mkdir(points_path)
        except FileExistsError:
            pass
        except FileNotFoundError as err:
            logger = logging.getLogger(__name__)
            logger.error('unable to generate points path {}'.format(points_path))
            raise err

        return points_path


    def get_potential_seeds(self, base_path):
        ''' returns information about potential seed data

            arguments:
            ----------
            base_path : string
                relative path to base directory

            returns:
            --------
            seed_info : iterator
                yields tuples containing burn value for seed and path to seed

            notes:
            ------
            only those seeds with burn-in earlier than self[BURN] are returned
            seeds are sorted with highest burn in value first
        '''
        # subpath specified by parameters (volume, time, period, burn)
        params_regex = '_'.join([str(self[VOLUME]), str(self[TIME]), str(self[PERIOD]), BURN.token, '(\d+)'])
        # subpath specified by points (x,y)
        points_sub = '_'.join([str(self[X]), str(self[Y])])

        base_contents = os.listdir(base_path)

        seed_info = []
        for params_sub in base_contents:
            matching = re.match(params_regex, params_sub)
            if matching:
                seed_burn = int(matching.group(1))
                seed_path = '/'.join([base_path, params_sub, points_sub])

                if seed_burn <= self[BURN].values[0] and os.path.isdir(seed_path):
                    seed_info.append((seed_burn, seed_path))

        if seed_info:
            seed_info.sort(key = lambda pair : pair[0], reverse = True)

        return iter(seed_info)




    def __str__(self):
        ''' representation for logging display '''
        return ' | '.join([repr(v) for (k, v) in self.items() if not k in [MATRIX_DIMENSION, SAVE_INTERVAL, OUTPUT_PATH, SEED]])
