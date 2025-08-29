def cube_even_numbers_for_loop(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result
input_data = [1, 2, 3.5, 4, 'hello', 6, 7, 8.0, 10]

print(cube_even_numbers_for_loop(input_data))   