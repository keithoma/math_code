#include <iostream>
#include <string>
#include <utility>

using namespace std;

enum class Sign {
    positive,
    negative
};

class RationalLight {
    public:
        RationalLight(float numerator, float denominator=1.0, Sign sign=Sign::positive);

        unsigned short numerator() { return numerator_; }
        unsigned short denominator() { return denominator_; }
        Sign sign() { return sign_; }

        string string_terminal();
        string string_latex();

    private:
        // max value for unsigned short is 65535 = 2^16 - 1
        const unsigned short numerator_;
        const unsigned short denominator_;
        const Sign sign_;

        unsigned gcd(unsigned n, unsigned m) { return (m == 0) ? n : gcd(m, n % m); }

        Sign handle_sign(float n, float d, Sign s);
        pair<unsigned, unsigned> handle_float(float numerator, float denomin);
        pair<unsigned, unsigned> reduce_fraction(unsigned numerator, unsigned denominator);
};

Sign RationalLight::handle_sign(float n, float d, Sign s) {
    return (((n > 0) - (n < 0)) * ((d > 0) - (d < 0)) * ((s == Sign::positive) - (s == Sign::negative)) == 1)
    ? Sign::positive : Sign::negative;
}

pair<unsigned, unsigned> RationalLight::handle_float(float numerator, float denominator) {

}

pair<unsigned, unsigned> RationalLight::reduce_fraction(unsigned numerator, unsigned denominator) {
    const unsigned div = gcd(numerator, denominator);
    return make_pair(numerator / div, denominator / div);
}

int main() {
    return 0;
}