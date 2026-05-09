def fractional_knapsack(weights, values, capacity):
    """
    solve fractional knapsack problem
    """

    items = []
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))
    
    items.sort(reverse=True)

    remaining_capacity = capacity
    total_value = 0

    for ratio, value, weight in items:

        # take entire item if capacity is enough
        if remaining_capacity >= weight:
            remaining_capacity -= weight
            total_value += value

        # if capacity is limited, take fractional item
        elif remaining_capacity != 0:
            total_value += ratio * remaining_capacity
            remaining_capacity = 0      # setting remaining capacity to 0
        
        # prevent unneccessary iterations by breaking the loop when remaining capacity is 0
        else:
            break

    return total_value


def main():
    print(fractional_knapsack([10, 20, 30, 40], [10, 100, 30, 300], 150))
    print(fractional_knapsack([10, 20, 30], [60, 100, 120], 50))
    print(fractional_knapsack([10, 20, 30], [60, 100, 120], 0))
    print(fractional_knapsack([10, 20, 30], [60, 100, 120], 100))
    print(fractional_knapsack([100], [500], 50))
    print(fractional_knapsack([10, 20], [10, 20], 15))
    print(fractional_knapsack([5, 10, 15, 22, 25], [30, 40, 45, 77, 90], 60))
    print(fractional_knapsack([10, 20, 30, 40], [10, 100, 30, 300], 150))


if __name__ == "__main__":
    main()