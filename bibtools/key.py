import logging

class ParameterKey:
    ''' custom keys for parameters '''
    def __init__(self, name, value_type, token):
        ''' initializes valueless entity along with its attributes

            arguments:
            -----------
            name : string
                name of parameter

            value_type : type
                parameter type 

            token : string
                abbreviated name of parameter
        '''
        self.name      = name
        self.type      = value_type
        self.token     = token

    def __hash__(self):
        ''' allow for use as dict key '''
        return hash(str(self.name) + str(self.type) + str(self.token))

    def __eq__(self, other):
        ''' allow for use as dict key

            parameters:
            -----------
            other : BibAttr object
        '''
        return (self.name == other.name and self.type == other.type and self.token == other.token)

    def __repr__(self):
        ''' string representation of key '''
        return '( ' + ' : '.join([self.name, str(self.type), self.token]) + ' ) '

