class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = profit/weight

def fract_knapsack(items, capacity):
    items = sorted(items, key= lambda x: x.ratio, reverse=True)

    total_profit = 0.0
    remaining = capacity

    for item in items:
        if remaining == 0:
            break

        if item.weight <= remaining:
            print(f"{item.profit}/{item.weight} -> Full")
            total_profit += item.profit
            remaining -= item.weight
            
        else:
            fraction = remaining/item.weight
            print(f"{item.profit}/{item.weight} -> {fraction * 100:.2f}%")
            total_profit += item.profit * fraction
            remaining = 0

    return total_profit

def main():
    items = []

    while True:
        print("\n=== Fractional Knapsack Menu ===")
        print("1. Enter items")
        print("2. Solve fractional knapsack")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            items.clear()
            n = int(input("Enter number of items: "))

            for i in range(n):
                value = float(input(f"Item {i+1} profit: "))
                weight = float(input(f"Item {i+1} weight: "))
                items.append(Item(value, weight))

        elif choice == "2":
            if not items:
                print("Please enter items first!")
                continue

            capacity = float(input("Enter knapsack capacity: "))
            max_value = fract_knapsack(items, capacity)
            print(f"\nMaximum total profit in knapsack: {max_value:.2f}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()