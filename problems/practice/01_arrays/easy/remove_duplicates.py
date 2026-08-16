from problems import solution

# ---- ---- ---- ----


@solution(
    "remove duplicates from array", 
    1, 
    description = "pythonic method, side effect of order not preserved"
)
def remove_duplicates(arr):
    return list(set(arr))

# -- -- -- --

@solution(
    "remove duplicates from array",
    2,
    description = "using python's dict.fromkeys() method - most pythonic way that preserves order"
)
def remove_duplicates_3(arr):
    return list(dict.fromkeys(arr))

# -- -- -- --

@solution(
    "remove duplicates from array",
    2,
    description = "pythonic way and also preserves order",
)
def remove_duplicates_3(arr):
    result = []
    seen = set()  
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# ---- ---- ---- ----


def main():
    arr = [12, 21, 12, 12, 21, 1, 1, 4, 5, 5, 5, 5]
    print(remove_duplicates(arr))

# -- -- -- --

if __name__ == "__main__":
    main()