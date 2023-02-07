import math

from util.validation import is_valid_comma_separated_list_of_numbers


class Practice7To8:
    pow_numerator = 0
    pow_denominator = 0
    xi = [0]
    a = 0

    def initiate_practice(self):
        print("Enter the xi values separated by comma: ")
        xi_input = input()

        while not is_valid_comma_separated_list_of_numbers(xi_input):
            print("Invalid input string. Please enter a comma-separated list of numbers: ")
            xi_input = input()

        self.xi = [float(num) for num in xi_input.split(',')]

    def calculate_polynom(self, x, y, x_number):
        polynom = 0

        for xi, yi in zip(x, y):
            numerator = 1
            denominator = 1

            for xj in x:
                if xj != xi:
                    numerator *= (x_number - xj)
                    denominator *= (xi - xj)

            polynomial_coefficient = numerator / denominator
            polynom += polynomial_coefficient * yi

        return polynom

    def calculate_y_value(self, x):
        return math.log(math.pow(x, (self.pow_numerator / self.pow_denominator)))
