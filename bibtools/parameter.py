import logging
from bibtools.key import ParameterKey


class Parameter:
    ''' parameter attributes and validation '''
    def __init__(self, key, values = []):
        ''' initializes valueless parameter 

            arguments:
            ----------
            key : ParameterKey object
                parameter key

            values : list
                values to be assigned to parameter
        '''
        self.key     = key
        self._values = None
        # use @values.setter
        self.values = values

    @property
    def values(self):
        ''' retrieves values as list '''
        return self._values

    @values.setter
    def values(self, values):
        ''' assigns values

            arguments:
            ----------
            values : object of type key.type OR
                     str convertible to type key.type OR
                     list with elements of type key.type OR
                     list with str elements convertible to type key.type
                values to be assigned
        '''
        # ensure list supplied
        if not (type(values) is list):
            values = [values]

        # load list element by element, converting type if necessary
        self._values = []
        for v in values:
            if type(v) is str:
                try:
                    v_value = self.key.type(v) 

                except ValueError as err:
                    logger = logging.getLogger(__name__)
                    logger.error('parameter attributes {} incompatible with (type, value) = ({},{})'.format(self.key, type(v), v))
                    raise TypeError

                self._values.append(v_value)

            elif not (type(v) is self.key.type):
                logger = logging.getLogger(__name__)
                logger.error('parameter attributes {} incompatible with (type, value) = ({},{})'.format(self.key, type(v), v))
                raise TypeError

            else:
                self._values.append(v)


    def __repr__(self):
        ''' string representation suitable for logging '''
        return self.key.name + ' : {:>6}'.format(' , '.join([str(v) for v in self._values]))


    def __str__(self):
        ''' string representation (abbreviated) suitable for path names '''
        return self.key.token + '_' + '_'.join(str(v) for v in self._values)

    def to_command_line(self):
        ''' list representation suitable for command line element '''
        #return ['--' + self.key.name] + [str(v) for v in self._values]
        return [str(v) for v in self._values]

    def to_csv(self):
        ''' list representation suitable as csv row '''
        return [self.key.name] + [str(v) for v in self._values]
