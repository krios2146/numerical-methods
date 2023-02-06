class Polynom:
    x = [1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]
    y = [0.888551, 0.889599, 0.890637, 0.891667, 0.892687, 0.893698, 0.894700, 0.895693, 0.896677, 0.897653, 0.898619]

    x_number = 1.427

    def calculate_polynom(self, x, y, x_number):
        polynom = 0

        for xi, yi in zip(x, y):
            numerator = 1
            denominator = 1

            for xj in x:
                if xj != xi:
                    numerator *= (x_number - xj)
                    denominator *= (xi - xj)

            polynomial_coefficient = numerator / denominator
            polynom += polynomial_coefficient * yi

        return polynom
