from practices.Practice2to4 import Practice2To4
from practices.Practice5 import Practice5
from practices.Practice7To8 import Practice7To8
from practices.Practice9To11 import Practice9To11


def init_app():
    print()
    print("(1) - Practice 2-4   : Solving algebraic and transcendental equations by numerical methods")
    print("(2) - Practice 5     : Solving systems of linear equations using approximate methods. Iteration method")
    print("(3) - Practice 6     : Solving systems of linear equations using approximate methods. The Seidel Method")
    print("(4) - Practice 7-8   : Lagrange interpolation formulas. Estimating the error interpolation of a function")
    print("(5) - Practice 9-11  : Calculating the integral of a function using numerical methods")
    print("(6) - Practice 12    : Numerical differentiation of a function given in table form")
    print("(7) - Practice 13-15 : Applying numerical methods to solve differential equations")
    print("(0) - Quit")
    print("Choose the practice to run: ", end="")

    answer = input()

    while not is_valid_answer(answer):
        print("You should enter number between 0 and 7")
        answer = input()

    if answer == "0":
        return None

    if answer == "1":
        practices_2_to_4 = Practice2To4()
        practices_2_to_4.initiate_practice()

    if answer == "2":
        practices_5 = Practice5()
        practices_5.initiate_practice()

    if answer == "4":
        practices_7_to_8 = Practice7To8()
        practices_7_to_8.initiate_practice()

    if answer == "5":
        practices_9_to_11 = Practice9To11()
        practices_9_to_11.initiate_practice()


def is_valid_answer(answer):
    if len(answer) == 1 and answer.isdigit() and 0 <= int(answer) <= 7:
        return True
    else:
        return False


if __name__ == '__main__':
    init_app()
