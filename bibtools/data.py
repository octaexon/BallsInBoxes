import numpy as np
import re
import os
import logging

class Data:
    def __init__(self):
        '''
        data members:
        -------------
        samples : numpy array
            samples from markov chain
        '''
        self.samples     = np.empty(shape = (0,0), dtype = int)


    def load_all_csv(self, input_path):
        ''' load data from input csv files

            parameters:
            -----------
            input_path : string
                path specifying containing directory for data files
        '''
        # assemble files located at the terminus of input path
        # get contents of directory
        try:
            contents = os.listdir(input_path)
        except OSError as err:
            logger = logging.getLogger(__name__)
            logger.error('input path {} does not exist'.format(input_path))
            raise err

        input_regex = '.*csv$'

        # filter out non-csv files
        r = re.compile(input_regex)
        input_files = filter(r.match, contents)

        # prepend path to each data file in list
        input_files = [input_path + '/' + ifile for ifile in input_files]
        # sort filenames since most likely this will place samples in order
        input_files.sort()

        if not input_files:
            return

        # placeholder for loaded data frames
        input_arrays = []

        # load data to list
        for ifile in input_files:
            try:
                ifile_contents = np.genfromtxt(ifile, dtype = int, delimiter = ',')
                input_arrays.append(ifile_contents)

            except FileNotFoundError as err:
                logger = logging.getLogger(__name__)
                logging.error('file not found {}'.format(ifile))
                raise err

            except ValueError as err:
                logger = logging.getLogger(__name__)
                logger.error('non-existent or invalid entries {}'.format(ifile))
                raise err

        # ensure that array are 2d
        for iarray in input_arrays:
            if iarray.ndim == 1:
                length = len(iarray)
                iarray.shape = (1, length)

        # concatenate list of pandas dataframe
        try:
            self.samples = np.concatenate(input_arrays, axis = 0)
        except ValueError as err:
            logger = logging.getLogger(__name__)
            logger.error('files with inconsistent formats loaded from {}'.format(input_path))
            raise err

        # note one might end up with self.samples being an empty nd.array
        if self.samples.size == 0:
            self.samples.shape = (0,0)
            return

        # check that there are no duplicates (by sample-id)
        if self.samples.shape[0] != len(set(self.samples[:,0])):
            logger = logging.getLogger(__name__)
            logger.error('duplicate samples in chain loaded from {}'.format(input_path))
            raise ValueError




    def load_nonindexed_samples(self, input_path, batch):
        ''' load a subset of samples 

            arguments:
            ----------
            input_path : string
                relative path to files

            batch : int
                number of samples to return
        '''
        self.load_all_csv(input_path)
        # slice -- does not raise exception if indices out of range
        self.samples = self.samples[:batch,1:]

        if self.samples.shape[0] < batch:
            logger = logging.getLogger(__name__)
            logger.error('insufficient samples to complete analysis')
            raise IndexError



    def last_indexed_sample(self, input_path):
        ''' retrieves last sample generated in path 

            arguments:
            ----------
            input_path : string
                path to sample files
        '''
        self.load_all_csv(input_path)
        # there may be nothing there yet
        if self.samples.size == 0:
            return []
        # keep last sample
        return self.samples[np.argmax(self.samples[:,0])].tolist()
