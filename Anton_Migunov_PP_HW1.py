class Operation:

    def __init__(self, l_operand: float, r_operand: float, sign: str):
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.sign = sign
        self.priority = 0

    def __repr__(self):
        return f"{self.l_operand} {self.sign} {self.r_operand} ({self.priority})"

    def prioritize(self):
        if self.sign in ("+", "-"):
            self.priority = 1
        elif self.sign in ("*", "/"):
            self.priority = 2
        elif self.sign == "^":
            self.priority = 3

    def calculate(self):
        if self.sign == "+":
            return self.l_operand + self.r_operand
        if self.sign == "-":
            return self.l_operand - self.r_operand
        if self.sign == "*":
            return self.l_operand * self.r_operand
        if self.sign == "/":
            return self.l_operand / self.r_operand
        if self.sign == "^":
            if not (self.l_operand < 0 and (1 / self.r_operand) % 2 == 0):
                return self.l_operand ** self.r_operand
            else:
                raise ValueError("Result of this operation is a complex number - unallowed result.")


class Equation:

    CONST = {" ": "",
             ",": ".",
             "**": "^",
             "e": "2.71",
             "pi": "3.14",
             "epi": "2.71",
             "pie": "3.14"}

    def __init__(self, equation_string: str):
        self.equation_string = equation_string

    def __repr__(self):
        return self.equation_string

    def standardize(self):
        for const, repl in self.CONST.items():
            self.equation_string = self.equation_string.replace(const, repl)
        print(self.equation_string)

    def validate(self):
        """
        - starts with digit or (
        - ends with digit or )
        - brackets must be closed correctly
        - no unallowed symbols must be present
        - negative numbers must be written in brackets, for example - (-1) - no complex numbers
        """
        allowed_symbols = "0123456789+-*/()^."
        brackets_stack = []

        for i in range(len(self.equation_string)):
            symbol = self.equation_string[i]

            if (i == 0 and symbol not in "0123456789(") \
                    or (i == len(self.equation_string)-1 and symbol not in "0123456789)"):
                raise ValueError(f"Incorrect string start/end - {symbol}.")

            elif symbol not in allowed_symbols:
                raise ValueError(f"Unallowed symbol has been found - {symbol}, {i}.")

            elif symbol == "(":
                brackets_stack.append(i)
            elif symbol == ")":
                if brackets_stack == []:
                    raise ValueError("Unbalanced brackets.")
                brackets_stack.pop(-1)

            elif 0 < i < len(self.equation_string)-1:
                if all((symbol in "+-*/^",
                        self.equation_string[i-1] not in "0123456789)",
                        self.equation_string[i+1] not in "0123456789(")):
                    raise ValueError(f"String has unallowed pattern - "
                                     f"{self.equation_string[i-1], symbol, self.equation_string[i+1]}")

        if brackets_stack != []:
            raise ValueError("Unbalanced brackets.")

    def decompose_plain_string(self):
        decomposed_string = []
        cursor = 0
        for i in range(len(self.equation_string)):
            symbol = self.equation_string[i]
            if symbol == "-" and i == 0:
                continue
            if symbol in ("+", "-", "*", "/", "^"):
                decomposed_string.append(self.equation_string[cursor:i])
                decomposed_string.append(symbol)
                cursor = i + 1
        decomposed_string.append(self.equation_string[cursor:len(self.equation_string)])

        return decomposed_string

    @staticmethod
    def group_string_elements(decomposed_string):
        operations = []
        if len(decomposed_string) == 1:
            return [Operation(float(decomposed_string[0]), 0, "+")]
        for e in range(1, len(decomposed_string) - 1, 2):
            operation = Operation(float(decomposed_string[e - 1]), float(decomposed_string[e + 1]),
                                  decomposed_string[e])
            operation.prioritize()
            operations.append(operation)
        print(operations)
        return operations

    def calculate_plain_string(self):
        # example 22+2*2.7
        operations = self.group_string_elements(self.decompose_plain_string())
        result_operation = operations[0]

        if len(operations) != 1:
            for o in range(1, len(operations)):
                if result_operation.priority >= operations[o].priority:
                    operations[o].l_operand = result_operation.calculate()
                    result_operation = operations[o]
                else:
                    result_operation.r_operand = operations[o].calculate()

        return result_operation.calculate()

    def calculate_complex_string(self):
        # example 25+((-2)*17)/(2.7^4)
        element_start_indexes = []
        result_string = self.equation_string[::]

        for i in range(len(self.equation_string)):
            symbol = self.equation_string[i]
            if symbol == "(":
                element_start_indexes.append(i)
            elif symbol == ")":
                element = Equation(self.equation_string[element_start_indexes[-1]+1:i])
                element_start_indexes.pop(-1)

                subequation = f"({element.equation_string})"
                result = str(element.calculate_plain_string())
                reduced_equation = Equation(result_string.replace(subequation, result))

                return reduced_equation.calculate_complex_string()

        return Equation(result_string).calculate_plain_string()


def main(eq_str: str):
    """    operations: + - * / **
    numbers: int, float
    special symbols: ()
    consts: e, pi

    - starts with digit, const, or (
    - ends with digit, const or )
    - brackets must be closed correctly
    - no unallowed symbols must be present
    - no division by zero
    - no roots with odd base from negative numbers
    - negative numbers must be written in brackets, for example - (-1) - no complex numbers

    EXAMPLE: (-5) + (2 + 2 * 2) - (e ** (pi ** 0.5)) / 22
    """
    equation = Equation(eq_str)

    equation.standardize()
    try:
        equation.validate()
    except ValueError as err:
        print(err)
        return None

    try:
        result = equation.calculate_complex_string()
    except ValueError as err:
        print(err)
        return None
    except ZeroDivisionError as err:
        print(err)
        return None

    return float(result)


if __name__ == "__main__":
    # Correct behavior
    assert main("(-5) + (2 + 2 * 2) - (e ** (pi ** 0.5)) / 22") == 0.7340494717285055
    # Division by zero
    assert main("1/0") is None
    # Complex number
    assert main("(-1)**0.5") is None
    # Incorrect string - unbalanced brackets
    assert main("(2+(2*2)") is None
    # Incorrect string - unallowed symbols
    assert main("2+f$2") is None
    # Incorrect string - unbalanced string
    assert main("+2*2") is None
    assert main("2+2*") is None
    assert main("(+2+2)") is None

print(main.__doc__)
user_input = input("Enter your equation here: ")
print(f"Result - {main(user_input)}")
