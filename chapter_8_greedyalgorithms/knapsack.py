def knapsack_rec(max_weight, item_weights, values, num):
    
    if num == 0 or max_weight == 0:
        return 0
        
    if (item_weights[num-1] > max_weight):
        return knapsack_rec(max_weight, item_weights, values, num-1)
    else:
        with_current_element = values[num-1] + knapsack_rec(max_weight-item_weights[num-1], item_weights, values, num-1)
        without_current_element = knapsack_rec(max_weight, item_weights, values, num-1)
        return max(with_current_element, without_current_element)


def knapsack(max_weight, item_weights, values, num):
    
    table = [ [0 for x in range(max_weight+1)] for x in range(num+1) ]
    
    for i in range(num+1):
        for w in range(max_weight+1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif item_weights[i-1] <= w:
                with_current_element = values[i-1] + table[i-1][w - item_weights[i-1]]
                without_current_element = table[i-1][w]
                table[i][w] = max(with_current_element, without_current_element)
            else:
                table[i][w] = table[i-1][w]
                
    return table[num][max_weight]
     

values = [60, 100, 120]
item_weights = [10, 20, 30]
max_weight = 50
num = len(values)
print(knapsack_rec(max_weight, item_weights, values, num))   
print(knapsack(max_weight, item_weights, values, num)) 
