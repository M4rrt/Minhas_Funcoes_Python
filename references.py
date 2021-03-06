import math


# calculates the distance from point 1 to the point 2 
def dist_r(x1,y1,x2,y2):
    distx = x2 - x1
    disty = y2 - y1
    dsquared = distx**2 + disty**2
    result = math.sqrt(dsquared)
    return dsquared

# calculate the hypotenuse of a right triangle
def hipotenusa_r(co,ca):
    c2 = ca**2 + co**2
    return math.sqrt(c2)

# calculate the circule area by the radius of the circle
def area_r(radius):
    a = math.pi * radius**2
    return a


# calculate circle area by the distance between point 1 (circle centre)
# and point 2 (circle perimeter)
def circle_area_r(x1,y1,x2,y2):
    return area_r(dist_r(x1,y1,x2,y2))


# is x devisible by y
def is_divisible_r(x, y):
    return x % y == 0


# is y between x and z ?
def is_between_r(x, y, z):
    return x <= y <= z


# take care is a recursive function maybe 
# this will get a lot of time to be execulted
def factorial_r(n):
    if not isinstance(n, int):
        print('factorial is applicable only with positives int numbers')
        return None
    elif n < 0: 
        print("factorial can't be usade in negative numbers")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_r(n-1)


# take care is a recursive function maybe 
# this will get a lot of time to be execulted
def fibonacci_r(n):
    if n == 0: 
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)


# if u use m > 3 and n > 0 the function will 
# exceeded the maximum recursion
def ack_r(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack_r(m-1,1)
    else:
        return ack_r(m-1,ack_r(m,n-1))


# test if a word is palindrome
def is_palidrome_r(word):
    x = 0
    z = len(word)-1
    for i in range(0,len(word)):
        if word[i] != word[z]:
            return False
            break
        z -= 1
    return True


# test if number a is a power of number b
def is_power_r(a,b):
    if a % b == 0 and a/b % b == 0:
        return True
    else:
        return False

# test the gcd
def gcd_condicion_r(r,a,b):
    for i in range(1,r):
            if (a %i == 0) and (b % i == 0):
                x = i
    return x

# define the condicion to the gcd
def gcd_r(a, b):
    if a >= b: 
        x = gcd_condicion_r(b, a, b)
    else:
         x = gcd_condicion_r(a, a, b)
    return x


# just a countdown...
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print('blastoff!')


# I don't see the really utility by this function but it is in the book...
def while_not_done_r():
    while True:
        line = input('> ')
        if line == 'done':
           break
        print(line)
    print('Done !')


# Newton Square root calculation, calculate the square root of a
def newton_square_r(a):
    x = 1
    while True:
        y = ( x + a / x ) / 2
        if y == x:
            break
        x = y
    return x

# uses eval to let the user make your own expression 
def eval_loop_r():
    while True:
        x = input('>')
        if x == 'done':
            print('shutting down\ndone...\n..\n.')
            break
        elif x != 'done':
            print(eval(x))

            
# make a new string.
# string : is the original string
# new    : new word in the string
# n      : were the 'new' will be put in the string
def restring_r(string, new, n):
    string = new + string[n:]
    return string

# finding a letter in a word
# word   : Original Word
# letter : letter then will be finded
# the function will return an array with the location(s) of the letter in the 'word' or will return -1 if don't find the letter
def find_r(word, letter):
    index = 0
    array = []
    while index < len(word):
        if word[index] == letter:
            array.append(index)
        index += 1
    if array == []:    
        return -1
    else:
        return array

# count the how many times a letter is in an word
# word   : string - the word to be checked  
# letter : char   - the letter to be finded
def count_letter_r(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count+= 1
    return count

# in both  is a function that look at two Strings and see if
# they have same letter inside of then
def in_both_r(word1, word2):
    let = []
    for letter in word1:
        if letter in word2:
            let.append(letter)
    return let

# checks if the 'word' is palindrome
# word : String - the word to be checked  
def is_palindrome_r(word):
    return word == word[::-1]


# checks the the words and see if they have equal letter
# word1 : String - first word
# word2 : String - second word
def in_both_r(word1, word2):  
    let = ''
    for letter in word1:
        if letter in word2:
            let += letter+' '
    return let


# encode a stings with ceasar cipher using a key to rotation between -26 and 26
# word   : String - the word to be enceded
# string : Int    - number between -26 and 26
def caesar_cipher_r(word, n):
    def verification(i,n,vi,vf):
        letter = ''
        if (ord(i)+n) > vf:
                x = (ord(i) + n) - (vf+1)
                letter += chr(vi + x)
        elif(ord(i) + n) < vi :
                x = vi - (ord(i) + n)
                letter += chr(vf+1 - x)
        else:
            letter += chr(ord(i) + n)
        return letter 
    
    letter = ''

    for i in word:
        if i.islower():
            letter += verification(i,n,97,122)

        elif i.isupper():
            letter += verification(i,n,65,90)

        elif i == ' ':
            letter+= ' '

    return letter

# this function uses a file with one word per line and return only the words with n letter in an array
# fin : file.txt - use "fin = open(file.tex)"
# n   : int
def words_len_checker(fin,n):
    wordsn = []
    for i in fin:
        word = i.strip()
        if len(word) >= n:
            wordsn.append(word)
    return wordsn  