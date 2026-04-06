def count_gt_avg(arr):
    sum = 0
    for num in arr:
        sum += num
    avg = sum/len(arr)

    count = 0
    for num in arr:
        if num > avg:
            count += 1
    return count



def main():
    arr1 = [3,5,2,4,6,11,0]
    print(count_gt_avg(arr1))


if __name__ == "__main__":
    main()