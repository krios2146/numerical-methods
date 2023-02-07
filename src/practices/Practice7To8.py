import math

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
        return math.log(math.pow(point, (self.pow_numerator / self.pow_denominator)))

    def calculate_absolute_error_at_given_point(self, point):
        polynomial_value = self.calculate_polynomial_at_given_point(point)
        y_value = self.calculate_y_value_at_given_point(point)

        return abs(polynomial_value - y_value)
