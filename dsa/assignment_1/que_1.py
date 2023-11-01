unsorted_list = [2,3,65,1,90,23]

for i in range(len(unsorted_list)):
    for j in range(i+1,len(unsorted_list)):
        if unsorted_list[j]<unsorted_list[i]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[j]
            unsorted_list[j] = temp

print(unsorted_list)