//
// transfer_factors.cpp
// 
// matrices of precomputed weight factors
//

#include "transfer_factors.h"
#include <cmath>

TransferFactors::TransferFactors(IWeight * w, long dimension) :
    w_(w),
    dimension_(dimension),
    alpha_(dimension * dimension),
    beta_(dimension * dimension),
    gamma_(dimension * dimension),
    delta_(dimension * dimension)
{
    // a. we compute the factor matrices for:
    // alpha_       : [1, dimension - 1] x [1, dimension - 1] -> R
    // beta_        : [1, dimension - 1] x [1, dimension - 1] -> R
    // gamma_       : [1, dimension - 1] x [1, dimension - 1] -> R
    // delta_       : [1, dimension - 1] x [1, dimension - 1] -> R
    // 
    // this means that we must ensure that the weight object can be evalualated
    // at lattice point in the upper right quadrant, including the axes, but not
    // necessarily the origin.

    for (long i = 1; i < dimension; ++i)
    {
        for(long j = 1; j < dimension; ++j)
        {
            // precompute element weights_(i, j)
            double denominator = (*w_)(i, j); 

            alpha_[i * dimension + j] = std::exp((*w_)(i, j - 1)     - denominator);
            beta_[i * dimension + j]  = std::exp((*w_)(i - 1, j)     - denominator);
            gamma_[i * dimension + j] = std::exp((*w_)(i - 1, j + 1) - denominator);
            delta_[i * dimension + j] = std::exp((*w_)(i + 1, j - 1) - denominator);
        }
    }
}

double TransferFactors::alpha(long i, long j) const
{ 
    // if precomputed, return
    if (i < dimension_ && j < dimension_)
    {
        return alpha_[i * dimension_ + j];
    }
    // else calculate from scratch
    else
    {
        return std::exp((*w_)(i, j - 1) - (*w_)(i, j));
    }
}

double TransferFactors::beta(long i, long j) const
{ 
    // if precomputed, return
    if (i < dimension_ && j < dimension_)
    {
        return beta_[i * dimension_ + j];
    }
    // else calculate from scratch
    else
    {
        return std::exp((*w_)(i - 1, j) - (*w_)(i, j));
    }
}

double TransferFactors::gamma(long i, long j) const
{ 
    // if precomputed, return
    if (i < dimension_ && j < dimension_)
    {
        return gamma_[i * dimension_ + j];
    }
    // else calculate from scratch
    else
    {
        return std::exp((*w_)(i - 1, j + 1) - (*w_)(i, j));
    }
}

double TransferFactors::delta(long i, long j) const
{ 
    // if precomputed, return
    if (i < dimension_ && j < dimension_)
    {
        return delta_[i * dimension_ + j];
    }
    // else calculate from scratch
    else
    {
        return std::exp((*w_)(i + 1, j - 1) - (*w_)(i, j));
    }
}
