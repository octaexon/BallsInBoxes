// acceptance_probability_transfer.cpp
//
// acceptance probability scheme
//

#include "acceptance_probability.h"

AcceptanceProbability::AcceptanceProbability(ITransferFactors * tf) :
    tf_(tf)
{}

double AcceptanceProbability::operator()(int loser, int gainer, ISpaceTime const & st) const
{
    double quotient;

    // accounting for periodicity (annoying, acceptance probability should not
    // see this part of the implementation -- the condition should just be:
    // gainer - loser == 1 etc
    if ((gainer - loser == 1) || (gainer - loser == 1 - st.sliceCount()))
    {
        quotient = tf_->alpha(st.slice(loser - 1), st.slice(loser))
                   * tf_->gamma(st.slice(loser), st.slice(loser + 1))
                   / tf_->beta(st.slice(loser + 1) + 1, st.slice(loser + 2));
    }

    else if ((gainer - loser == -1) || (gainer - loser == st.sliceCount() - 1))
    {
        quotient = tf_->delta(st.slice(loser - 1), st.slice(loser))
                   * tf_->beta(st.slice(loser), st.slice(loser + 1))
                   / tf_->alpha(st.slice(loser - 2), st.slice(loser - 1) + 1);
    }

    else
    {
        quotient = tf_->alpha(st.slice(loser - 1), st.slice(loser))
                   * tf_->beta(st.slice(loser), st.slice(loser + 1))
                   / (tf_->alpha(st.slice(gainer - 1), st.slice(gainer) + 1)
                      * tf_->beta(st.slice(gainer) + 1, st.slice(gainer + 1)));
    }
    // calculate acceptance probability
    return (quotient < 1.0 ? quotient : 1.0);
}



