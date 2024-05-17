# Lab #8
# Date: 12/03/2021
# Ryan Talalai



def matrixCalculator(matrix1, matrix2, operation):
    if operation == 'sub':
        return [[x-y for x,y in zip(row1,row2)] for row1,row2 in zip(matrix1,matrix2)]
    elif operation == 'add':
        return [[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(matrix1,matrix2)]
    




def mulDigits(num, fn):
    answer = 1
    while num:
        if fn(num % 10):
            answer *= num % 10
        num //= 10

    return answer




def getCount(x):
    def help(num):               #Helper function for getCount
        count = 0
        num = abs(num)          #Negative numbers become positive
        while num > 0:
            digit = num%10
            if digit == x:
                count += 1
            num //= 10
        return count
    
    
    return help



def itemize(seq):
    count = 0
    for num in seq:
        yield count, num
        count += 1
        


def frange(*args):
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    if step > 0:
        while start < stop:
            yield round(start,3)            #Rounds to 3 decimal places
            start += step
    else:
        while start > stop:
            yield round(start,3)
            start += step



def genFib(fn):
    a = 0
    b = 1

    while True:                 #Indefinite Loop
        if fn(a):
            yield a
        temp_a = a
        temp_b = b
        a = temp_b
        b = temp_a + temp_b
