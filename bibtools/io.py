import getopt
import os
from   csv      import (DictReader, reader, writer)
from   datetime import datetime

import logging
import sys

from   bibtools.defaults import (PROJECT_DIR, CONFIG_FILE)


class CommandLineError(Exception):
    def __init__(self, message = ''):
        self.message = message


class HelpInterrupt(Exception):
    pass





def parse_command_line(argv):
    ''' parse command line options

        arguments:
        ----------
        argv : list of strings
            command line options

        methodology:
        ------------
        parses command line using getopt library

        options types:
        --------------
        h       : help
        project : relative path to root directory
        config  : relative path to configuration file

        returns:
        --------
        project_dir : string
        config_file : string
            names
    '''
    project_dir = PROJECT_DIR
    config_file = CONFIG_FILE


    try:
        opts, args = getopt.getopt(argv, 'h', ['project=', 'config='])
    except getopt.GetoptError as err:
        logger = logging.getLogger(__name__)
        logger.error('command line {}'.format(sys.exc_info()[1]))
        raise CommandLineError()

    for opt, arg in opts:
        if opt == '-h':
            raise HelpInterrupt

        elif opt == '--project':
            project_dir = arg

        elif opt == '--config':
            config_file = arg

        else:
            logger = logging.getLogger(__name__)
            logger.error('unhandled option : ({}, {})'.format(opt, arg))
            raise BibIOError()

    return (project_dir, config_file)



def read_config_csv(input_file):
    ''' reads configuration file into dict

        parameters:
        -----------
        input_file : string
            configuration file name
    '''
    try:
        source = open(input_file, 'r')
    except FileNotFoundError as err:
        logger = logging.getLogger(__name__)
        logger.error('unable to open configuration file {}'.format(input_file))
        raise err

    with source:
        rdr = DictReader(source)
        contents = [row for row in rdr]
        return contents


def read_analysis_csv(input_file):
    ''' reads analysis file into dict

        parameters:
        -----------
        input_file : string
            analysis file name
    '''
    try:
        source = open(input_file, 'r')
    except FileNotFoundError as err:
        logger = logging.getLogger(__name__)
        logger.error('unable to open analysis file {}'.format(input_file))
        raise err

    with source:
        rdr = reader(source)
        contents = {line[0] : line[1:] for line in rdr}
        return contents


def write_analysis_csv(output_file, *containers):
    ''' writes analysis file

        parameters:
        -----------
        output_file : string
            analysis file name

        *containers : ParameterDict objects
    '''
    with open(output_file, 'w') as terminus:
        wtr = writer(terminus)
        for c in containers:
            for parameter in c.values():
                wtr.writerow(parameter.to_csv())



def generate_base_path(project_path, task_path):
    ''' generates folder structure

        parameters:
        -----------
        project_path : string
            relative path to root project directory

        task_path : string
            relative path to base of task at hand

        methodology:
        ------------
        generate/ensure folder structure
    '''
    # path to task directory
    base_path    = os.path.join(project_path, task_path)

    try:
        os.mkdir(project_path)
    except FileExistsError:
        pass
    except FileNotFoundError as err:
        logger = logging.getLogger(__name__)
        logger.error('unable to generate project path {}'.format(project_path))
        raise err

    try:
        os.mkdir(base_path)
    except FileExistsError:
        pass
    except FileNotFoundError as err:
        logger = logging.getLogger(__name__)
        logger.error('unable to generate base path{}'.format(base_path))
        raise err

    return base_path


def generate_analysis_filename(output_path, identifier):
    ''' generates analysis file

        arguments:
        ----------
        output_path : string
            relative path

        identifier  : string
            file name

        returns:
        --------
        output_file : string
            full file name

        notes:
        ------
        returns file structure:
            output_path / identifier + extension
    '''
    # construct file name
    output_file = os.path.join(output_path, identifier + '.csv')

    return output_file




def generate_plot_file(root_path):
    ''' generates plots file structure

        parameters:
        -----------

        root_path : string
            relative path

        methodology:
        ------------
        generate file name

        notes:
        ------
        returns file structure:
            root_path / current timestamp + extension
    '''
    # construct file name
    plots_file = os.path.join(root_path, '{}'.format(datetime.now().strftime('%Y_%b_%d__%H_%M_%S_%f')) + '.eps')

    return plots_file
