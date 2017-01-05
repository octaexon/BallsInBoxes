// weight.h
//
// implements BIB weight
//

#ifndef WEIGHT_H
#define WEIGHT_H

#include "interface_weight.h"
#include "point.h"

class Weight : public IWeight
{
    public:
        Weight(Point const & point);
        double operator()(long i, long j) const override;

    private:
        Point point_; 
};


#endif
