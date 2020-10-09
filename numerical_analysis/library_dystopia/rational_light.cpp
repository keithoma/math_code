#include <iostream>
#include <string>
#include <utility>

using namespace std;

enum class Sign {
    positive,
    negative
};

struct Q {
    Q(unsigned numerator, unsigned denominator, Sign sign)
        : numerator_{numerator},
          denominator_{denominator},
          sign_{sign}
    {}
    const unsigned short numerator_;
    const unsigned short denominator_;
    const Sign sign_;
};

// put these things in a class
// class RationalLight creates the structs Q and handles everything
Sign handle_sign(float n, float d) {
    return (((n > 0) - (n < 0)) * ((d > 0) - (d < 0)) == 1) ? Sign::positive : Sign::negative;
}

pair<unsigned, unsigned> handle_float(float numerator, float denominator) {
    // do later
    // for now, we require the arguments to be whole numbers
}

unsigned gcd(unsigned n, unsigned m) { return (m == 0) ? n : gcd(m, n % m); }

pair<unsigned, unsigned> reduce_fraction(unsigned numerator, unsigned denominator) {
    const unsigned div = gcd(numerator, denominator);
    return make_pair(numerator / div, denominator / div);
}

Q rational(float numerator, float denominator=1.0) {
    const Sign sign = handle_sign(numerator, denominator);
    const pair<unsigned, unsigned> num_den = reduce_fraction(static_cast<unsigned> (numerator),
                                                             static_cast<unsigned> (denominator));
    return Q {num_den.first, num_den.second, sign};
}

int main() {
    Q a = rational(15, 3);
    cout << a.numerator_;
    cout << a.denominator_;
    return 0;
}
