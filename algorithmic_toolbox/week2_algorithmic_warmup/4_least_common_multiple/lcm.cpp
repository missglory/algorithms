#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

int gcd(int a, int b) { 
  // std::cout << a << " " << b << "\n";
  return b == 0 ? a : gcd(b, a % b);}
unsigned long long lcm(int a,int b) { return ((unsigned long long)a) / gcd(a,b) * b; }

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
