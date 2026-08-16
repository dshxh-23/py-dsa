from problems import solution

# ---- ---- ---- ----


@solution("Largest Element", 1)
def largestElement(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
    
# ---- ---- ---- ----


def main():
    arr = [19, 38, 42, 21, 39, 183, -48]
    print(largestElement(arr))

# -- -- -- --

if __name__ == "__main__":
    main()