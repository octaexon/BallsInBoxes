import numpy  as np

import logging


from bibtools.container import ParameterDict
from bibtools.parameter import Parameter

from bibtools.defaults  import (GAMMA, SIGMA, DELTA, AVG_DATA, AVG_CENTRED_DATA)

from bibtools.centre    import centre_samples


class Analysis(ParameterDict):
    def __init__(self):
        # initialize empty ParameterDict
        super().__init__()

        # load default parameters
        self[GAMMA]            = Parameter(GAMMA)
        self[SIGMA]            = Parameter(SIGMA)
        self[DELTA]            = Parameter(DELTA)
        self[AVG_DATA]         = Parameter(AVG_DATA)
        self[AVG_CENTRED_DATA] = Parameter(AVG_CENTRED_DATA)

    def analyse(self, samples): 
        ''' analyse observable properties of samples from markov chain

        arguments:
        -----------
        samples : numpy array
            holds input samples to be analysed

        methodology:
        ------------
        produces statistics:
            (sigma                      : float 
             delta                      : float 
             gamma                      : float 
             average of samples         : list of floats 
             average of centred samples : list of floats)
        '''
        # centre samples
        centred_samples = centre_samples(samples)

        # shifted (by 1) samples (needed for delta)
        shifted_samples = np.concatenate((samples[:,1:], samples[:,:1]), axis = 1)

        # useful powers of total volume
        volume = np.sum(samples[0])
        volume_squared = volume ** 2

        # sample sigma = sum of squared volumes / total volume squared
        sigma_sample = np.sum(samples * samples / volume_squared, axis = 1)

        # sample delta = sum of absolute differences / (2 * total volume)
        delta_sample = (np.sum(  np.absolute(samples - shifted_samples)   , axis = 1)  / (2 * volume)  )

        # sample gamma = 1 / minimum volume occurring in the sample
        gamma_sample = 1 / np.amin(samples, axis = 1)

        # average over the all samples
        self[GAMMA].values            = float(1 - np.mean(gamma_sample))
        self[SIGMA].values            = float(np.mean(sigma_sample))
        self[DELTA].values            = float(1 - np.mean(delta_sample))
        self[AVG_DATA].values         = np.mean(samples, axis = 0).tolist()
        self[AVG_CENTRED_DATA].values = np.mean(centred_samples, axis = 0).tolist()
