text = "Hello World! Python is Fun."

upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
