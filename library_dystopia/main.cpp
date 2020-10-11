/**
 * 11th October 2020
 * things to do: write handle float
 */

#include <rational.hpp>

#include <iostream>

using namespace rational;

using namespace std;

int main() {
    RationalNumberLight a = Rational::Construct(15, 3);
    RationalNumberLight b = Rational::Construct(13, -3000);
    cout << Rational::StringTerminal(a) << "\n";
    cout << Rational::StringTerminal(b) << "\n";
    cout << "\n\n";
    cout << Rational::StringLatex(b);
    return 0;
}
