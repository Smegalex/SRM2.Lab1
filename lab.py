import matplotlib.pyplot as plt
import math


math_functions = {'lg': math.log, 'log': math.log, 'e': math.e}

# 25. lg(x + 1) − e^(x) + 0.5 = 0


# def select_brackets(statement: str, start_ind: int, last_ind: int = None):
#     bracket_state = ''
#     if not last_ind:
#         start = None
#         for i in range(start_ind, len(statement)):
#             if statement[i] == ')':
#                 return [bracket_state, start, i]
#             if start != None:
#                 bracket_state += statement[i]
#                 continue
#             if statement[i] == '(':
#                 start = i
#                 continue
#     else:
#         pass


# def fill_other_blanks(full_statement: str, already_parsed: list, parsed_ind: dict):
#     not_checked = list(range(0, len(full_statement)))
#     for filled in list(parsed_ind.keys()):
#         filled = filled.split(":")
#         filled[0] = int(filled[0])
#         filled[1] = int(filled[1])

#         for i in range(filled[0], filled[1]+1):
#             if i == filled[0] :
#                 print(i)
#                 not_checked.insert(not_checked.index(i)+1, 'INSERTION')
#             not_checked.pop(not_checked.index(i))
#     print(not_checked)


# def separate_x(statement: str, variable: str = 'x'):
#     returnable = [""]
#     current_ind = 0
#     for a in statement:
#         if a == variable:
#             if returnable[-1] == "":
#                 returnable[-1] = a
#             else:
#                 returnable.append(a)
#             returnable.append("")
#             current_ind = len(returnable)-1
#             continue
#         returnable[current_ind] += a
#     if returnable[-1] == "":
#         returnable.pop(-1)
#     return returnable


# def functionify(function: str, variable: str = 'x'):
#     function = function.replace(" ", "")
#     parsed_math_functions = []
#     parsed_indexes = {}
#     for key, value in math_functions.items():
#         if key in function:
#             buff_ind = function.index(key) + len(key)
#             in_bracket = select_brackets(function, buff_ind)
#             after_bracket_ind = in_bracket[2]
#             before_bracket_ind = in_bracket[1]

#             in_bracket = in_bracket[0]

#             parsed_indexes[str(buff_ind-len(key)) + ":" +
#                            str(after_bracket_ind)] = str(len(parsed_math_functions))

#             parsed_math_functions.append(value)
#             before_bracket = function[buff_ind:before_bracket_ind]
#             if before_bracket:
#                 parsed_math_functions.append(before_bracket)

#             for part in separate_x(in_bracket):
#                 parsed_math_functions.append(part)

#             parsed_math_functions.append("SEPARATOR")

#             parsed_indexes[str(buff_ind-len(key)) + ":" +
#                            str(after_bracket_ind)] += ":" + str(len(parsed_math_functions)-1)

#             print(parsed_math_functions)
#             print(parsed_indexes)
#     fill_other_blanks(function, parsed_math_functions, parsed_indexes)

def function_calculation(x: float):
    return math.log10(x+1) + math.e ** (x) + 0.5


def first_derivative(x: float):
    return math.e ** x + (1 / (math.log(10) * (x + 1)))


def second_derivative(x: float):
    return math.e ** x - (1 / (math.log(10) * (x ** 2 + 2 * x + 1)))


def fi(x: float):
    return 10 ** (-math.exp(x)-0.5)-1


def dfi(x: float):
    return - math.log(10)*math.exp(x)*10**(-math.exp(x)-0.5)


def graph(x_start: float, x_finish: float, step: float = 1):

    y_results = []

    if step < 1:
        x_range = [
            x*step for x in range(int(x_start/step), int(x_finish/step)+1, 1)]
    else:
        x_range = range(x_start, x_finish+1, step)

    for x in x_range:
        y_results.append(function_calculation(x))
    fig, ax = plt.subplots()
    ax.plot(x_range, y_results)
    plt.show()


def half_dividing(f, left_limit: float, right_limit: float, accuracy: float = 0.001, counter: int = 0):
    middle_limit = (left_limit+right_limit)/2

    middle_value = f(middle_limit)

    if abs(middle_limit-left_limit) <= accuracy:
        return middle_limit, counter

    counter += 1

    if middle_value < 0:
        return half_dividing(f, middle_limit, right_limit, accuracy, counter)

    if middle_value > 0:
        return half_dividing(f, left_limit, middle_limit, accuracy, counter)


def Newton_method(f, df, d2f, left_limit: float = None, right_limit: float = None, x0: float = None, accuracy: float = 0.001, counter: int = 0):
    if left_limit != None and right_limit != None:
        if f(left_limit) * d2f(left_limit) > 0:
            x0 = left_limit
        elif f(right_limit) * d2f(right_limit) > 0:
            x0 = right_limit

    x_next = x0 - (f(x0)/df(x0))

    error = abs(x_next - x0)
    counter += 1
    if error <= accuracy:
        return x_next, counter
    else:
        return Newton_method(f, df, d2f, x0=x_next, accuracy=accuracy, counter=counter)


def hords(f, xk1: float, xk: float, accuracy: float = 0.001):
    x = xk1
    counter = 0
    while abs(xk1-xk) > accuracy:
        # Обчислення значення функції на кінцях відрізка
        fxk1 = f(xk1)
        fxk = f(xk)

        # Обчислення нового наближення за формулою хорд
        x = xk - ((xk - xk1) / (fxk - fxk1)) * fxk

        # Оновлення відрізка виміру
        xk1, xk = xk, x
        counter += 1

    return x, counter


def simple_iteration(fi, dfi, left_limit: float = None, right_limit: float = None, x0: float = None, accuracy: float = 0.001, q: float = None, counter: int = 0):
    if q == None:
        x_range = [
            x*accuracy for x in range(int(left_limit/accuracy), int(right_limit/accuracy), 1)]
        abs_dfi_range = []
        for x in x_range:
            abs_dfi_range.append(abs(dfi(x)))

        q = max(abs_dfi_range)

    if x0 == None:
        x0 = (left_limit+right_limit)/2

    fix = fi(x0)
    error = q/(1-q)*abs(fix-x0)
    counter += 1
    if error <= accuracy:
        return fix, counter
    else:
        return simple_iteration(fi, dfi, x0=fix, accuracy=accuracy, q=q, counter=counter)


if __name__ == "__main__":
    graph(-0.999, -0.75, 0.001)
    left = -0.999
    right = -0.75
    accuracy = 0.001
    print(f"Усі результати нижче надано з точністю до {accuracy}.")

    halfDiv, iterations = half_dividing(function_calculation, left, right, accuracy) 
    print(
        f'Корінь, знайдений методом половинного ділення за {iterations} кроків:\n{halfDiv}')
    
    Newton, iterations = Newton_method(function_calculation, first_derivative, second_derivative, left, right, accuracy=accuracy)
    print(
        f'Корінь, знайдений методом Ньютона за {iterations} кроків:\n{Newton}')

    hords, iterations = hords(function_calculation, right, left, accuracy)
    print(
        f'Корінь, знайдений методом хорд за {iterations} кроків:\n{hords}'
    )

    simplIter, iterations = simple_iteration(fi, dfi, left, right, accuracy=accuracy)
    print(
        f'Корінь, знайдений методом простої ітерації за {iterations} кроків:\n{simplIter}\n'
    )
