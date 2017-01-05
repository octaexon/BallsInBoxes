//
// space_time_writer.cpp
//
// writes space time(s) to disk
//

#include "space_time_writer.h"
#include <sstream>
#include <fstream>
#include <iomanip>
#include <ctime>

SpaceTimeWriter::SpaceTimeWriter(ISpaceTime * st, long writePeriod, std::string const & outputDir, long long zeroCount) :
    st_(st),
    writeCounter_(0LL),
    writeTime_(writePeriod),
    writeZeroCount_(zeroCount),
    writePeriod_(writePeriod),
    outputDir_(outputDir)
{
    // needed for correct filename
    writeRemainder_ = st_->count() % writePeriod_;

    if (writeRemainder_ == 0)
    {
        writeCount_     = st_->count() / writePeriod_;
    }
    else
    {
        writeCount_     = st_->count() / writePeriod_ + 1;
    }
}

// transforms the slices
void SpaceTimeWriter::transform(int loser, int gainer, double probability)
{
    st_->transform(loser, gainer, probability);

    if ((st_->counter() == writeTime_) || st_->acquired())
    {
        // update time to next write
        writeTime_ += writePeriod_;

        // create file name from components
        std::stringstream ss;
        ss << outputDir_;
        ss << "/" << getTimeStamp();
        ss << "." << extension_;
        std::string fileName = ss.str();

        // open a file
        std::ofstream data;
        data.open(fileName);

        // write samples to file
        long long sampleID = writeZeroCount_ + writeCounter_ * writePeriod_ + 1;
        for (auto i : st_->data())
        {
            data << sampleID;
            for (auto j : i)
            {
            data << "," << j;
            }
            data << std::endl;
            ++sampleID;
        }

        // record that samples have been written
        ++writeCounter_;
        // perform some cleaning
        st_->tidyup();

    }
}

// tests if goal is reached
bool SpaceTimeWriter::acquired() const
{
    if (writeCounter_ >= writeCount_)
    {
        return true;
    }
    return false;
}

std::string SpaceTimeWriter::getTimeStamp() const
{
    std::time_t now { std::time(nullptr) };
    char timeStamp[100];
    std::strftime(timeStamp, sizeof(timeStamp), "%Y_%b_%d__%H_%M_%S", std::localtime(&now));
    return timeStamp;
}
