from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "first repeating",
    solution_number = 1,
    approach = "brute force",
)
def first_repeating(arr):
    for i in range(len(arr)):
        for j in range(0, i):
            if(arr[i] == arr[j]):
                return arr[j]
    return None

# -- -- -- --

@solution(
    problem = "first repeating",
    solution_number = 2,
    approach = "storing elements",
)
def first_repeating_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

# ---- ---- ---- ----


def main():
    arr = [5,3,4,3,5,6]
    print(first_repeating_1(arr))
    
# -- -- -- --

if __name__ == "__main__":
    main()
