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

        print("Enter the a value: ")
        self.a = ask_number()

        self.complete_practice()

    def calculate_polynomial_at_given_point(self, a):
        polynomial = 0

        for xi in self.x:
            polynomial_coefficient = 1
            for xj in self.x:
                if xj != xi:
                    polynomial_coefficient *= (a - xj) / (xi - xj)

            polynomial += polynomial_coefficient * self.calculate_y_value(xi)

        return polynomial

    def calculate_y_value(self, x):
        return math.log(math.pow(x, (self.pow_numerator / self.pow_denominator)))

    def complete_practice(self):
        polynomial_value_at_point = self.calculate_polynomial_at_given_point(self.a)
        print(f"Value of f(x) at the {self.a} calculated using Lagrange polynomial = {polynomial_value_at_point}")
