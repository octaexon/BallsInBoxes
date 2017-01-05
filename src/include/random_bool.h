// random_bool.h
//
// generates a random boolean
//

#ifndef RANDOM_BOOL_H
#define RANDOM_BOOL_H

#include <random>


class RandomBool
{
    public:
        RandomBool() : generator_(std::random_device()()) {}

        bool operator()(double probability)
        {
            std::bernoulli_distribution boolRandom(probability);
            return boolRandom(generator_);
        }

    private:
        std::mt19937 generator_;
};


#endif
