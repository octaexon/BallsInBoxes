//
// transfer_factors.h
//
// matrices of precomputed weight factors
//

#ifndef TRANSFER_FACTORS_H
#define TRANSFER_FACTORS_H

#include "interface_transfer_factors.h"
#include "interface_weight.h"
#include <memory>
#include <vector>

class TransferFactors : public ITransferFactors
{
    public:
        TransferFactors(IWeight * w, long dimension);

        double alpha(long i, long j) const override;
        double beta(long i, long j) const override;
        double gamma(long i, long j) const override;
        double delta(long i, long j) const override;

    private:
        std::unique_ptr<IWeight> w_;
        int dimension_;

        std::vector<double> alpha_;
        std::vector<double> beta_;
        std::vector<double> gamma_;
        std::vector<double> delta_;
};

#endif
