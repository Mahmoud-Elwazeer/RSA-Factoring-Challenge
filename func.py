#!/usr/bin/python3

from math import isqrt

def get_factors(number):
    """
    get_factors of number

    Args:
        number: number

    Return:
        factors
    """
    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return i, number // i
    return None

def read_file(file_path):
    """
    read line by line in file

    Args:
        file_path: path of file
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = get_factors(number)
                if factors:
                    p, q = factors
                    print("{}={}*{}".format(number, p, q))
    except FileNotFoundError:
        print("Error: File {} not found".format(file_path))
    except ValueError:
        print("Error: Invalid number in file {}.".format(file_path))
    except Exception as err:
        print(err)
