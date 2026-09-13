# 1. Floor Division
# a = 14
# b = 4
# c = a // b
# print(c)
# addition
a = 5
b = 8
sum = a+b
print(sum)
# subtraction
score_1 = 20
score_2 = 10
final_score = score_1 - score_2
print(final_score)
# multiplication operator
x = 9
y = 2
xy = x*y
print(xy)
# division
x = 8
y = 3
z = (x/y)
print(z)
x = 8
y = 3
z = x//y
print(z)
# exponentiation
x = 10
y = 3
power_result = x ** y
print(power_result)
# modulus operator
a = 35
b = 7
c = a % b
print(c)
# assignment operators
# 1. simple assignment
x = 5
print(x)
name = 'Vishakha'
print(name)
# 2. strict assignment
x = 5
y == x
#  addition and assignment
x = 7
x += 2 
# x = x+2
print(x)
# subtraction and assignment
# x = 9
# x %= 5
# print(x)




# Comparison (Relational) Operators
# equal to (==) or assignment (=) operator is used to compare two values. It returns True if both values are equal, otherwise it returns False.
x = 5
y = 5
print(x == y)  # Output: True

# not equal to (!=) operator is used to compare two values. It returns True if both values are not equal, otherwise it returns False.
a = 'Yess'
b = 'yess'
print(a == b)
print(a != b)  

# greater than (>) operator is used to compare two values. It returns True if the left value is greater than the right value, otherwise it returns False.
a = 17
b = 16
print(a>b)
# less than (<) operator is used to compare two values. It returns True if the left value is less than the right value, otherwise it returns False.
c = 9
d = 10
print(c<d)
# greater than or equal to (>=) operator is used to compare two values. It returns True if the left value is greater than or equal to the right value, otherwise it returns False.
t = 5
v = 5
print(t>=v)
# less than or equal to (<=) operator is used to compare two values. It returns True if the left value is less than or equal to the right value, otherwise it returns False.
e = 3
f = 4
print(e<=f)
x = 4
# x > 5
print(not(x < 5))
d = 561
f = 67
print(not(d>f))

print(5>6 and 7>3)
print(5>6 or 7>3)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)
b = a
c = a
print(a is b, c is  b)
x = 'apple'
print('t' in x)
print('t' not in x)
# 0 or 1
# 2**3 == 8

# 0 or 1 
# 0,1,2,3 : 00, 01, 10, 11 : 2^n : n numbers : 2^0 = 1: 0: 2^1 = 2: 2^2 = 4
# 2^0 = 2*0 = 1
# 2^1 = 2*1 = 2
# 2^2 = 2*2 = 4
# 2^3 = 2*2*2 = 8
# 0 or 1  : 0 -> 0, 1->1, 2  -> 10
# iind(2^1 = 2) ist (2^0 = 1)
#           0*2.  +       0*1 = 0+0 = 0
#            0*2     +    1*1 = 0 + 1 = 1 (01)
#            1*2    +.  0*1 = 2+ 0 = 2(10)
#           1*2  +. 1*1 = 2+ 1 = 3 (11)

# 8 - numbers 0 or 1 form - 3 min 
# iiird(2^2 = 4) iind(2^1 = 2) ist (2^0 = 1)
# 000 = 0
# 001 = 1
# 010 = 2
# 011 = 3
# 100 = 4
# 101 = 5
# 110 = 6
# 111 = 7
# 0 or 1
# 2**4 == 16
# 2^0,2^1,2^2,2^3 = 1, 2, 4,8 || 8 4 2 1 == (1*0 = 0 + 2*0 = 0 + 4*0 = 0 + 8*0 = 0 ) == 0 (0000) || 
# 0000 =0
# 0001 =1 (8 4 2 1) = (2^3* 0 = 0 + 2^2*0 = 0 + 2^1* 0 = 0 + 2^0*1 = 1) == 1 (0001)
# 0010 = 2 = (2^3*0 +2^2*0+2^1*1+ 2^0*0 = 0) == 2 ||(0010)
# 0011 = 3 = (   2^3*0+    2^2*0   +2^1*1  + 2^0*1)==(0+0+2+1)==(3)==(0011)
# 0100 = 4
# 0101 = 5
# 0110 = 6
# 0111 = 7
# 1000 = 8
# 1001 = 9
# 1010 = 10
# 1011 = 11
# 1100 = 12
# 1101 = 13
# 1110 = 14
# 1111 = 15

# & : Bitwise AND
# | : Bitwise OR
# ^ : Bitwise XOR
# ~ :  Bitwise NOT
# << : Zero-fill left shift
# >> : Signed right shift

