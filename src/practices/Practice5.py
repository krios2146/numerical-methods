from util.input import ask_number, ask_comma_separated_list_of_numbers


class Practice5:
    initial_approximation = []
    calculation_accuracy = 0.0001

    a_1 = [0.23, 0.21, 0.06, -0.34]
    a_2 = [0.05, 1, 0.23, 0.12]
    a_3 = [0.35, -0.27, 1, -0.05]
    a_4 = [0.12, -0.43, 0.34, -0.22]

    b_array = [1.47, -0.57, 0.68, -2.14]

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

        x_roots = self.complete_practice()
        i = 0
        for x in x_roots:
            print(f"x{i} = {x}")
            i += 1

    def complete_practice(self):
        x_j = self.initial_approximation
        while True:
            x_i = self.calculate_x_i_array(x_j)

            if self.is_accuracy_satisfied(x_i, x_j):
                return x_i

            x_j = x_i

    def calculate_x_i_array(self, x_j):
        x_i = []
        i = 0
        for b in self.b_array:
            x_i.append((b - self.calculate_sum_of_coefficients(x_j, i)) / self.get_coefficient(i, i))
            i += 1

        return x_i

    def calculate_sum_of_coefficients(self, x_j, i):
        sum_of_coefficients = 0
        j = 0
        for x in x_j:
            if j != i:
                sum_of_coefficients += self.get_coefficient(i, j) * x
            j += 1

        return sum_of_coefficients

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

    def is_accuracy_satisfied(self, x_i, x_j):
        index = 0
        accuracy_array = []
        while index != len(x_i):
            accuracy_array.append(abs(x_i[index] - x_j[index]))
            index += 1

        accuracy_array.sort()

        if accuracy_array[-1] < self.calculation_accuracy:
            return True

        return False
