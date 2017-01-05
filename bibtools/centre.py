''' centres data
    
    functions:
    ----------
    centre_samples : centres array of samples
    centre_sample  : helper function that centres individual sample
'''


import numpy as np

def centre_sample(sample):
    ''' centres data sample

            parameters:
            -----------
            sample : 1d numpy array
                    uncentred data sample, along with splitting index as last entry

            returns:
            --------
            centred sample : 1d numpy array
                centred data sample

            methodology:
                 split array along index specified by final entry, remembering to discard final entry
                 swap two parts
        '''
    return np.append(sample[sample[-1]:-1], sample[:sample[-1]])


def centre_samples(samples):
    ''' centres data samples

        parameters:
        -----------
        samples : 2d numpy array
            uncentred data samples

        returns:
        --------
        centred_samples : 1d numpy array
            centred data samples

        methodology:
        ------------
        compute centres of mass of each sample
        centre data, sample by sample, by rotating enough elements to the front, row by row
    '''  
    # number of samples and number of elements in each sample
    total_samples, sample_size = samples.shape

    # midpoint of the sample, rounded down if the sample has an odd number of elements
    midpoint_index = sample_size // 2

    # angle between nearest-neighbour element pairs, when placed on circle
    segment_angle = 2 * np.pi / sample_size

    # compute points on circle to place volumes : shape (sample size, 2)
    circle_points = np.column_stack((np.cos(np.arange(sample_size) * segment_angle), np.sin(np.arange(sample_size) * segment_angle)))

    # centres of volume for samples = matrix multiplication (samples array * circle points array)
    # up to rescaling by total volume 
    centre_points = np.dot(samples, circle_points)

    # compute angle between line (centre of volume -> origin) and +ve x-axis
    # angle = arctan(y,x)
    # range : (-pi, pi]
    centre_angles  = np.arctan2(centre_points[:,1], centre_points[:,0])

    # compute nearest index to centre of volume
    # range : [-sample size // 2, sample size // 2]
    # e.g. for sample_size = 12, [-6, 6]; sample_size = 11, [-5, 5]
    # n.b. for even sample_size : -sample_size // 2 = sample_size // 2
    #      so one of the indices is represented twice, but this has zero effect 
    #      as subsequent manipulations erase this feature
    centre_indices = np.rint(centre_angles / segment_angle).astype(int)

    # compute index at which to slice the sample
    # as viewed on the line:
    #      centre to left of midpoint
    #         centre_index > 0
    #         displacement = centre_index - midpoint_index < 0
    #         => split should be made at : displacement + sample_size
    #      centre to right of midpoint
    #         centre_index < 0
    #         centre_index + sample_size > 0
    #         displacement = centre_index + sample_size - midpoint_index > 0
    #         => split should be made at : displacement
    #      centre at midpoint
    #         displacement = 0
    #         take modulus to deal with this special case
    splitting_indices = np.mod(centre_indices - midpoint_index + sample_size, sample_size); 

    # compute centred samples
    # reshape splitting_indices array : (1, total_samples) -> (total_samples, 1)
    # concatenate splitting_indices to samples as last column
    # centre each row (axis = 1) of resulting array
    return np.apply_along_axis(centre_sample, 1, np.concatenate((samples, splitting_indices.reshape(total_samples,1)), axis = 1))
