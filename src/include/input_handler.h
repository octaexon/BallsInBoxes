//
// input_handler.h
//
// input: command line
//
// function: processes command line arguments
//
// output: simulation and configuration parameters
//

#ifndef INPUT_HANDLER_H
#define INPUT_HANDLER_H

#include "point.h"
#include "exceptions.h"

#include <string>
#include <vector>
#include <sstream>


// template string conversion
template <typename T> T fromCString(char const * cStr)
{
    std::string s { cStr };
    std::istringstream is { s };
    T t;
    if (!(is >> t))
    {
        throw ArgumentException { s + " -- invalid argument type" };
    }
    return t;
}


// holds an argument handler, configfile parser and datafile parser
// this is exposed to the user

class InputHandler 
{
    public:
        InputHandler(int argc, char ** argv);

       // need to retrieve config and data information
        Point     getPoint() const            { return point_; }
        long      getTotalVolume() const      { return totalVolume_; }
        int       getSliceCount() const       { return sliceCount_; }
        long      getSamplePeriod() const     { return samplePeriod_; } 
        long      getMatrixDimension() const  { return matrixDimension_; }
        int       getMinimumVolume() const    { return minimumVolume_; }
        long long getSampleCount() const      { return sampleCount_; }
        long      getWritePeriod() const      { return writePeriod_; }

        long long getSampleID() const         { return sampleID_; }

        // calculated parameters
        long long   getTransformCount() const { return transformCount_; }
        std::string getOutputDir() const { return outputDir_; }

        std::vector<long> const & getData() const { return dataSet_; }

    private:
        // supplied parameters
        Point       point_           { };
        long        totalVolume_     { 0 };
        int         sliceCount_      { 0 };
        long        samplePeriod_    { 0 };
        long        matrixDimension_ { 0 };
        int         minimumVolume_   { 1 };
        long long   sampleCount_     { 0 };
        long        writePeriod_     { 0 };
        std::string outputDir_       { "" };
        long long   sampleID_        { 0 };
        std::vector<long> dataSet_   { };

        // calculated parameters
        long long   transformCount_  { 0 };

        // calculators
        long long   computeTransformCount(long long sampleCount, long samplePeriod);

        int         minArgNr_         { 10 };
};

#endif
