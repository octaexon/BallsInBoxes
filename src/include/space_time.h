// space_time.h
//
// concrete implementation of space time 
//

#ifndef SPACE_TIME_H
#define SPACE_TIME_H


#include "interface_space_time.h"
#include "random_bool.h"

#include <vector>

class SpaceTime : public ISpaceTime
{
    public:
        SpaceTime(long volumeTotal, int sliceCount, int minimumVolume, long long transformCount,
                  std::vector<long> const & data);

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
        std::vector<std::vector<long>> data_;

        long volumeTotal_;
        int sliceCount_;

        // minimum volume per space time slice
        long const volumeSliceMin_;

        RandomBool transformRandom_;

        long long transformCount_;
        long long transformCounter_;
};


std::vector<std::vector<long>> const & SpaceTime::data() const
{
    return data_;
}

long const & SpaceTime::slice(int index) const
{ 
    // account for periodicity
    index = (index % sliceCount_ + sliceCount_) % sliceCount_;
    return data_[0][index]; 
}

int const & SpaceTime::sliceCount() const
{
    return sliceCount_;
}

long long const & SpaceTime::count() const
{
    return transformCount_;
}

long long const & SpaceTime::counter() const
{
    return transformCounter_;
}

void SpaceTime::tidyup()
{}

#endif
