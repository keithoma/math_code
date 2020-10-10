
/**
 * 10th October 2020
 * things to do: write handle float, string functions
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

// here, we could have a heavier but more flexible version of the struct above, the RationalNumberFlex

class Rational {
    public:
        static RNL ConstructLight(int n, int d=1);
        // static RNF ConstructFlex(float n, float d=1.0);

        static string StringTerminal(RNL q);
        static string StringLatex(RNL q);

    private:
        static unsigned gcd(unsigned n, unsigned m) { return (m == 0) ? n : gcd(m, n % m); }
        static Sign HandleSign(int n, int d);
        static pair<unsigned, unsigned> ReduceFraction(unsigned n, unsigned d);
};

RNL Rational::ConstructLight(int n, int d) {
    const Sign sign = HandleSign(n, d);
    const pair<unsigned, unsigned> num_den = ReduceFraction(static_cast<unsigned> (abs(n)),
                                                            static_cast<unsigned> (abs(d)));
    return RNL {num_den.first, num_den.second, sign};
}

string Rational::StringTerminal(RNL q) {
    if (q.sign == Sign::positive) {
        return to_string(q.numerator) + " / " + to_string(q.denominator);
    } else {
        return "-" + to_string(q.numerator) + " / " + to_string(q.denominator);
    }
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
    RationalNumberLight a = Rational::ConstructLight(15, 3);
    RationalNumberLight b = Rational::ConstructLight(13, -3000);
    cout << Rational::StringTerminal(a) << "\n";
    cout << Rational::StringTerminal(b) << "\n";
    cout << "\n\n";
    cout << Rational::StringLatex(b);
    return 0;
}
