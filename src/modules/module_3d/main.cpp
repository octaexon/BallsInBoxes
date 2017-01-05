//
// main.cpp
//
// drives an MCMC for a BIB model of spacetime
//

#include "input_handler.h"

#include "weight.h"
#include "transfer_factors.h"
#include "acceptance_probability.h"

#include "space_time.h"
#include "space_time_sampler.h"
#include "space_time_writer.h"

#include "metropolis_hastings.h"

#include <string>
#include <iostream>

int main(int argc, char ** argv)
{

    try
    {
        InputHandler ih { argc, argv };

        // create acceptance probability calculator object
        AcceptanceProbability ap 
        { 
            new TransferFactors 
            { 
                new Weight
                { 
                    ih.getPoint() 
                }, 
                    ih.getMatrixDimension() 
            } 
        };

        // create a space time sampler writer
        SpaceTimeWriter sw 
        { 
            new SpaceTimeSampler 
            { 
                new SpaceTime 
                { 
                    ih.getTotalVolume(), ih.getSliceCount(), ih.getMinimumVolume(),
                        ih.getTransformCount(), ih.getData() 
                },
                    ih.getSamplePeriod() 
            },
                ih.getWritePeriod(), ih.getOutputDir(), ih.getSampleID() 
        };

        // run simulation
        metropolisHastings(sw, ap);
    }
    catch(ArgumentException const & ie)
    {
        std::cerr << "\n";
        std::cerr << ie.what() << " ---> ";
        std::cerr << ie.getReason() << std::endl;
    }
}
