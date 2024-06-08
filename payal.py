def add_numbers(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    elif num1 < 0 and num2 < 0:
        return num1 + num2
    else:
        return "The numbers have different signs"
      number1 = 5
number2 = -3
print("Sum:", add_numbers(number1, number2))