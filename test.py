operation_dict = dict()

user_input = input("Enter sentence: ")

for char in user_input:
    if char not in operation_dict.keys():
        operation_dict[char] = 1
    else:
        operation_dict[char] += 1

print(operation_dict)
print(operation_dict.keys())
print(operation_dict.values())