#!/usr/bin/python3.6

number = 3752

change_type = list(str(number))

print(int(change_type[0]) + int(change_type[1]) + int(change_type[2]) + int(change_type[3])) # стосовно даного завдання не впевнений чи зробив правильно

change_type.reverse()
print(change_type)


change_type.sort()
print(change_type)
