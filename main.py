import Employee
from Person import *


def ex01(x: float, y: float, x_power_to_y=None):
    x_power_to_y
    """
    a function that requires 2 numbers and calculates the result of powering the first number to the second
    :param x: The first required number
    :param y: The second required number
    :return: The first number power the second number
    """
    if isinstance(x, float) and isinstance(y, float):
        print("x power y is:" + str (x ** y))
    else:
        print("you need integers")


def ex02 (numbers_dict: dict) -> None:
    """
    a function that requires a dictionary and prints a tuple of two numbers the maximum and the minimum
    :param numbers_dict: The dictionary we need to get the numbers from
    :return: None
    """
    print("Maximum and minimum values of the dictionary is:")
    print((max(numbers_dict.values()), min(numbers_dict.values())))


def ex03(tuples_list: list) -> list:
    """
    a function that requires a list of tuples and finds the two biggest and two smallest values in it
    :param tuples_list: the list of tuples we aim to iterate in order to get the numbers
    :return: a list
    """
    max_list = []
    min_list = []
    for val in tuples_list:
        max_list.append(max(val))
        min_list.append(min(val))
    max_num = max(max_list)
    min_num = min(min_list)
    max_list.remove(max_num)
    min_list.remove(min_num)
    return [max_num, max(max_list)] + "?????????????????????????"


def ex04(list_to_check: list, check_integer_average=None) -> None:
    check_integer_average
    """
    a function that requires a list of numbers checks if the average is a whole number
    :param list_to_check: the list of numbers of aim to check
    :return: None
    """
    print("The average number is a whole number" if isinstance(sum(list_to_check) / len(list_to_check), int)
          else "The average number is NOT a whole number")


def ex05(num: int, print_only_divisible=None):
    print_only_divisible
    """
    a function that requires an integer and prints the numbers that are divisible by that number
    :param num: the number we are checking
    :return: None
    """
    if isinstance(num, int):
        list_divisible_nums = [str(val + 1) for val in range(num + 1) if num % (val + 1) == 0]
        list_to_str = ",".join(list_divisible_nums)
        print(list_to_str if len(list_divisible_nums) > 2 else 1)
    else:
        print("you need an integer")


def ex06 (num, check_palindrom_number=None):
    check_palindrom_number
    """
    a function that requires a number and checks if the number was palindrom
    :param num: the number we are checking
    :return: True if the number was palindrom else False
    """
    if isinstance(num, int):
        str_num = str(num)
        for val in range(len(str_num)):
            if str_num[val] != str_num[-val - 1]:
                return False
        return True
    else:
        print("you need an integer")
    return False


def check_palindrom_number(val):
    pass


def number_of_palindroms_in_list(numbers_list: list):
    """
    a function that requires a list of numbers and check how many palindrom numbers in it
    :param numbers_list: the list we are checking for palindrom numbers
    :return: The amount of palindrom numbers
    """
    count = 0
    for val in numbers_list:
        if check_palindrom_number(val):
            count += 1
    return count


def ex07(num, make_triangles=None):
    make_triangles
    """
    a function that requires an integer and builds a triangle with edges according to the given number
    :param num: the number we are using to build the triangle
    :return: None
    """
    if isinstance(num, int):
        for val in range(num + 1):
            for val2 in range(num - val):
                print(" ", end="")

            for val3 in range(num - val, num):
                print(" *", end="")
            print()
    else:
        print("you need an integer")


def ex08(v1, v2, M, matrix_mul=None):
    matrix_mul
    """
    a funciton that requires two matrixes and a number and multiply the matrixes
    :param v1: vertical matrix
    :param v2: horizontal matrix
    :param M: the length of the matrixes
    :return: returns the multiplication of the matrixes
    """
    if M == len(v1) == len(v2):
        return [v1[0][ind] * v2[ind][0] for ind in range(M)]
    else:
        print("make sure the given values align with the requirements you need two matrixes with the same length and an"
              "integer representing the length of the matrixes")
        return []


def matrix_mul(v1, v2, M):
    pass


def output_matrix_mul(v1, v2, M):
    """
    a function that requires 2 matrixes and an integer representing their length gives us an output of the
    multiplication method of the two matrixes
    :param v1: vertical matrix
    :param v2:horizontal matrix
    :param M: the length of the matrixes
    :return: None
    """
    v3 = matrix_mul(v1, v2, M)
    for i in range(len(v3)):
        print(*(str(v1) + "X" if i == int((M - 1) / 2) else (" " for i2 in range(M + 9))), v2[i],
              *(" " for i3 in range(M)), v3 if i == int((M - 1) / 2) else "")


def main():
    pass


if __name__ == '__main__':
    main()

