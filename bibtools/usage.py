
def usage(name):
    ''' prints usage instructions
    '''
    print('\033[0;36m{:<16}\033[0m {:<7}'.format('usage', '')
        + ' : {}'.format(name)
        + ' [-h]'
        + ' [--project \033[0;33mname\033[0m]'
        + ' [--config \033[0;33mname\033[0m]')

    print('{:<16} {:<7}'.format('-h', '')
        + ' : help')

    print('{:<16} \033[0;33m{:<7}\033[0m'.format('--project', 'name')
        + ' : relative path to project directory')

    print('{:<16} \033[0;33m{:<7}\033[0m'.format('--config', 'name')
        + ' : relative path to configuration file')
