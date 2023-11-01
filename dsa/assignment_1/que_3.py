list = [5,7,8,9,7,4,10,11]

sum_of_elements = 0
for i in range(len(list)):
    sum_of_elements += list[i]
    print(f'Index: {i} and current sum is {sum_of_elements}')

average_of_elements = sum_of_elements/len(list)

print("Average of list elements: ", round(average_of_elements,2))