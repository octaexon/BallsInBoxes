import logging
from collections import OrderedDict

from bibtools.parameter import Parameter


class ParameterDict(OrderedDict):
    ''' OrderedDict holding Parameter objects '''

    def __init__(self):
        ''' initializes empty base OrderedDict '''
        super().__init__()


    def set_values_from_dict(self, values):
        ''' sets values of parameters

            arguments:
            ----------
            values : dict
                parameter name -> parameter value
        '''
        try:
            for parameter in self.values():
                parameter.values = values[parameter.key.name]
        except KeyError:
            pass
        except ValueError as err:
            logger = logging.getLogger(__name__)
            logger.warning('invalid values supplied to parameter')
            raise err 
