
from bibtools.key import ParameterKey

# phase coordinate keys
B1               = ParameterKey('b_1', float, 'B1')
B2               = ParameterKey('b_2', float, 'B2')

# generic plotter preferences
FIGURE_PREFS     = {'figsize' : (6,4)       , 'facecolor' : 'white'}
AXES_PREFS       = [0.17,0.15,0.75,0.79] 
MAJOR_TICK_PREFS = {'axis' : 'both', 'which' : 'major', 'labelsize' : 10}
MINOR_TICK_PREFS = {'axis' : 'both', 'which' : 'minor', 'labelsize' : 8}
