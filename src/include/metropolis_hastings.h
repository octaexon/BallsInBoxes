//
// metropolis_hastings.h
//
// implements Metropolis-Hastings routine
//

#ifndef METROPOLIS_HASTINGS_H
#define METROPOLIS_HASTINGS_H

#include "interface_space_time.h"
#include "acceptance_probability.h"

void metropolisHastings(ISpaceTime & st, AcceptanceProbability const & ap);

#endif
