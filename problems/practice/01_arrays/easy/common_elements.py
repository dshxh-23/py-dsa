from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "Common Elements", 
    solution_number = 1,
    description = "Pythonic approach using sets and list comprehension.",
)
def intersection(arr1, arr2):
    set2 = set(arr2)    # introduce set cuz searching is O(n) in list, but O(1) in sets 
    result = [num for num in arr1 if num in set2]
    return list(set(result))

# -- -- -- --

@solution(
    "Common Elemnets", 
    2,
    description="Traditional approach which uses conventional loops.",
)
def intersection_2(arr1, arr2):
    result = []
    for num in arr1:
        if num in arr2:
            result.append(num)
    return list(set(result))

# ---- ---- ---- ----


def main():
    arr1 = [1,2,3,4, 39,20,27,27,38]
    arr2 = [3,4,5,38,22,54,27]
    print(intersection_2(arr1, arr2))

# -- -- -- --

if __name__ == "__main__":
    main()