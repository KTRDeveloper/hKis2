#ifndef _bump_h_INCLUDED
#define _bump_h_INCLUDED

#include <stdbool.h>

struct kissat;

void kissat_bump_analyzed (struct kissat *);
void kissat_update_scores (struct kissat *);
void kissat_rescale_scores (struct kissat *);
void kissat_bump_variable (struct kissat *, unsigned idx);
void kissat_bump_score_increment (struct kissat *);
void pol_dec_act(struct kissat *);
void bump_pol_sc (struct kissat *, unsigned);

#define MAX_SCORE 1e150

#endif
