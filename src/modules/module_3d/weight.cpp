// weight.cpp
//
// implements BIB weight for 3d model
//

#include "weight.h"
#include <cmath>


Weight::Weight(Point const & point) : point_(point)
{}

double Weight::operator()(long i, long j) const
{
    double kinetic = 2.0 * (i - j) * (i - j) * point_.x() / (i + j);
    double potential = (-2.0) * point_.y() / (i + j);

    return (-1.0) * (kinetic + potential);
}
