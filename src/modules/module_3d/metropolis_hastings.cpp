//
// metropolis_hastings.cpp 
//
// implements Metropolis-Hastings routine
//

#include "metropolis_hastings.h"
#include "random_integer.h"

void metropolisHastings(ISpaceTime & st, AcceptanceProbability const & ap)
{
    RandomInteger indexRandom;

    while(!st.acquired())
    {
        // slices upon which to perform transformation
        int loser;
        int gainer;

        // generate distinct random slices
        do
        {
            loser = indexRandom(0,st.sliceCount() - 1);
            gainer = indexRandom(0, st.sliceCount() - 1);
        }
        while (loser == gainer);

        // calculate acceptance probability
        double probability = ap(loser, gainer, st);

        // attempt to perform transformation
        st.transform(loser, gainer, probability);
    }
}
