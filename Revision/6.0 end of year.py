def task1():
    num = int(input('Give me a number between 5 and 30. '))
    if num <=4 or num >=31:
        print('Invalid input')
    else:
        letter = num + 60
        char = chr(letter)
        print(f'{num} is equal to {char}')

def task2():
    import time
    import random
    p1score = 0
    p2score = 0
    
    
    rounds = 0 
    p1 = input('What is your full name? ')
    p1f = p1.find(' ')
    p1fn = p1[0:p1f]
    
    p2 = input('What is your full name?')
    p2f = p2.find(' ')
    p2fn = p2[0:p2f]
    print(f"Players are {p1} and {p2}")
    
    for i in range(0,5):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        p1score = dice1+dice2
        p1txt = print(f'{p1fn} rolls the die... \nThey roll a {dice1} and a {dice2} making their score {p1score}...')
        if p1score % 2 == 0:
            print(f"Score is even...\n+10 points!")
            p1score = p1score+10
            print(p1score)
        elif p1score % 2 != 0:
            print(f"Score is odd...\n-5 points!")
            p1score = p1score-5
            print(p1score)
            if p1score < 0:
                p1score = 0 
                print(p1score)
        elif dice1 == dice2:
            print('A double...\nRoll again')
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            p1score = p1score + dice1+dice2 
            print(p1score)
        print(p1score)

def eoy5():
    product = 0
    checkDigit = 0
    total = 0
    multiplier = 10
    modulus = 0
    isbn = []
    check = ''
    count = 1
    isbn2 = []
    count2 = 0
    isbn3 = 0
    
    print('Type in the digits of your ISBN number')
    for i in range(9):
        check = int(input(f"Digit {count}:  "))
        count+= 1
        isbn.append(check)
    
    
    for n in range(10,1,-1):
        isbn2.append(isbn[count2]*n)
        count2+=1
    isbn3 = sum(isbn2)
    modulus = isbn3%11 
    checkDigit = 11-modulus 
    
    if checkDigit == 11:
        isbn.append(0)
        print(isbn)
    if checkDigit == 10:
        isbn.append('X')
        print(isbn)
    else:
        isbn.append(checkDigit)
        print(checkDigit)
        print(isbn)
eoy5()