def choose_practice():
    print()
    print("Choose the practice to run: ")
    print("(1) - Practice 2-4   : Solving algebraic and transcendental equations by numerical methods")
    print("(2) - Practice 5     : Solving systems of linear equations using approximate methods. Iteration method")
    print("(3) - Practice 6     : Solving systems of linear equations using approximate methods. The Seidel Method")
    print("(4) - Practice 7-8   : Lagrange interpolation formulas. Estimating the error interpolation of a function")
    print("(5) - Practice 9-11  : Calculating the integral of a function using numerical methods")
    print("(6) - Practice 12    : Numerical differentiation of a function given in table form")
    print("(7) - Practice 13-15 : Applying numerical methods to solve differential equations")
    print("(0) - Quit")

    answer = input()
    if answer == "0":
        return None

    while not is_valid_answer(answer):
        print("You should enter number between 0 and 7")
        answer = input()


def is_valid_answer(answer):
    if len(answer) == 1 and answer.isdigit() and 1 <= int(answer) <= 7:
        return True
    else:
        return False


if __name__ == '__main__':
    choose_practice()
