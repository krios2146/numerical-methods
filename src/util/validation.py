def is_valid_comma_separated_list_of_numbers(input_list):
    try:
        numbers = input_list.split(',')
        numbers_float = [float(num) for num in numbers]
        return True
    except ValueError:
        return False


def is_valid_number(input_number):
    try:
        float(input_number)
        return True
    except ValueError:
        return False
