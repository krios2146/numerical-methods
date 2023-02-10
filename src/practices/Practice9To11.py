import math

import numpy as np

from util.input import ask_comma_separated_list_of_numbers, ask_number


class Practice9To11:
    pow_numerator = 0
    pow_denominator = 0
    root_isolation_boundary = [0]
    root = 0
    n = 0

    def initiate_practice(self):
        print("Enter the numerator of a degree: ", end="")
        self.pow_numerator = ask_number()

        print("Enter the denominator of a degree: ", end="")
        self.pow_denominator = ask_number()

        print("Enter the root isolation boundaries separated by comma: ", end="")
        self.root_isolation_boundary = ask_comma_separated_list_of_numbers()

        print("Enter the n value: ", end="")
        self.n = ask_number()

        self.complete_practice()

    def complete_practice(self):
        self.newton_cotes_method()

    def newton_cotes_method(self):
        xi = np.linspace(self.root_isolation_boundary[0], self.root_isolation_boundary[-1], int(self.n + 1))

        yi = []
        for xi in xi:
            yi.append(self.calculate_y_value_at_given_point(xi))

        print(xi)
        print(yi)

    def calculate_y_value_at_given_point(self, point):
        return math.pow(math.log(point), (self.pow_numerator / self.pow_denominator))

    def calculate_cotes_coefficient(self, a, b, iteration):
        c_1_0, c_1_1 = (b - a) / 2
        n_1 = [c_1_0, c_1_1]

        c_2_0, c_2_2 = (b - a) / 6
        c_2_1 = (4 * (b - a)) / 6
        n_2 = [c_2_0, c_2_1, c_2_2]

        c_3_0, c_3_3 = (b - a) / 8
        c_3_1, c_3_2 = (3 * (b - a)) / 8
        n_3 = [c_3_0, c_3_1, c_3_2, c_3_3]

        c_4_0, c_4_4 = (7 * (b - a)) / 90
        c_4_1, c_4_3 = (16 * (b - a)) / 45
        c_4_2 = (2 * (b - a)) / 15
        n_4 = [c_4_0, c_4_1, c_4_2, c_4_3, c_4_4]

        c_5_0, c_5_5 = (19 * (b - a)) / 288
        c_5_1, c_5_4 = (25 * (b - a)) / 96
        c_5_2, c_5_3 = (25 * (b - a)) / 144
        n_5 = [c_5_0, c_5_1, c_5_2, c_5_3, c_5_4, c_5_5]

        c_6_0, c_6_6 = (41 * (b - a)) / 840
        c_6_1, c_6_5 = (9 * (b - a)) / 35
        c_6_2, c_6_4 = (9 * (b - a)) / 280
        c_6_3 = (34 * (b - a)) / 105
        n_6 = [c_6_0, c_6_1, c_6_2, c_6_3, c_6_4, c_6_5, c_6_6]

        ni = [n_1, n_2, n_3, n_4, n_5, n_6]

        return ni[self.n][iteration]
