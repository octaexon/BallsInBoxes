//
// acceptance_probability.h
//
// acceptance probability scheme
//

#ifndef ACCEPTANCE_PROBABILITY_H
#define ACCEPTANCE_PROBABILITY_H

#include "interface_space_time.h"
#include "interface_transfer_factors.h"
#include <memory>

class AcceptanceProbability
{
    public:
        AcceptanceProbability(ITransferFactors * tf);
        double operator()(int loser, int gainer, ISpaceTime const & st) const; 

    private:
        std::unique_ptr<ITransferFactors> tf_;
};

#endif
