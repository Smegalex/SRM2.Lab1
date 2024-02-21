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


def half_dividing(function: str, variable: str = 'x', accuracy: float = 0.001):
    # functionify(function, accuracy)
    pass


if __name__ == "__main__":
    function = "lg(x + 1) - e^(x) + 0.5 = 0"
    half_dividing(function)
