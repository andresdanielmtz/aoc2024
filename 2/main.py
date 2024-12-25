# Day 2, Part 1


arr = []
total = 0


def isListIncreasingOrDecreasing(arr: list) -> bool:
    return all(i < j for i, j in zip(arr, arr[1:])) or all(
        i > j for i, j in zip(arr, arr[1:])
    )


def exceedMaximum(arr) -> bool:
    return any(abs(i - j) > 3 for i, j in zip(arr, arr[1:]))


with open("./inp.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        arr.append(list(map(int, line.split(" "))))

example_matrix = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


for lst in arr:
    if isListIncreasingOrDecreasing(lst) and not exceedMaximum(lst):
        print(lst)
        total += 1
print(total)
