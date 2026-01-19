numbers = []
print("Please enter 5 numbers:")
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))  
    numbers.append(num)  
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
print("\n--- Results ---")
print("List of numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest Number:", largest)