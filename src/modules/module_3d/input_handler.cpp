//
// input_handler.cpp
//
// manages command line arguments and input file parsing
//

#include "input_handler.h"

#include <sstream>

InputHandler::InputHandler(int argc, char ** argv)
{
    char ** i = argv;
    // number in test should match the required arguments in the body
    if (argc - 1 >= minArgNr_)
    {
        totalVolume_     = fromCString<long>(*(++i));
        sliceCount_      = fromCString<int>(*(++i));
        samplePeriod_    = fromCString<long>(*(++i));
        double xCoord    = fromCString<double>(*(++i)); 
        double yCoord    = fromCString<double>(*(++i));
        point_           = Point { xCoord, yCoord };
        sampleCount_     = fromCString<long long>(*(++i));
        minimumVolume_   = fromCString<int>(*(++i));
        matrixDimension_ = fromCString<long>(*(++i));
        writePeriod_     = fromCString<long>(*(++i));
        outputDir_       = std::string(*(++i));
    }
    else
    {
        throw ArgumentException { "too few command line arguments" };
    }

    if (argc - 1 == minArgNr_)
    {}
    else if (argc - 1 == minArgNr_ + sliceCount_ + 1)
    {
        sampleID_ = fromCString<long long>(*(++i));
        while (i - argv < argc - 1)
        {
            dataSet_.push_back(fromCString<long>(*(++i)));
        }
    }
    else
    {
        throw ArgumentException { "incorrect data type" };
    }

    // compute number of transformations to make during the simulation
    transformCount_ = computeTransformCount(sampleCount_, samplePeriod_);
}

long long InputHandler::computeTransformCount(long long sampleCount, long samplePeriod)
{
    return sampleCount * samplePeriod;
}
