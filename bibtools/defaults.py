''' central file for default values '''

from matplotlib.pyplot import cm

from bibtools.key       import ParameterKey
from bibtools.parameter import Parameter



## NAMES ##

# root project directory
PROJECT_DIR      = 'test/project'
# subdirectories of project containing major subparts 
DATA_DIR         = 'data'
ANALYSES_DIR     = 'analyses'
PLOTS_DIR        = 'plots'
# default configuration file
CONFIG_FILE      = 'test/test_config.csv'

# executable for simulator
SIMULATION_EXEC  = 'bin/bib3d'




## CONFIGURATION PARAMETER KEYS  ##

VOLUME           = ParameterKey('volume'          , int  , 'V')
TIME             = ParameterKey('time'            , int  , 'T')
PERIOD           = ParameterKey('period'          , int  , 'P')
BURN             = ParameterKey('burn'            , int  , 'B')
X                = ParameterKey('x'               , float, 'X')
Y                = ParameterKey('y'               , float, 'Y')
BATCH            = ParameterKey('batch'           , int  , 'S')


## SIMULATION PARAMETER KEYS ##

MINIMUM_VOLUME   = ParameterKey('minimum_volume'  , int  , 'MV')
MATRIX_DIMENSION = ParameterKey('matrix_dimension', int  , 'MD')
SAVE_INTERVAL    = ParameterKey('save_interval'   , int  , 'SI')

## SIMULATION PARAMETER VALUES ##
MINIMUM_VOLUME_VALUE   = 1
MATRIX_DIMENSION_VALUE = 2000
SAVE_INTERVAL_VALUE    = 100000


## PATH PARAMETER KEYS ##

OUTPUT_PATH      = ParameterKey('output_path'     , str  , 'OP')


## DATA PARAMETER KEYS ##

SEED             = ParameterKey('seed'            , int  , 'DS')


## STATISTICS PARAMETERS KEYS ##

GAMMA            = ParameterKey('gamma'           , float, 'GA')
SIGMA            = ParameterKey('sigma'           , float, 'SI')
DELTA            = ParameterKey('delta'           , float, 'DE')
AVG_DATA         = ParameterKey('avg_data'        , float, 'AD')
AVG_CENTRED_DATA = ParameterKey('avg_centred_data', float, 'ACD')


CORRELATED   = ParameterKey('correlated'        , Parameter, 'CORR')
LOCALIZED    = ParameterKey('localized'         , Parameter, 'LOCA')
ANTIFERRO    = ParameterKey('antiferromagnetic' , Parameter, 'ANTI')
DROPLET      = ParameterKey('droplet'           , Parameter, 'DROP')



# Phase object arguments are: name, gamma range, delta range, sigma range
# theoretic values of (gamma, sigma, delta)   [V = total_volume, W = width of droplet]
# correlated :        (>0.0 , ~1/V , >0.0)
# localized  :        (=0.0 , =1.0 , =0.0)
# antiferro  :        (=0.0 , ~2/V , =0.0)
# droplet    :        (=0.0 , ~1/W , >0.0)

# however convergence is bad, so interval must be made rather wide
# this could cause a problem with identifying antiferrormagnetic phase
# as it differs from the localized phase only by sigma parameter

# gamma > 0.0 is enough to pick out correlated phase
CORRELATED_TOLERANCES = {GAMMA : [0.005, 1.0], SIGMA : [0.0, 1.0], DELTA : [0.0, 1.0]}
# sigma ~ 1.0 is enough to pick out localized phase   #[0.995, 1.0]
LOCALIZED_TOLERANCES  = {GAMMA : [0.0, 0.005], SIGMA : [0.2, 1.0], DELTA : [0.0, 1.0]}
# finally the difference between antiferro and droplet is the differnce in delta
ANTIFERRO_TOLERANCES  = {GAMMA : [0.0, 0.005], SIGMA : [0.0, 0.2], DELTA : [0.0, 0.2]}
                                                                         #[0.0, 0.005]
DROPLET_TOLERANCES    = {GAMMA : [0.0, 0.005], SIGMA : [0.0, 0.2], DELTA : [0.2, 1.0]}



## PLOTTER ##

CORRELATED_PLOT_PREFS = {'color' : cm.RdYlGn(255) , 'alpha' : 0.5, 'marker' : (6,1)}
LOCALIZED_PLOT_PREFS  = {'color' : cm.autumn(255) , 'alpha' : 0.5, 'marker' : (4,1)}
ANTIFERRO_PLOT_PREFS  = {'color' : cm.seismic(50) , 'alpha' : 0.5, 'marker' : (5,1)}
DROPLET_PLOT_PREFS    = {'color' : cm.seismic(200), 'alpha' : 0.5, 'marker' : (3,1)}
