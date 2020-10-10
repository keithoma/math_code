
/**
 * 9th October 2020
 * things to do: write handle float, string functions
 */

#include <iostream>
#include <string>
#include <utility>

using namespace std;

enum class Sign {
    positive,
    negative
};

// light version for computing
struct RationalNumberLight {
    RationalNumberLight(unsigned numerator, unsigned denominator, Sign sign)
        : numerator_{numerator},
          denominator_{denominator},
          sign_{sign}
    {}
    const unsigned short numerator_;
    const unsigned short denominator_;
    const Sign sign_;
};

// flexible version
struct RationalNumberFlex {
    RationalNumberFlex(float numerator, float denominator, Sign sign)
        : numerator_{numerator},
          denominator_{denominator},
          sign_{sign}
    {}
    float numerator_;
    float denominator_;
    const Sign sign_;
};

using RNL = RationalNumberLight;
using RNF = RationalNumberFlex;

class Rational {
    public:
        static RNL ConstructLight(float n, float d=1.0);
        // static RNF ConstructFlex(float n, float d=1.0);

        static string StringTerminal(RNL q);
        static string StringLatex(RNL q);

    private:
        unsigned gcd(unsigned n, unsigned m) { return (m == 0) ? n : gcd(m, n % m); }

        Sign HandleSign(float n, float d);
        pair<unsigned, unsigned> HandleFloat(float n, float d);
        pair<unsigned, unsigned> ReduceFraction(unsigned n, unsigned d);
};

RNL constructLight(float n, float d=1.0) {
    const Sign sign = handle_sign(n, d);
    const pair<unsigned, unsigned> num_den = reduce_fraction(static_cast<unsigned> (n),
                                                             static_cast<unsigned> (d));
    return RNL {num_den.first, num_den.second, sign};
}


Sign handle_sign(float n, float d) {
    return (((n > 0) - (n < 0)) * ((d > 0) - (d < 0)) == 1) ? Sign::positive : Sign::negative;
}

pair<unsigned, unsigned> handle_float(float numerator, float denominator) {
    // do later
    // for now, we require the arguments to be whole numbers
}

pair<unsigned, unsigned> reduce_fraction(unsigned numerator, unsigned denominator) {
    const unsigned div = gcd(numerator, denominator);
    return make_pair(numerator / div, denominator / div);
}

int main() {
    RationalNumberLight a = rational(15, 3);
    cout << a.numerator_;
    cout << a.denominator_;
    return 0;
}