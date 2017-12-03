#include <iostream>
#include <cmath>
#include <tuple>
#include <stdexcept>
#include <complex>


std::tuple <double, double> quadratic(double a, double b, double c) {
	double x1;
	double x2;
	x1 = ((-1*b) + std::sqrt(std::pow(b, 2) - (4*a*c)))/(2*a);
	x2 = ((-1*b) - std::sqrt(std::pow(b, 2) - (4*a*c)))/(2*a);
	std::tuple <double, double> solutions = std::make_tuple(x1, x2);
	return solutions;
}



int main() {
	double a;
	double b;
	double c;
	std::cout << "input a then b then c in the form ax^2 + bx + c = 0" << std::endl;
	std::cout << "a: " << std::endl;
	std::cin >> a;
	std::cout << "b: " << std::endl;
	std::cin >> b;
	std::cout << "c: " << std::endl;
	std::cin >> c;
	auto solution = quadratic(a, b, c);
	std::cout << std::get<0>(solution) << std::endl;
	std::cout << std::get<1>(solution) << std::endl;
	return 0;
}