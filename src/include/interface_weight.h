//
// interface_weight.h
//
// abstract weight class
//

#ifndef I_WEIGHT_H
#define I_WEIGHT_H

class IWeight
{
    public:
        IWeight() {}
        virtual ~IWeight() {}
        virtual double operator()(long i, long j) const = 0;
};

#endif
