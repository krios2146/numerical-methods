import math

from util.input import ask_number, ask_comma_separated_list_of_numbers


class Practice2To4:
    root_isolation_boundary = [2, 3]
    calculation_accuracy = 0.0001
    n = 0

    def initiate_practice(self):
        print("Enter the root isolation boundaries separated by comma: ", end="")
        self.root_isolation_boundary = ask_comma_separated_list_of_numbers()

        while not self.is_valid_boundaries(self.root_isolation_boundary):
            print(f"There is no root in {self.root_isolation_boundary} boundaries")
            self.root_isolation_boundary = ask_comma_separated_list_of_numbers()

        print("Enter the accuracy: ", end="")
        self.calculation_accuracy = ask_number()

        print("Enter the n value: ", end="")
        self.n = ask_number()

        self.complete_practice()

    def complete_practice(self):
        root, iterations = self.bisection_method()
        print(f"Approximate solution by the bisection method with {iterations} iterations = {root}")

    def calculate_y_value_at_given_point(self, x):
        return math.log(x) - math.pow(x, 2) + 5

    def bisection_method(self):
        iterations = 0
        root = 0

        start_root_isolation_boundary = self.root_isolation_boundary[0]
        end_root_isolation_boundary = self.root_isolation_boundary[-1]

        a = start_root_isolation_boundary
        b = end_root_isolation_boundary

        while abs(a - b) >= self.calculation_accuracy:
            value_at_a = self.calculate_y_value_at_given_point(a)
            value_at_b = self.calculate_y_value_at_given_point(b)

            middle_point = (a + b) / 2

            value_at_middle_point = self.calculate_y_value_at_given_point(middle_point)

            if value_at_a * value_at_middle_point < 0:
                b = middle_point

            if value_at_b * value_at_middle_point < 0:
                a = middle_point

            iterations += 1
            root = value_at_middle_point

        return root, iterations

    def is_valid_boundaries(self, root_isolation_boundary):
        value_at_start = self.calculate_y_value_at_given_point(root_isolation_boundary[0])
        value_at_end = self.calculate_y_value_at_given_point(root_isolation_boundary[-1])

        return not value_at_start * value_at_end > 0
