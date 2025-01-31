def pair_numbers(input):
    input = [1, 2, 3, 4, 5, 6]
    for i in input:
        if i % 2 == 0:
            input.remove(i)
    return input
print(pair_numbers(input)) 