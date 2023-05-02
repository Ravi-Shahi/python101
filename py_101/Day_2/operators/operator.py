'''

operators are somthing which can manipulate the value of operands.

68 + 1 = 69

+ -> is operator
68,1 -> is operands
69 -> is result of operation

Different types of operators in python are:
    - Arithmetic Operators
    - Comparison (Relational) Operators
    - Assignment Operators
    - Logical Operators
    - Bitwise Operators
    - Membership Operators
    - Identity Operators

'''

# Arithmetic Operators
'''

+   -> Addition     -> 1 + 68 = 69
-   -> Subtraction  -> 70 - 1 = 69
*   -> Multiplication -> 34.5 * 2 = 69
/   -> Division -> 138/2 = 69
%   -> Modulus -> 69%10 = 9
**  -> Exponent -> 6**2 = 36
//  -> Floor Division -> 9//2 =4

'''
a = 23
b = 2
print('sum: ', a+b)
print('sub: ', a-b)
print('mul: ', a*b)
print('div: ', a/b)
print('rem: ', a%b)
print('exp: ', a**b)
print('floor div: ', a//b)


# Comparision Operators

'''
==  -> Equal  
!=  -> Not equal
>   -> Greater Than
<   -> Less Than
>=  -> Greater than or Equal to
<=  -> Less than or Equal to

note: it return True/False

'''

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# Assignment Operators

'''

=   -> Assignment Operator  -> a = 10
+=  -> Addition Assignment  -> a += 5   (a=a+5)
-=  -> Subtraction Assignment   -> a-=6  (a=a-6)
*=  -> Multiplication Assignment    -> a*=2 (a=a*2) 
/=  -> Division Assignment  -> a/=5 (a=a/5)
%=  -> Remainder Assignment ->  a%=2    (a=a%2)
**= -> Exponent Assignment  => a**=2 (a=a**2)
//= -> Floor Division Assignment    => a//=2    (a=a//2)

'''

print('Listed below result is Assignment operator')
# print('sum: ', a += 1)
# print('sub: ', a -= 5)
# print('mul: ', a *= 2)
# print('div: ', a /= 2)
# print('rem: ', a %= 10)
# print('exp: ', a **=2)
# print('floor div: ', a//=2)


'''
cool Fact: 
    the above print statement will give Syntax ERROR!

Reason: 
    a+=1, a-=5... an so on are assignment statement, print statement always expects an expression/value to print.
'''
#original value of a
print('Orignal', a)
# after assignment operations
a += 1
print(a)
a -= 5
print(a)
a *= 25
print(a)
a /= 2
print(a)
a %= 10
print(a)
a **=2
print(a)
a //= 2
print(a)

#Logical Operators
'''
and -> logical and  -> both condition should be satisfied
or  -> logical or   -> either of the conditions need to be satisfied
not -> logical not  -> retruns false if true, vice-versa

'''
print('Value of "a":',a)
print(a>5 and a<10)
print(a<100 or a>100)
print(not(a==10))

#Bitwise Operators
'''

&   -> Binary AND
|   -> Binary OR
^   -> Binary XOR
~   -> Binary Ones Complement
<<  -> Binary Left Shift
>>  -> Binary Right Shift

Bitwise operator works on bits and performs bit by bit operation.
Please check bit operations to understand this operator,

'''

#Membership Operators
'''
in  -> true if match found
not in  ->  true if not found
This operators test for membership in sequence, such as
    - strings
    - lists
    - tuples

let's take example of Strings, we'll cover lists and tupples later

'''

print("Membership operator: True if present else False ")

user_word = input('Enter your sentence \n')
search_str = input('Enter string to search \n')

print('in operator: ',search_str in user_word)
print('not in operator: ', search_str not in user_word)



#Identity Operator

'''
is      -> if variables are same object, returns TRUE 
is not  -> if variables are not same object, retruns TRUE
'''

i = ['HELLO','GUYS','SUBSCRIBLE','PLEASE']
j = ['HELLO','GUYS','SUBSCRIBLE','PLEASE']
k = j

print('Check i and j are same object: ',i is j)
print('Check j and k are same object: ',j is k)  #memory location ka chakar babu bhyia

print('Check if k and i are not same object: ', k is not i)






