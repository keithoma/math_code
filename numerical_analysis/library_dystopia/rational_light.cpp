
/**
 * 11th October 2020
 * things to do: write handle float
 */

#include <cmath>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

enum class Sign {
    positive,
    negative
};

enum class Mode {
    light,
    flex
};

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

using RNL = RationalNumberLight;

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

int main() {
    RationalNumberLight a = Rational::Construct(15, 3);
    RationalNumberLight b = Rational::Construct(13, -3000);
    cout << Rational::StringTerminal(a) << "\n";
    cout << Rational::StringTerminal(b) << "\n";
    cout << "\n\n";
    cout << Rational::StringLatex(b);
    return 0;
}
