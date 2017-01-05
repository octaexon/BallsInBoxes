import matplotlib.pyplot as plt
import logging

from   bibtools.container import ParameterDict
from   bibtools.phase     import Phase

from   bibtools.defaults  import CORRELATED, LOCALIZED, ANTIFERRO, DROPLET
from   bibtools.defaults  import CORRELATED_TOLERANCES, LOCALIZED_TOLERANCES, ANTIFERRO_TOLERANCES, DROPLET_TOLERANCES
from   bibtools.defaults  import CORRELATED_PLOT_PREFS, LOCALIZED_PLOT_PREFS, ANTIFERRO_PLOT_PREFS, DROPLET_PLOT_PREFS

from   bibtools.defaults  import X, Y

from   bibtools.plotsettings.phase   import *


class Diagram(ParameterDict):
    ''' holds and plots Phases '''
    def __init__(self):
        ''' initializes empty container for phases '''
        super().__init__()

        try:
            self[CORRELATED] = Phase(CORRELATED, CORRELATED_TOLERANCES, **CORRELATED_PLOT_PREFS)
            self[LOCALIZED]  = Phase(LOCALIZED , LOCALIZED_TOLERANCES , **LOCALIZED_PLOT_PREFS)
            self[ANTIFERRO]  = Phase(ANTIFERRO , ANTIFERRO_TOLERANCES , **ANTIFERRO_PLOT_PREFS)
            self[DROPLET]    = Phase(DROPLET   , DROPLET_TOLERANCES   , **DROPLET_PLOT_PREFS)
        except TypeError:
            logger = logging.getLogger(__name__)
            logger.error('phase initialization failing')
            raise TypeError


    def load(self, analysis, configuration):
        ''' loads parameters/statistics for testing+addition

            analysis : ParameterDict
                holds statistics

            configuration : ParameterDict
                holds configuration parameters
        '''
        for phase in self.values():
            if phase.contains(analysis):
                phase.add(configuration)

    def plot(self, output_file):
        ''' plots phases

            parameters:
            -----------
            output_file : string
                file to write plot
        '''
        # create subplot axes 
        fig  = plt.figure(**PLOT_FIGURE_PREFS)
        ax   = fig.add_axes(PLOT_AXES_PREFS) 

        plt.title(**PLOT_TITLE_PREFS)
        plt.xlabel(**PLOT_XLABEL_PREFS)
        plt.ylabel(**PLOT_YLABEL_PREFS)
        plt.xlim(*PLOT_XLIM_PREFS)
        plt.ylim(*PLOT_YLIM_PREFS)
        plt.tick_params(**PLOT_MAJOR_TICK_PREFS)
        plt.tick_params(**PLOT_MINOR_TICK_PREFS)

        for phase in self.values():
            # wrap in try block
            x_coordinates = [parameter.values for parameter in phase.values if parameter.key == X][0]
            y_coordinates = [parameter.values for parameter in phase.values if parameter.key == Y][0]

            ax.scatter(x_coordinates, y_coordinates, color = phase.color, alpha = phase.alpha, marker = phase.marker)

            plt.savefig(output_file, format = 'eps', dpi = 1000)
        plt.close()
