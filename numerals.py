#MCS 260 Project Two by <Maria Folvarska>
"""
This program works in 3 parts:
 (1)Dictionary is written to convert from number to Chinese/
    Japanese numeral.
    (a) NUM is a dictionary used to convert regular numbers to
        Chinese/Japanese numerals through Unicode.
 (2)Asks user for value of a Chinese/Japanese numeral.
    (a) Chinese/Japanese numeral is randomly given as a random integer.
    (b) User is prompted to input the value of the Chinese/Japanese numeral.
        (1)If user inputs wrong answer: the correct answer is given and the
           quiz stops,
        (2)If user gives correct answer, the quiz continues.
 (3)Asks user to identity the index position of the randomly
    given Chinese/Japanese numeral.
    (a) A list is created from the values of NUM.
    (b) The list is shuffled and printed.
    (c) The program prompts the user to state the position of
        of a random Chinese/Japanese numeral within the
        shuffled list.
        (1)If user inputs wrong answer, the correct answer is given the
           quiz stops;
        (2)If user inputs correct answer, the program congratulates the
           user. 

"""
from random import randint, shuffle
#create dictionary to access Chinese numerals
NUM = { \
    1 : '\u4e00', 2 : '\u4e8c', 3 : '\u4e09', 4 : '\u56db', \
    5 : '\u4e94', 6 : '\u516d', 7 : '\u4e03', 8 : '\u516b', \
    9 : '\u4e5d', 10 : '\u5341' \
}
#welcome message, first question of quiz and input
print('Welcome to our quiz on Chinese/Japanese numerals.')
x = randint(1, 10)                #random integer
n = NUM[x]
a = int(input('What is the value of ' + str(n) + ' ? '))
#wrong answer: provide correct solution using string concatenation
if a != x:
    print('Wrong answer, ' + str(n) + ' equals ' + str(x) +'.')
#print correct message, move on to next question
else:
    print('Congratulations! Let us continue then, consider: ')
    x = randint(1, 10)             #random integer
    v = NUM.values()               
    L = list(v)                    #creates list from the values of NUM
    shuffle(L)                     #shuffles the list L
    print(L) 
    b = int(input('At which position is the value of ' + str(x) + ' ? '))
    #wrong answer: 
    if L[b] != NUM[x]:
        p = L.index(NUM[x])
        print('Wrong answer, ' + str(NUM[x]) + ' is at position ' + str(p) + '.')
    else:
        print('Congratulations!')    
    


    
        
   
    
