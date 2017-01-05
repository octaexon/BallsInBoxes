from bibtools.container import ParameterDict
from bibtools.parameter import Parameter
from bibtools.defaults  import (GAMMA, SIGMA, DELTA, X, Y)

class Phase(Parameter, ParameterDict):
    ''' characterizes a phase within the phase space '''
    def __init__(self, key, tolerances, color, alpha, marker):
        ''' initializes attributes

            parameters:
            -----------
            key : string
                name of phase

            color : string
                1-character color id for matplotlib

            alpha : float
                alpha value for matplotlib

            tolerances : list of three 2-element lists
                tolerance allowed in statistics : gamma, sigma, delta
        '''
        Parameter.__init__(self, key, [Parameter(X), Parameter(Y)])
        ParameterDict.__init__(self)

        self[GAMMA] = Parameter(GAMMA, tolerances[GAMMA])
        self[SIGMA] = Parameter(SIGMA, tolerances[SIGMA])
        self[DELTA] = Parameter(DELTA, tolerances[DELTA])

        # plot preferences
        self.color = color
        self.alpha = alpha
        self.marker = marker


    def contains(self, analysis):
        ''' tests that phase contains configuration point

            parameters:
            -----------
            analysis : ParameterDict object
        '''
        # run through tolerances loaded into Phase
        # chack only those Statistics from supplied dict
        for key, parameter in self.items():
            if not (parameter.values[0] <= analysis[key].values[0] <= parameter.values[1]):
                return False
        return True

    def add(self, coordinates):
        ''' add coordinates to phase

            parameters:
            -----------
            coordinates : ParameterDict
        '''
        # run through parameters loaded into Phase
        # add only those parameters from the supplied dict
        for coordinate in self.values:
            coordinate.values += coordinates[coordinate.key].values
