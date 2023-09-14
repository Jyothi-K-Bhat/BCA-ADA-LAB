def knapsack_greedy(values, weights, capacity):
    # Calculate the value-to-weight ratio for each item
    value_per_weight = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]

    # Sort items by value-to-weight ratio in descending order
    value_per_weight.sort(reverse=True)

    total_value = 0  # Total value of items selected
    knapsack = []    # List to store the selected items

    for ratio, value, weight in value_per_weight:
        if capacity == 0:
            break  # Knapsack is full

        if weight <= capacity:
            # Add the entire item to the knapsack
            total_value += value
            capacity -= weight
            knapsack.append((value, weight))
        else:
            # Add a fraction of the item to the knapsack
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((fraction * value, fraction * weight))
            break

    return total_value, knapsack

# Example usage
n=int(input("Enter the number of items:"))
values = []
weights = []
for i in range(n):
    values.append(int(input(f"Enter the value of item{i+1}")))
    weights.append(int(input(f"Enter the weight of item{i+1}")))
capacity = int(input("ENter the total capacity:"))

max_value, selected_items = knapsack_greedy(values, weights, capacity)

print("Maximum value:", max_value)
print("Selected items:")
for item in selected_items:
    print("Value:", item[0], "Weight:", item[1])