// interface_space_time.h
//
// abstract base class
//

#ifndef I_SPACE_TIME_H
#define I_SPACE_TIME_H

#include <vector>
#include "random_bool.h"

class ISpaceTime
{
    public:
        ISpaceTime() {}
        virtual ~ISpaceTime() {}

        // transforms the slices
        virtual void transform(int loser, int gainer, double probability) = 0; 

        // tests if goal is reached
        virtual bool acquired() const = 0;

        // getters
        virtual std::vector<std::vector<long>> const & data() const = 0; 
        virtual long const & slice(int index) const = 0;
        virtual int const & sliceCount() const = 0;
        virtual long long const & count() const = 0;
        virtual long long const & counter() const = 0;

        // setter
        virtual void tidyup() = 0;
};

#endif
