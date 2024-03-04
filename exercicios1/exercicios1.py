A = 11
B = 3

print(A + B * A)
print((B * A) + B)
print(A // B)
print(B % A)
print(A % B)
print(B // A)
print(B - A / B)
print(A / B - A * B)
print(10 + A % B)
print(10 - B // A)
print(B // A - 50)
print(A + B % A - A // B * 2)
print(A * (B + A) - (A - B) / 2)

X = True
Y = False

print(X and Y) #false
print(X or Y) #true
print(X and Y or X) #true
print(X or Y or X) #true
print(not(X or not Y)) #false
print(not (not X and not Y)) #true
print(not X and Y) #false
print(not (X and Y)) #true
print(not X and Y or X) #true
print(not (X and Y) and Y) #false
print(X and Y or Y and not X) #false
print(not (X or Y and Y or Y)) #false
# not (X or (Y and Y) or Y)
# not (X or False or Y)
# not (True or Y)
# not (True)
# // false


A = 5
B = 9
X = not True #false
Y = False and True #false
M = "Casa"
N = "Mesa"

print(X and Y == X or Y) #false
# False and (False == False) or False
# False and False or False
# False or False
# // false

print(A * B <= B - A) #false

print(not (A == B or not B != A)) #true
# not (False or not True)
# not (False or False)
# not (False)
# // true

print(not (M != N and B > A)) #false
# not (True and True)
# not (True)
# // false

print(B + A <= A * B and Y) #false
# 9 + 5 <= 5 + 9 and False
# 14 <= 14 and False
# True and False
# // false

print(X and not Y or A // B != A % B) #true
# False and not False or 0 != 5
# False and not False or True
# False and True or True
# False or True
# // true

