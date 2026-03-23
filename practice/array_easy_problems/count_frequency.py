def count_frequency(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1
        
        # if i not in freq:
        #     freq[i] = 1
        # else:
        #     freq[i] += 1
    
    return freq


def main():
    arr = [12, 21, 12, 12, 21, 1, 1, 4, 5, 5, 5, 5]
    arr2 = 'banana'
    print(count_frequency(arr))
    print(count_frequency(arr2))


if __name__ == "__main__":
    main()