# Comparison Operators
# == : Equal to
x = 4
y = 6
# print(x == y)  
# != : Not equal to
# print(x != y)
# > : Greater than
# print(x > y)
# < : Less than
# print(x < y)
# >= : Greater than or equal to
# print(x >= y)
# <= : Less than or equal to
# print(x <= y)

# Logical Operators
# and : Logical AND
x = 2
y = 11
# print(x > 3 and y < 10)
# or : Logical OR
# print(x > 3 or y < 10)
# not : Logical NOT
# print(not(x > 3 and y < 10))
# print(not(x>3))
# identity operators
# is : Returns True if both variables are the same object
# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(a is not b) 
# print(a is not c)
# membership operators
# in : Returns True if a sequence with the specified value is present in the object
# x = 'apple'
# print('p' not in x)

# 0 or 1
# 0 or 1
# 00 or 11 or 10 or 01
# 000, 001,010, 011, 100, 101, 110, 111
# 2 ** 4
# 2 ** 3
# generally formula 2**n where n is the number of bits. For example, if we have 4 bits, then the total number of combinations will be 2**4 = 16.

# 0000 ,2^0 = 0, 2^1
# x = 2 (0010) 2^1 = 2
# x =3 (0011)2^1 + 2^0 = 3

# 00 = 0 (2^0, 2^1,2^2,2^3) = 0 + 0 = 0
# 01 = 1 (1) = (2^0 = 1*1 = 1) = 1 + (2^1=2 * 0 = 0) = 1+ 0 = 1
# 10 = (2^0 *0 = 1 *0 = 0) + (2^1 * 1 = 2 *1) 0 + 2 = 2
# 11 = (2^0 *1 = 1 * 1 = 1)+(2^1 *1 = 2* 1 = 2) = 1+ 2 = 3

# a = 7  
# b = 4
# bitwise AND (&)
# print(a & b)
# a = 3 (0011) == (0010) == 2
# b = 6 (0110)
# 0010 :(2^0*0 = 0)+(2^1*1 = 2)+(2^2*0=0)+(2^3*0)=0 = 0+2+0+0 = 2
# 0111
# print(a | b)
# bitwise xor (^) when both bits are different, it returns 1, otherwise it returns 0.
# print(a ^ b)
# 0011 ^ 0110 = 0101 = 5
# bitwise NOT (~) operator inverts the bits of its operand. It changes 1 to 0 and 0 to 1.
# a = 3 (0011)
# ~a = 1100 = -4
# a = 4 
# print(~a)
# logical and : a and b true and false = false bitwise and & 3 and 6 0110  & 0011 = 0010
# bitwise left shift (<<) operator shifts the bits of its operand to the left by a specified number of positions. It fills the rightmost bits with zeros. For example, if we have a number 5 (0101 in binary) and we apply a left shift of 2 positions, we get 20 (10100 in binary).
# print(a >> 2)
# a = 5
# print(a >> 2)
# 5 >> 3 = 5 // 2^3
# 0101 << 2 = 10100
# 5 << 2 = 5* 2^2 = 5*4 = 20
# 5<<3 = 5* 2^3 = 5*8 = 40
# 5>>2 = 5// 2^2 = 5//4 = 1


# BITWISE AND (&)
a = 3
b = 6
print(a & b)
# 3 - 0011(2^0*1 + 2^1*1+ 2^2*0 + 2^3*0) = 3
# 6 - 0110(2^0*0 + 2^1*1 + 2^2*1 + 2^3*0) = 6
# 3&6 = 0010 = 2
# 3|6 = 0111 = 7
# # bitwise OR (|)
print(a | b)
#  bitwise not ~
print(~a)
# # 0011 = 3 = 1100 = -4
# print(~b)
# b = 6 = 0110
# ~b = 1001
# print(~b)
# a = 15
# b = 8
# print(a & b)
# bitwise left shift (<<) operator shifts the bits of its operand to the left by a specified number of positions. It fills the rightmost bits with zeros. For example, if we have a number 5 (0101 in binary) and we apply a left shift of 2 positions, we get 20 (10100 in binary).
a = 5 << 2 = 5* 2**2 = 5*4 = 20
b = 5<<3 = 5* 2**3 = 5*8 = 40
c = 5>>2 = 5// 2**2 = 5//4 = 1
d = 5>>3 = 5//2**3 = 5//8 = 0
# 5 >> n = 5//2**n
# 5<<n = 5* 2**n
# bitwise xor ^
# 1110 ^ 0001 = 1111
# 1^1 = 0
# 0^0 = 0
# 1^0 = 1
# 0^1 = 1
# 1110
# 0001
# 1111