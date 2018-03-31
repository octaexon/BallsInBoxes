# BallsInBoxes

BallsInBoxes is a Markov-Chain-Monte-Carlo simulator for a class of statistical mechanical systems known as
balls-in-boxes models.  The default weights are pertinent for capturing volume
profiles of 2+1 causal dynamical triangulations within this simpler framework.

Results of the analysis are presented in:  
[D. Benedetti](https://sites.google.com/site/dariobene/), [J. Ryan](https://github.com/octaexon) : 
[Capturing the phase diagram of (2+1)-dimensional CDT using a balls-in-boxes model](https://arxiv.org/abs/1612.09533)


## Installation

1. Either download or clone the repository.
2. Move to code root directory: `cd BallsInBoxes`
3. Run: `./maker`
to compile the C++11 source code. 

##### Note: 
`maker` utilizes the Gnu compiler `g++`.

## Usage

`simulator` simulates and saves the sampling data. It is generally run as:
```bash
./simulator --project path/to/project --config path/to/config
```
Output is placed in a project `data` subdirectory.
A sample configuration file may be found in the `./test` directory. If options are
left unspecified, this configuration file is used by default and the output is
placed in a `./test/project/data` directory.

`analyser` analyses the data, calculating various observables/exponents. Again
this is called as:
```bash
./analyser --project path/to/project --config path/to/config
```
Output is placed in a project `analyses` subdirectory.


`plotphase` and `plotexponent` utilize the matplotlib library to produce phase
diagram plots and exponent plots across phase transitions.  As usual:
```bash
./plotphase --project path/to/project --config path/to/config
./plotexponent --project path/to/project --config path/to/config
```
Output is placed in a project `plots` subdirectory.

## Customization

The weights for the model can be customized by changing the contents of
`./src/modules/module_3d/weight.cpp`.

There are also several configuration files at:
```bash
./bibtools/defaults.py
./bibtools/plotsettings/phase.py
./bibtools/plotsettings/exponent.py
```
