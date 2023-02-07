def is_valid_comma_separated_list_of_numbers(input_list):
    try:
        numbers = input_list.split(',')
        numbers_float = [float(num) for num in numbers]
        return True
    except ValueError:
        return False
