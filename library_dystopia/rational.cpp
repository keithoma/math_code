/**
 * 11th October 2020
 * things to do: write handle float
 */

#include <cmath>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

namespace rational {

using RNL = RationalNumberLight;
using RNF = RationalNumberFlex;

RNL Rational::Construct(int n, int d) {
    const Sign sign = HandleSign(n, d);
    const pair<unsigned, unsigned> num_den = ReduceFraction(static_cast<unsigned> (abs(n)),
                                                            static_cast<unsigned> (abs(d)));
    return RNL {num_den.first, num_den.second, sign};
}

RNF Rational::Construct(float n, float d, bool s) {
    if (s == false) {
        return RNF {n, d, Sign::positive};
    } else {
        return RNF {n, d, Sign::negative};
    }
}

string Rational::StringTerminal(RNL q) {
    string str = "/";
    str = str.replace(2, 0, to_string(q.denominator));
    str = str.replace(0, 0, to_string(q.numerator));
    if (q.sign == Sign::negative) { str = str.replace(0, 0, "-"); };
    return str;
}

string Rational::StringLatex(RNL q) {
    string str = "\\frac{}{}";
    str = str.replace(8, 0, to_string(q.denominator));
    str = str.replace(6, 0, to_string(q.numerator));
    if (q.sign == Sign::negative) { str = str.replace(0, 0, "-"); };
    return str;
}


Sign Rational::HandleSign(int n, int d) {
    return (((n > 0) - (n < 0)) * ((d > 0) - (d < 0)) == 1) ? Sign::positive : Sign::negative;
}

pair<unsigned, unsigned> Rational::ReduceFraction(unsigned n, unsigned d) {
    const unsigned div = gcd(n, d);
    return make_pair(n / div, d / div);
}

} // namespace rational