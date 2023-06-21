def knapsack_greedy(values, weights, capacity):
    n = len(values)
    value_weight_ratio = [(values[i] / weights[i], i) for i in range(n)]
    value_weight_ratio.sort(reverse=True)  # Sort items in descending order of value-to-weight ratio

    max_value = 0
    included_items = []
    current_weight = 0

    for ratio, index in value_weight_ratio:
        if current_weight + weights[index] <= capacity:
            max_value += values[index]
            included_items.append(index)
            current_weight += weights[index]

    return max_value, included_items


# Example usage
values = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367,
          853655, 1826027, 65731, 901489, 577243, 466257, 369261]
weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 
           323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]
capacity = 6404180

max_value, included_items = knapsack_greedy(values, weights, capacity)

solution = [0] * len(values)
for item in included_items:
    solution[item] = 1

quality_percentage = (max_value / sum(values)) * 100

print("Maximum value:", max_value)
print("Optimal solution (0/1 format):", solution)
print("Quality percentage:", quality_percentage, "%")
