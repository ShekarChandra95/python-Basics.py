# python 
print("Hello, myself")

# Arithmetic operation

a = 12
a += 12 # a = a + 12
print(a)
a -= 18 # a = a - 18
print(a)
a /= 4 # a = a / 4
print(a)
a *= 11 # a = a * 11
print(a)
a **= 2 # a = a^2 * 2
print(a)
a //= 2.6
print(a)

#BODMAS principle (Brackets of Division, Multiplication, Addition and Subtraction)
a = 5
b = 7
x = (a+b)*(b-a)
print(x) # x = 24
y = (x/6)*a
print(y) # y = 20
z = (((((((x + y)/11)*y)-y)/a)-x)+y)
print(z) # z = 2


a, b = 15, 19

b, a = a, b # swap the numbers
print(f"a: {a}, b: {b}")

if __name__ == "__main__":
    print("Hellow World")

# Maximum numbers
def my_numbers(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    
print(my_numbers(3, 4, 5, 32, 15, 20, 22, 11,)) # '32' is the Maximum number in this list


