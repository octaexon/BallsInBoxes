//
// space_time.cpp
//
// concrete implementation of space time
//

#include "space_time.h"
#include "random_integer.h"

SpaceTime::SpaceTime(long volumeTotal, int sliceCount, int minimumVolume,
                     long long transformCount, std::vector<long> const & data) :
    data_(1,std::vector<long>(sliceCount)),
    volumeTotal_(volumeTotal),
    sliceCount_(sliceCount),
    volumeSliceMin_(minimumVolume),
    transformCount_(transformCount),
    transformCounter_(0LL)
{
    if (data.size() != 0)
    {
        data_[0] = data;
    }
    else
    {
        // randomly distributes volume among slices

        //  Implementation: 
        //  
        //  draws from a uniform distribution over the set of ways to assign
        //  "volumeTotal" indistinguishable balls to "sliceCount" distinguishable
        //  slices and outputs that assignment.  The probability of any given
        //  configuration is:
        // 
        //       {(volumeTotal - (volumeSliceMinimum - 1) * sliceCount - 1) choose (sliceCount - 1)}^{-1}
        //  
        //  1. the "volumeTotal - (volumeSliceMinimum - 1) * sliceCount" balls are placed in a line
        //  2. they are separated by empty "slots"
        //  3. into "sliceCount - 1" of these slots are placed dividers,
        //     at random and drawn from uniform distributions with diminishing range.
        //     Each such configuration has probability:
        // 
        //        (volumeTotal - volumeSliceMinimum * sliceCount)! / (volumeTotal - (volumeSliceMinimum - 1) * sliceCount - 1)!
        // 
        //  4. this assigns the balls to the slices
        //  5. However, retaining only the number of balls in each slice, rather than
        //     the order in which the slice dividers were randomly placed, accounts
        //     for the missing factor of:
        // 
        //        (sliceCount - 1)!
        //

        RandomInteger indexRandom;

        // used to test whether a slot is as yet used up
        bool const used   = true;
        bool const unused = false;


        // initialize a vector of unused slots
        long const slotCount    = volumeTotal_ - (volumeSliceMin_ - 1) * sliceCount_ - 1;
        int  const dividerCount = sliceCount_ - 1;
        std::vector<bool> slotState(slotCount, unused);


        // assigment of dividers to slots
        for (long slotFreeCount = slotCount; slotFreeCount > slotCount - dividerCount;
                --slotFreeCount) {
            // draw from this uniform distribution
            long slotIndex = 0;
            long slotFreeIndex = indexRandom(0, slotFreeCount - 1);

            // slotFreeIndex does not account for used slots
            // count along the line of slots
            // skip if it is already in use
            while (slotFreeIndex >= 0) {
                if (slotState[slotIndex] == unused)
                {
                    --slotFreeIndex;
                }
                ++slotIndex;
            }
            slotState[slotIndex - 1] = used;
        }

        // calculation of contents of each slice
        long slotIndex = 0;
        long slotPrevIndex = -1;

        for (int sliceIndex = 0; sliceIndex < sliceCount_; ++sliceIndex) {
            if (sliceIndex == sliceCount_ - 1) 
                // slotPrevIndex = (actual position - 1) => - 1 term on rhs 
                data_[0][sliceIndex] = volumeTotal_ - slotPrevIndex - 1 + (volumeSliceMin_ - 1);
            else {
                while(slotState[slotIndex] == unused)
                    ++slotIndex;
                data_[0][sliceIndex] = slotIndex - slotPrevIndex + (volumeSliceMin_ - 1);

                slotPrevIndex = slotIndex;
                // shift so that it does not immediately fail condition
                ++slotIndex;
            }
        }
    }
}

// transfers volume from one slice to another
void SpaceTime::transform(int loser, int gainer, double probability)
{
    // should satisfy minimal volume constraint
    if (data_[0][loser] > volumeSliceMin_ && transformRandom_(probability))
    {
        // perform move
        --data_[0][loser];
        ++data_[0][gainer];
    }
    // this records **attempted** transformations
    // to record **successful** transformations, move this inside the above
    // conditional block 
    ++transformCounter_; 
}


// tests if goal is reached - specified number of transformations
bool SpaceTime::acquired() const 
{
    if (transformCounter_ >= transformCount_)
    {
        return true;
    }
    return false;
}
