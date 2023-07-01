#!/usr/bin/python3

from math import isqrt

def get_prime(number):
    """
    get_factors of number

    Args:
        number: number

    Return:
        factors
    """
    flag = 0;
    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            flag += 1
            if flag == 1:
                p = i
            elif flag == 2:
                q = i
                return p, q
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
                factors = get_prime(number)
                if factors:
                    p, q = factors
                    print("{}={}*{}".format(number, p, q))
    except FileNotFoundError:
        print("Error: File {} not found".format(file_path))
    except ValueError:
        print("Error: Invalid number in file {}.".format(file_path))
    except Exception as err:
        print(err)
