/**
 * 10th of July 2020
 */

#include <iostream>

using namespace std;

unsigned long long int factorial(unsigned long long int n) {
    // even unsigned long long int is too small for factorial
    return (n==1 || n==0) ? 1: n * factorial(n - 1);  
}

int binominal_coefficient(int n, int k) {
    return factorial(n) / (factorial(n - k) * factorial(k));
}

class Hypergeometric {
    public:
        Hypergeometric(int N_, int K_, int n_) {
            N = N_;
            K = K_;
            n = n_;
        };

        float pmf(int k) {
            return (float)(binominal_coefficient(N - K, n - k) * binominal_coefficient(K, k)) / 
                   (float)(binominal_coefficient(N, n));
        };

        int get_N() { return N; };
        int get_K() { return K; };
        int get_n() { return n; };

    private:
        int N; // population size
        int K; // number of success in the population
        int n; // number of draws
};

int main() {
    // check: https://www.wolframalpha.com/input/?i=hypergeometric+distribution+3%2C+3%2C+10
    Hypergeometric distribution(10, 3, 3);
    cout << distribution.pmf(3) << "\n";

    return 0;
}