def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

while True:
    binary_num = input("Enter a binary number: ")
    if set(binary_num) <= set("01"):
        break
    print("You have not entered a valid binary number.")

print(binary_to_decimal(binary_num))