arr = []
with open("./inp.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        arr.append(list(map(int, line.split(" "))))

# [lst[:i] + lst[i+1:] for i in range(len(lst))]

example_matrix = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


# all iterations without specific element
def get_variants(lst: list) -> list[list]:
    return [lst[:i] + lst[i + 1 :] for i in range(len(lst))]


example_matrix_lst = example_matrix[0]
print(get_variants(example_matrix_lst))
