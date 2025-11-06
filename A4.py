def build_knapsack_dp(values, weights, n, capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


def print_dp_table(dp, n, capacity):
    print("     ", end="")
    for w in range(capacity + 1):
        print(f"{w:4}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:3} ", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:4}", end="")
        print()


def main():
    values = []
    weights = []
    n = 0

    while True:
        print("\n=== 0/1 Knapsack Menu ===")
        print("1. Enter items (values & weights)")
        print("2. Solve 0/1 Knapsack")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            values.clear()
            weights.clear()
            n = int(input("Enter number of items: "))

            for i in range(n):
                v = int(input(f"Item {i+1} value: "))
                w = int(input(f"Item {i+1} weight: "))
                values.append(v)
                weights.append(w)

        elif choice == "2":
            if n == 0:
                print("Please enter items first!")
                continue

            capacity = int(input("Enter knapsack capacity: "))
            dp = build_knapsack_dp(values, weights, n, capacity)

            print("\nDP Table:")
            print_dp_table(dp, n, capacity)

            print(f"\nMaximum value that can be put in knapsack: {dp[n][capacity]}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
