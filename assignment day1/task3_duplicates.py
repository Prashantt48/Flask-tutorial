numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original list:", numbers)

unique_numbers = list(dict.fromkeys(numbers))

print("Updated list:", unique_numbers)