list_number = [1,2,3,4,5,6]

target = 5

def test2(list_number,target):
    total_numbers = len(list_number)
    return_var = []
    for x in range(0,total_numbers):
        for y in range(0,total_numbers):
            if x == y:
                continue
            else:
                if list_number[x] + list_number[y] == target:
                    if list_number[x] < list_number[y]:
                        return_var.append((list_number[x],list_number[y]))
                    else:
                        return_var.append((list_number[y],list_number[x]))
    return list(set(return_var))

print(test2(list_number,target))