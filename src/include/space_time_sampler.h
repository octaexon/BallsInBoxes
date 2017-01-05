//
// space_time_sampler.h
//
// collects space time samples
//

#ifndef SPACE_TIME_SAMPLER_H
#define SPACE_TIME_SAMPLER_H

#include "interface_space_time.h"
#include <vector>
#include <memory>

class SpaceTimeSampler : public ISpaceTime
{
    public:
        SpaceTimeSampler(ISpaceTime * st, long samplePeriod);

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
        std::vector<std::vector<long>> samples_;

        long long sampleCount_;
        long long sampleCounter_;
        long long sampleTime_;

        long samplePeriod_;
};


std::vector<std::vector<long>> const & SpaceTimeSampler::data() const
{
    return samples_;
}

long const & SpaceTimeSampler::slice(int index) const
{
    return st_->slice(index);
}

int const & SpaceTimeSampler::sliceCount() const
{
    return st_->sliceCount();
}

long long const & SpaceTimeSampler::count() const
{
    return sampleCount_;
}

long long const & SpaceTimeSampler::counter() const
{
    return sampleCounter_;
}

void SpaceTimeSampler::tidyup()
{
    samples_.clear();
}


#endif
