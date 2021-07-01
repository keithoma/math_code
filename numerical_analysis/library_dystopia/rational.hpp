/**
 * 11th October 2020
 * things to do: write handle float
 */

#pragma once

#include <string>
#include <utility>

enum class Sign {
    positive,
    negative
};

enum class Mode {
    light,
    flex
};

namespace rational {

// light version for computing
struct RationalNumberLight {
    RationalNumberLight(unsigned n, unsigned d, Sign s)
        : numerator{n},
          denominator{d},
          sign{s}
    {}
    const unsigned short numerator;
    const unsigned short denominator;
    const Sign sign;
};

struct RationalNumberFlex {
    RationalNumberFlex(float n, float d, Sign s)
        : numerator{n},
          denominator{d},
          sign{s}
    {}
    float numerator;
    float denominator;
    Sign sign;
};

using RNL = RationalNumberLight;
using RNF = RationalNumberFlex;

class Rational {
    public:
        static RNL Construct(int n, int d=1);
        static RNF Construct(float n, float d=1.0, bool s=false);

        static string StringTerminal(RNL q);
        static string StringLatex(RNL q);

    private:
        static unsigned gcd(unsigned n, unsigned m) { return (m == 0) ? n : gcd(m, n % m); }
        static Sign HandleSign(int n, int d);
        static pair<unsigned, unsigned> ReduceFraction(unsigned n, unsigned d);
};

} // namespace rational
