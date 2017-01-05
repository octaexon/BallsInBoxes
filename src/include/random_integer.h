// random_integer.h
//
// generates a random integer
//

#ifndef RANDOM_INTEGER_H
#define RANDOM_INTEGER_H

#include <random>


class RandomInteger
{
    public:
        RandomInteger() : generator_(std::random_device()()) {}

        int operator()(double limitLower, double limitUpper)
        {
            std::uniform_int_distribution<int> integerRandom(limitLower, limitUpper);
            return integerRandom(generator_);
        }

    private:
        std::mt19937 generator_;
};


#endif
