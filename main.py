# Variables & Data Type
name = "Tarik Shah"
age = 25
is_student = True

print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Is Student:", is_student, "| Type:", type(is_student))

print("\n--- Arithmetic Operations ---")
# Arithmetic Operations
print("Age + 5 =", age + 5)
print("Age - 2 =", age - 2)
print("Age * 3 =", age * 3)
print("Age / 2 =", age / 2)

print("\n--- Comparison Operators ---")
# Comparison Operators
print("Is age > 18?", age > 18)
print("Is age == 25?", age == 25)
print("Is age != 30?", age != 30)
print("Is age < 30?", age < 30)

print("\n--- Logical Operators ---")
# Logical Operators
cond1 = age > 18
cond2 = is_student == True

print("cond1 and cond2:", cond1 and cond2)
print("cond1 or cond2:", cond1 or cond2)
print("not cond1:", not cond1)

print("\n--- Assignment Operators ---")
# Assignment Operators
x = 10
print("Initial x:", x)
x += 5
print("After x += 5:", x)
x -= 3
print("After x -= 3:", x)
x *= 2
print("After x *= 2:", x)
x /= 4
print("After x /= 4:", x)

print("\n--- Identity Operators ---")
# Identity Operators
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b:", a is b)
print("c is d:", c is d)
print("c is not d:", c is not d)

print("\n--- Membership Operators ---")
# Membership Operators
my_list = [10,11,20,30]
print("10 in my_list:",10 in my_list)
print("50 not in my_list:", 50 not in my_list)
