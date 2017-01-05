import logging
import matplotlib.pyplot as plt

from bibtools.container             import ParameterDict
from bibtools.parameter             import Parameter
from bibtools.defaults              import X, Y
from bibtools.plotsettings.exponent import *

class Exponent(ParameterDict):
    ''' plotting class for exponents '''
    def __init__(self, key):
        ''' initialize exponent

            arguments:
            ----------
            key : ParameterKey object
                corresponding to exponent
        '''
        super().__init__()
        self.key    = key

        # holds phase space coordinates
        self[X]     = Parameter(X)
        self[Y]     = Parameter(Y)

        # holds exponent values
        self[key] = Parameter(key)

    def load(self, *containers):
        ''' loads values from container parameters

            *containers : ParameterDict objects
                hold values for X, Y and key
        '''
        for c in containers:
            for key, parameter in c.items():
                try:
                    self[key].values += parameter.values
                except KeyError:
                    pass
                except ValueError as err:
                    logger = logging.getLogger(__name__)
                    logger.error('')
                    raise err 

    def plot(self, output_file):
        ''' plot exponent along transition (hopefully)

            arguments:
            ----------
            output_file : string
                filename to save figure
        '''
        # create subplot axes 
        if len(set(self[X].values)) == 1:
            # sort lists based on y values
            abscissa = Parameter(B2, sorted(self[Y].values))
            fixed    = Parameter(B1, self[X].values)
            sorted_ordinate_values = [o for (a,o) in sorted(zip(self[Y].values, self[self.key].values), key = lambda pair : pair[0])]

        elif len(set(self[Y].values)) == 1:
            abscissa = Parameter(B1, sorted(self[X].values))
            fixed    = Parameter(B2, self[Y].values)
            sorted_ordinate_values = [o for (a,o) in sorted(zip(self[X].values, self[self.key].values), key = lambda pair : pair[0])]
        else:
            logger = logging.getLogger(__name__)
            logger.error('Cannot plot exponent')
            raise ValueError

        ordinate = Parameter(self.key, sorted_ordinate_values)

        fig  = plt.figure(**FIGURE_PREFS)
        ax   = fig.add_axes(AXES_PREFS) 

        #title_prefs  = {'s' : '', 'fontsize' : 18}
        xlabel_prefs = {'s' : '${}$ @ ${} = {}$'.format(abscissa.key.name, fixed.key.name, fixed.values[0]), 'fontsize' : 15}
        ylabel_prefs = {'s' : '$\{}$'.format(ordinate.key.name), 'fontsize' : 15}

        #plt.title(**TITLE_PREFS)
        plt.xlabel(**xlabel_prefs)
        plt.ylabel(**ylabel_prefs)
        plt.tick_params(**MAJOR_TICK_PREFS)
        plt.tick_params(**MINOR_TICK_PREFS)

        plt.plot(abscissa.values, ordinate.values)
        plt.savefig(output_file, format = 'eps', dpi = 1000)
        plt.close()



