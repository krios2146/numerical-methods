from util.input import ask_number, ask_comma_separated_list_of_numbers


class Practice5:
    initial_approximation = []
    calculation_accuracy = 0.0001

    a_1 = [0.23, 0.21, 0.06, -0.34]
    a_2 = [0.05, 0, 0.23, 0.12]
    a_3 = [0.35, -0.27, 0, -0.05]
    a_4 = [0.12, -0.43, 0.34, -0.22]

    coefficients = [a_1, a_2, a_3, a_4]

    def initiate_practice(self):
        if self.is_convergence_condition_satisfied():
            print("Convergence condition satisfied, any initial approximation allowed")
        else:
            print("Convergence condition is not satisfied")

        print("Enter the initial approximation values separated by comma: ", end="")
        self.initial_approximation = ask_comma_separated_list_of_numbers()

        print("Enter the accuracy: ", end="")
        self.calculation_accuracy = ask_number()

        self.complete_practice()

    def complete_practice(self):
        pass

    def is_convergence_condition_satisfied(self):
        # Calculate sum of coefficients for each row in matrix
        for i in range(len(self.coefficients)):
            sum_of_coefficients = self.calculate_sum_of_coefficients_of_row(i)
            if sum_of_coefficients >= self.coefficients[i][i]:
                return False
            i += 1

        return True

    def calculate_sum_of_coefficients_of_row(self, i):
        sum_of_coefficients = 0
        for a_i_j in self.coefficients[i]:
            # Exclude a_i_i (diagonal coefficient) from sum
            if a_i_j != self.coefficients[i][i]:
                sum_of_coefficients += abs(a_i_j)
        return sum_of_coefficients

    def get_coefficient(self, i, j):
        # i - row, j - column
        return self.coefficients[i][j]
