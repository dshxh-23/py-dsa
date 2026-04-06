def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max
    
def main():
    arr = [19, 38, 42, 21, 39, 183, 48]
    print(find_max(arr))

if __name__ == "__main__":
    main()