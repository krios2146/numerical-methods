from util.input import ask_number, ask_comma_separated_list_of_numbers


class Practice5:
    initial_approximation = []
    calculation_accuracy = 0.0001

    def initiate_practice(self):
        print("Enter the initial approximation values separated by comma: ", end="")
        self.initial_approximation = ask_comma_separated_list_of_numbers()

        while not self.is_convergence_condition_satisfied():
            print(
                f"Method convergence condition is not satisfied on this {self.initial_approximation} initial approximation")
            self.initial_approximation = ask_comma_separated_list_of_numbers()

        print("Enter the accuracy: ", end="")
        self.calculation_accuracy = ask_number()

        self.complete_practice()

    def complete_practice(self):
        pass

    def is_convergence_condition_satisfied(self):
        pass
