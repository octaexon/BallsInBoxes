//
// space_time_writer.h
//
// writes space time(s) to disk
//

#ifndef SPACE_TIME_WRITER_H
#define SPACE_TIME_WRITER_H

#include "interface_space_time.h"
#include <vector>
#include <memory>
#include <string>

class SpaceTimeWriter : public ISpaceTime
{
    public:
        SpaceTimeWriter(ISpaceTime * st, long writePeriod, std::string const & outputDir, long long zeroCount = 0LL);

        // transforms the slices
        void transform(int loser, int gainer, double probability) override;

        // tests if goal is reached
        bool acquired() const override;

        // getters
        inline std::vector<std::vector<long>> const & data() const override;
        inline long const & slice(int index) const override;
        inline int const & sliceCount() const override;
        inline long long const & count() const override;
        inline long long const & counter() const override;

        // setter
        inline void tidyup() override;

    private:
        std::unique_ptr<ISpaceTime> st_;

        long long writeCount_;
        long long writeCounter_;
        long long writeTime_;

        // needed if number of objects to be written is not a multiple of the
        // writeperiod
        long long writeRemainder_;
        long long writeZeroCount_;

        long writePeriod_;

        // write information
        std::string outputDir_;
        std::string const extension_ = "csv";

        std::string getTimeStamp() const;
};


std::vector<std::vector<long>> const & SpaceTimeWriter::data() const
{
    return st_->data();
}

long const & SpaceTimeWriter::slice(int index) const
{
    return st_->slice(index);
}

int const & SpaceTimeWriter::sliceCount() const
{
    return st_->sliceCount();
}

long long const & SpaceTimeWriter::count() const
{
    return writeCount_;
}

long long const & SpaceTimeWriter::counter() const
{
    return writeCounter_;
}

void SpaceTimeWriter::tidyup()
{}

#endif
