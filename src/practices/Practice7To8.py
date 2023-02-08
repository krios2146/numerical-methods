import math

from sympy import Symbol, diff, log

from util.input import *


class Practice7To8:
    pow_numerator = 0
    pow_denominator = 0
    x = [0]
    a = 0

    def initiate_practice(self):
        print("Enter the numerator of a degree: ")
        self.pow_numerator = ask_number()

        print("Enter the denominator of a degree: ")
        self.pow_denominator = ask_number()

        print("Enter the x values separated by comma: ")
        self.x = ask_comma_separated_list_of_numbers()

        # TODO: a should be in range of interpolation
        print("Enter the a value: ")
        self.a = ask_number()

        self.complete_practice()

    def complete_practice(self):
        polynomial_value = self.calculate_polynomial_at_given_point(self.a)
        print(f"Value of f(x) at the {self.a} calculated using Lagrange polynomial = {polynomial_value}")

        absolute_error = self.calculate_absolute_error_at_given_point(self.a)
        print(f"Absolute error at the {self.a} = {absolute_error}")

        upper_bound = self.calculate_upper_bound()
        print(f"Upper bound = {upper_bound}")

    def calculate_polynomial_at_given_point(self, point):
        polynomial = 0

        for xi in self.x:
            polynomial_coefficient = 1
            for xj in self.x:
                if xj != xi:
                    polynomial_coefficient *= (point - xj) / (xi - xj)

            polynomial += polynomial_coefficient * self.calculate_y_value_at_given_point(xi)

        return polynomial

    def calculate_y_value_at_given_point(self, point):
        return math.pow(math.log(point), (self.pow_numerator / self.pow_denominator))

    def calculate_absolute_error_at_given_point(self, point):
        polynomial_value = self.calculate_polynomial_at_given_point(point)
        y_value = self.calculate_y_value_at_given_point(point)

        return abs(polynomial_value - y_value)

    def calculate_upper_bound(self):
        x = Symbol("x")
        function = log(x) ** (self.pow_numerator / self.pow_denominator)
        derivative = diff(function, x, len(self.x))

        max_value = 0
        term = 1
        for xi in self.x:
            derivative_value = abs(derivative.evalf(subs={x: xi}))

            if derivative_value > max_value:
                max_value = derivative_value

            term *= (self.a - xi)

        factorial = math.factorial(len(self.x))

        upper_bound = (max_value / factorial) * abs(term)

        return upper_bound
