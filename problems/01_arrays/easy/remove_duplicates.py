# using set, the orignal order is not preserved
def remove_duplicates(arr):
    return list(set(arr))


# manually using loops
def remove_duplicates_1(arr):
    result = []
    seen = set()   # introduce seen to avoid checking entire arr in each iteration. For cases where arr is very large and consists of many duplicate entries
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# using dict.fromkeys to preserve order - most modern
def remove_duplicates_2(arr):
    return list(dict.fromkeys(arr))


def main():
    arr = [12, 21, 12, 12, 21, 1, 1, 4, 5, 5, 5, 5]
    print(remove_duplicates_1(arr))


if __name__ == "__main__":
    main()