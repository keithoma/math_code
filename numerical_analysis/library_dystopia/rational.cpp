#include <iostream>
#include <math.h>
#include <string>

using namespace std;

class Rational {
    public:
        Rational(float numerator, float denominator=1.0, int sign=1)
            : numerator_{numerator},
              denominator_{denominator},
              sign_{sign}
        {}

        float numerator() { return numerator_; }
        float denominator() { return denominator_; }
        int sign() { return sign_; }

        Rational reduce_fraction();
        Rational handle_sign();
        Rational handle_float();
        Rational handle_all();

        string string_terminal();
        string string_latex();

    private:
        float numerator_;
        float denominator_;
        int sign_;

        float gcd(float n, float m) { return (m == 0) ? n : gcd(m, fmod(n, m)); }
};

Rational Rational::reduce_fraction() {
    float div = gcd(this->numerator_, this->denominator_);
    numerator_ = int(numerator_ / div);
    denominator_ = int(denominator_ / div);
    return *this;
}

int main() {
    Rational r {3.0, 9.0};
    cout << r.numerator() << "\n";
    cout << r.denominator() << "\n";
    cout << "\n\n";
    cout << r.reduce_fraction().numerator();
    cout << r.denominator();
    cout << "hello!";
    return 0;
}