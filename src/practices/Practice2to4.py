import math

start_root_isolation_boundary = 2
end_root_isolation_boundary = 3

calculation_accuracy = 0.0001


def calculate_y_value(x):
    return math.log(x) - math.pow(x, 2) + 5


def bisection_method(a, b):
    i = 0
    root = 0

    while abs(a - b) >= calculation_accuracy:
        value_a = calculate_y_value(a)
        value_b = calculate_y_value(b)

        if value_a * value_b > 0:
            return

        m = (a + b) / 2

        value_m = calculate_y_value(m)

        if value_a * value_m < 0:
            b = m

        if value_m * value_b < 0:
            a = m

        i += 1
        root = value_m
        print(root)

    return root
