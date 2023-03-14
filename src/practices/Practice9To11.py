import math

import numpy as np
import sympy
from sympy import Symbol, log

from util.input import ask_comma_separated_list_of_numbers, ask_number


class Practice9To11:
    pow_numerator = 0
    pow_denominator = 0
    limits_of_integral = [0]
    n = 0
    newton_leibniz_integral = 0

    def initiate_practice(self):
        print("Enter the numerator of a degree: ", end="")
        self.pow_numerator = ask_number()

        print("Enter the denominator of a degree: ", end="")
        self.pow_denominator = ask_number()

        print("Enter the limits of integral separated by comma: ", end="")
        self.limits_of_integral = ask_comma_separated_list_of_numbers()

        print("Enter the n value: ", end="")
        self.n = ask_number()

        self.complete_practice()

    def complete_practice(self):
        self.newton_leibniz_method()
        print(f"Integral calculated by Newton-Leibniz method      = {self.newton_leibniz_integral}")

        newton_integral = self.newton_cotes_method()
        newton_integral_error = self.calculate_absolute_error(newton_integral)
        print(
            f"Integral calculated by Newton-Cotes method        = {newton_integral} "
            f"with absolute error = {newton_integral_error}")

        rectangle_integral = self.rectangle_method()
        rectangle_integral_error = self.calculate_absolute_error(rectangle_integral)
        print(
            f"Integral calculated by rectangle method           = {rectangle_integral} "
            f"with absolute error = {rectangle_integral_error}")

        trapezoidal_integral = self.trapezoidal_method()
        trapezoidal_integral_error = self.calculate_absolute_error(trapezoidal_integral)
        print(
            f"Integral calculated by trapezoidal method         = {trapezoidal_integral} "
            f"with absolute error = {trapezoidal_integral_error}")

        simpson_integral = self.simpson_method()
        simpson_integral_error = self.calculate_absolute_error(simpson_integral)
        print(
            f"Integral calculated by Simpson method             = {simpson_integral} "
            f"with absolute error = {simpson_integral_error}")

    def newton_leibniz_method(self):
        x = Symbol("x")
        function = log(x) ** (self.pow_numerator / self.pow_denominator)
        antiderivative = sympy.integrate(function, x)
        f_a = antiderivative.evalf(subs={x: self.limits_of_integral[0]})
        f_b = antiderivative.evalf(subs={x: self.limits_of_integral[-1]})
        newton_leibniz_integral = f_b - f_a
        self.newton_leibniz_integral = newton_leibniz_integral.args[0]

    def newton_cotes_method(self):
        x_values = np.linspace(self.limits_of_integral[0], self.limits_of_integral[-1], int(self.n + 1))
        y_values = self.calculate_y_values_at_given_points(x_values)

        integral = 0
        iteration = 0
        for y in y_values:
            cotes_coefficient = self.calculate_cotes_coefficient(iteration)
            integral += cotes_coefficient * y
            iteration += 1

        return integral

    def rectangle_method(self):
        x_values = np.linspace(self.limits_of_integral[0], self.limits_of_integral[-1], int(self.n + 1))
        x_values = np.delete(x_values, -1)
        y_values = self.calculate_y_values_at_given_points(x_values)

        h = x_values[1] - x_values[0]

        integral = 0
        for y in y_values:
            integral += y

        return h * integral

    def trapezoidal_method(self):
        x_values = np.linspace(self.limits_of_integral[0], self.limits_of_integral[-1], int(self.n + 1))
        y_values = self.calculate_y_values_at_given_points(x_values)

        h = x_values[1] - x_values[0]

        integral = 0
        for y in y_values:
            integral += y

            if y != y_values[0] and y != y_values[-1]:
                integral += y

        return (h / 2) * integral

    def simpson_method(self):
        if self.n % 2 != 0:
            return None

        x_values = np.linspace(self.limits_of_integral[0], self.limits_of_integral[-1], int(self.n + 1))
        y_values = self.calculate_y_values_at_given_points(x_values)

        h = x_values[1] - x_values[0]

        integral = 0
        sum_of_even_y_values = 0
        sum_of_odd_y_values = 0
        for y in y_values:
            if y_values.index(y) % 2 == 0 and y != y_values[-1] and y != y_values[0]:
                sum_of_even_y_values += y
            elif y_values.index(y) % 2 != 0:
                sum_of_odd_y_values += y
            else:
                integral += y

        return (h / 3) * (integral + 2 * sum_of_even_y_values + 4 * sum_of_odd_y_values)

    def calculate_absolute_error(self, integral):
        return abs(self.newton_leibniz_integral - integral)

    def calculate_y_values_at_given_points(self, x_points):
        y_values = []

        for x in x_points:
            y_values.append(math.pow(math.log(x), (self.pow_numerator / self.pow_denominator)))

        return y_values

    def calculate_cotes_coefficient(self, iteration):
        a = self.limits_of_integral[0]
        b = self.limits_of_integral[-1]

        c_1_0 = c_1_1 = (b - a) / 2
        n_1 = [c_1_0, c_1_1]

        c_2_0 = c_2_2 = (b - a) / 6
        c_2_1 = (4 * (b - a)) / 6
        n_2 = [c_2_0, c_2_1, c_2_2]

        c_3_0 = c_3_3 = (b - a) / 8
        c_3_1 = c_3_2 = (3 * (b - a)) / 8
        n_3 = [c_3_0, c_3_1, c_3_2, c_3_3]

        c_4_0 = c_4_4 = (7 * (b - a)) / 90
        c_4_1 = c_4_3 = (16 * (b - a)) / 45
        c_4_2 = (2 * (b - a)) / 15
        n_4 = [c_4_0, c_4_1, c_4_2, c_4_3, c_4_4]

        c_5_0 = c_5_5 = (19 * (b - a)) / 288
        c_5_1 = c_5_4 = (25 * (b - a)) / 96
        c_5_2 = c_5_3 = (25 * (b - a)) / 144
        n_5 = [c_5_0, c_5_1, c_5_2, c_5_3, c_5_4, c_5_5]

        c_6_0 = c_6_6 = (41 * (b - a)) / 840
        c_6_1 = c_6_5 = (9 * (b - a)) / 35
        c_6_2 = c_6_4 = (9 * (b - a)) / 280
        c_6_3 = (34 * (b - a)) / 105
        n_6 = [c_6_0, c_6_1, c_6_2, c_6_3, c_6_4, c_6_5, c_6_6]

        ni = [n_1, n_2, n_3, n_4, n_5, n_6]

        return ni[int(self.n - 1)][iteration]
