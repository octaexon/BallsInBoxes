//
// space_time_sampler.cpp
//
// collects snapshots of space time
//

#include "space_time_sampler.h"

SpaceTimeSampler::SpaceTimeSampler(ISpaceTime * st, long samplePeriod) :
    st_(st),
    sampleCounter_(0LL),
    sampleTime_(samplePeriod),
    samplePeriod_(samplePeriod)
{
    sampleCount_ = (st_->count() % samplePeriod == 0) ?
                    st_->count() / samplePeriod :
                    st_->count() / samplePeriod + 1;
}

// transforms the slices
void SpaceTimeSampler::transform(int loser, int gainer, double probability)
{
    st_->transform(loser, gainer, probability);

    if ((st_->counter() == sampleTime_) || st_->acquired())
    {
        // update time to next sample
        sampleTime_ += samplePeriod_;

        // take a sample
        for (auto i : st_->data())
        {
            samples_.push_back(i);
        }
        // record that sample has been taken
        ++sampleCounter_;
    }
}

// tests if goal is reached
bool SpaceTimeSampler::acquired() const
{
    if (sampleCounter_ >= sampleCount_)
    {
        return true;
    }
    return false;
}
