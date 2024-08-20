import math
from functools import reduce
import sys

def func_1():
    def generate_squares_traditional(A):
        squares = []
        for x in A:
            squares.append(x ** 2)
        return squares

    def generate_squares_hof(A):
        return list(map(lambda x: x ** 2, A))

    def generate_cubes_traditional(A):
        cubes = []
        for x in A:
            cubes.append(x ** 3)
        return cubes

    def generate_cubes_hof(A):
        return list(map(lambda x: x ** 3, A))

    def squares_in_range_traditional(A):
        result = []
        for x in A:
            square = x ** 2
            if 20 <= square <= 40:
                result.append(square)
        return result

    def squares_in_range_hof(A):
        return list(filter(lambda x: 20 <= x <= 40, map(lambda x: x ** 2, A)))

    def generate_evens_traditional(A):
        evens = []
        for x in A:
            if x % 2 == 0:
                evens.append(x)
        return evens

    def generate_evens_hof(A):
        return list(filter(lambda x: x % 2 == 0, A))
    
    return {
        "generate_squares_traditional": generate_squares_traditional,
        "generate_squares_hof": generate_squares_hof,
        "generate_cubes_traditional": generate_cubes_traditional,
        "generate_cubes_hof": generate_cubes_hof,
        "squares_in_range_traditional": squares_in_range_traditional,
        "squares_in_range_hof": squares_in_range_hof,
        "generate_evens_traditional": generate_evens_traditional,
        "generate_evens_hof": generate_evens_hof
    }

def func_2 ():
    def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return {
        "distance": distance
    }
    
def func_3 ():
    def get_dog_names(animals):
        return list(map(lambda animal: animal['name'], filter(lambda animal: animal['type'] == 'Dog', animals)))
    return {
        "get_dog_names": get_dog_names
    }

def func_4 ():
    def sum_elements(B, direction='left'):
        if direction == 'left':
            return reduce(lambda x, y: x + y, B)
        elif direction == 'right':
            return reduce(lambda x, y: y + x, B)
        else:
            raise ValueError("Direction must be 'left' or 'right'")

    def concatenate_with_Y(B, direction='left'):
        sum_elements_result = sum_elements(B, direction)
        return sum_elements_result + 'Y'
    return {
        "sum_elements": sum_elements,
        "concatenate_with_Y": concatenate_with_Y
    }

def main():
    argument = sys.argv[1]
    if (argument[0] == "1"):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        functions = func_1()
        generate_squares_traditional = functions["generate_squares_traditional"]
        generate_squares_hof = functions["generate_squares_hof"]
        generate_cubes_traditional = functions["generate_cubes_traditional"]
        generate_cubes_hof = functions["generate_cubes_hof"]
        squares_in_range_traditional = functions["squares_in_range_traditional"]
        squares_in_range_hof = functions["squares_in_range_hof"]
        generate_evens_traditional = functions["generate_evens_traditional"]
        generate_evens_hof = functions["generate_evens_hof"]

        if (len(argument) < 2):
            print("a .Squares (Traditional):", generate_squares_traditional(A))
            print("   Squares (Higher-order):", generate_squares_hof(A))
            print("b .Cubes (Traditional):", generate_cubes_traditional(A))
            print("   Cubes (Higher-order):", generate_cubes_hof(A))
            print("c. Squares in range 20-40 (Traditional):", squares_in_range_traditional(A))
            print("   Squares in range 20-40 (Higher-order):", squares_in_range_hof(A))
            print("d. Even numbers (Traditional):", generate_evens_traditional(A))
            print("   Even numbers (Higher-order):", generate_evens_hof(A))

        else:
            if (argument[1] == "a"):
                print("a. Squares (Traditional):", generate_squares_traditional(A))
                print("   Squares (Higher-order):", generate_squares_hof(A))

            if (argument[1] == "b"):
                print("b. Cubes (Traditional):", generate_cubes_traditional(A))
                print("   Cubes (Higher-order):", generate_cubes_hof(A))

            if (argument[1] == "c"):
                print("c. Squares in range 20-40 (Traditional):", squares_in_range_traditional(A))
                print("   Squares in range 20-40 (Higher-order):", squares_in_range_hof(A))

            if (argument[1] == "d"):
                print("d. Even numbers (Traditional):", generate_evens_traditional(A))
                print("   Even numbers (Higher-order):", generate_evens_hof(A))
    
    # Exercise 2
    if (argument == "2"):
        functions = func_2()
        distance = functions["distance"]
        print("Distance between pixels (4, 5) and (3, 2):", distance(4, 5, 3, 2))
    
    # Exercise 3
    if (argument == "3"):
        animals = [
            {'type': 'Dog', 'name': 'Lucy'},
            {'type': 'Cat', 'name': 'Buddy'},
            {'type': 'Rabbit', 'name': 'Jack'},
            {'type': 'Cat', 'name': 'Duke'},
            {'type': 'Rabbit', 'name': 'Sadie'},
            {'type': 'Dog', 'name': 'Bella'}
        ]
        functions = func_3()
        get_dog_names = functions["get_dog_names"]
        print("Dog names:", get_dog_names(animals))
    
    # Exercise 4
    if (argument == "4"):
        B = ['a', 'b', 'c', 'd', 'e']
        functions = func_4()
        sum_elements = functions["sum_elements"]
        concatenate_with_Y = functions["concatenate_with_Y"]
        if (len(argument) < 2):
            print("a. Sum from left to right:", sum_elements(B, 'left'))
            print("b. Sum from right to left:", sum_elements(B, 'right'))
            print("c. Concatenate 'Y' from left to right:", concatenate_with_Y(B, 'left'))
            print("d. Concatenate 'Y' from right to left:", concatenate_with_Y(B, 'right'))
        else:
            if (argument[1] == "a"):
                print("Sum from left to right:", sum_elements(B, 'left'))
            if (argument[1] == "b"):
                print("Sum from right to left:", sum_elements(B, 'right'))
            if (argument[1] == "c"):
                print("Concatenate 'Y' from left to right:", concatenate_with_Y(B, 'left'))
            if (argument[1] == "d"):
                print("Concatenate 'Y' from right to left:", concatenate_with_Y(B, 'right'))


if __name__ == "__main__":
    main()