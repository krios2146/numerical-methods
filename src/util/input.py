from util.validation import is_valid_number, is_valid_comma_separated_list_of_numbers


def ask_number():
    input_str = input()

    while not is_valid_number(input_str):
        print("Invalid input string. Please enter a number: ", end="")
        input_str = input()

    return float(input_str)


def ask_comma_separated_list_of_numbers():
    xi_input = input()

    while not is_valid_comma_separated_list_of_numbers(xi_input):
        print("Invalid input string. Please enter a comma-separated list of numbers: ", end="")
        xi_input = input()

    return [float(num) for num in xi_input.split(',')]
