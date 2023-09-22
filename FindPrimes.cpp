/*finding all the prines between the user supplied lower and upper bound*/

#include <iostream>
#include <vector>
#include <cmath>

using std::cout; using std::cin;  using std::vector; 

int main() {
	int n, N;
	int jmax,fmax;
	bool isPrime;
	int const primeSize = 25;
	int primes[primeSize] = { 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
	vector<int> p;
	

	cout << "Input lower then upper bound: ";
	cin >> n >> N;

	fmax = static_cast<int>(sqrt(N));
	
	for (int i = 0; i < primeSize; ++i) {
		if (primes[i] > fmax) {
			jmax = i;
			break;
		}
	}

	for (int i = n; i <= N; ++i) {
		for (int j = 0; j < jmax; ++j) {
			int f = primes[j];
			if (i % f == 0) {
				isPrime = false;
				break;
			}
			else isPrime = true;
		}
		if (isPrime) p.push_back(i);
	}
	
	for (vector<int>::iterator ip = p.begin(); ip < p.end(); ++ip) {
		cout <<std::endl<< *ip << " ";
	}
}