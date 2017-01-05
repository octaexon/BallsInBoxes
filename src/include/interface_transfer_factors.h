//
// interface_transfer_factors.h
//
// abstract factors class
//

#ifndef I_TRANSFER_FACTORS_H
#define I_TRANSFER_FACTORS_H

class ITransferFactors
{
    public:
        ITransferFactors() {}
        virtual ~ITransferFactors() {}

        virtual double alpha(long i, long j) const = 0;
        virtual double beta(long i, long j) const = 0;
        virtual double gamma(long i, long j) const = 0;
        virtual double delta(long i, long j) const = 0;
};

#endif
