# HW1
# Date: 09/10/2021
# Ryan Talalai



def rectangle(perimeter,area):
 
    import math
    length = ((perimeter/2) + math.sqrt(((perimeter**2)/4)-4*area))/2       # derived from quadratic formula
    width = (perimeter/2) - length
    if length.is_integer() == False or width.is_integer() == False:
        return False
    else:
        return int(length)



def frequency(aString):

    d = {}
    aString = aString.lower()
    string_list = list(aString)

    num = 0
    while num < len(string_list):
        if string_list[num].isalpha() == True:
            if string_list[num] in d:
                d[string_list[num]] += 1
            else:
                d[string_list[num]] = 1
        num += 1
    
    value_list = list(d.values())
    key_list = []
    for key in d.keys():
        key_list.append(key)
    
    highest_value = value_list[0]
    list_position = 0
    num = 0
    while num < len(value_list):
        if value_list[num] > highest_value:
            highest_value = value_list[num]
            list_position = num
        num += 1
    
    high_key = key_list[list_position]

    if high_key == 'a' or high_key == 'e' or high_key == 'i' or high_key == 'o' or high_key == 'u':   
        return 'vowel', d
    else:
        return 'consonant', d




def successors(file):

    with open(file) as f: 
        contents = f.read()

    d = {}
    lst = list(contents)
    temp_lst = []
    dict_lst = ['.']
    i = 0
    while i < len(lst):
        if lst[i].isalnum() == True:
            temp_lst.append(lst[i])
            i += 1
            continue
        if lst[i].isalnum() == False and temp_lst != []:   
            string = ''.join(temp_lst)
            dict_lst.append(string)
            temp_lst = []
            if lst[i] == ' ' or lst == ['\n']:
                i += 1
                continue
            else:
                continue
        
        if lst[i].isalnum() == False and lst[i] != ' ':
            dict_lst.append(lst[i])
            i += 1

    lst = [n for n in dict_lst if n not in ['\n']]          #Creates list without new line

    i = 0
    while i < (len(lst) - 1):
        if lst[i] in d:
            d[lst[i]].append(lst[i+1])
            popped_lst = []
            for num in d[lst[i]]:
                if num not in popped_lst:
                    popped_lst.append(num)
            d[lst[i]] = popped_lst
            i += 1
            continue
        else:
            d[lst[i]] = [lst[i+1]]
        i += 1
    return d


def getPosition(num, digit):

    num_2 = num
    digit_count = 0
    while num_2 != 0:
        num_2 = num_2 // 10
        digit_count += 1
    num_length = digit_count
    
    position_count = 1
    while position_count <= num_length:
        if num % 10 == digit:
            return position_count
            break
        else:
            num = num//10
        position_count += 1
    
    if position_count > num_length:
        return False



def hailstone(count):

    lst = []
    lst.append(int(count))
    while count != 1:
        if count % 2 == 0:
            count = count/2
            lst.append(int(count))
        else:
            count = 3*count + 1
            lst.append(int(count))
    return lst


def largeFactor(num):

    if num > 1:
        factors_lst = []
        count = 1
        while count < num:
            if num % count == 0:
                factors_lst.append(count)
            count += 1
        
        highest_value = 1
        count = 0
        while count < len(factors_lst):
            if factors_lst[count] > highest_value:
                highest_value = factors_lst[count]
            count += 1
        
        return highest_value
    else:
        return 'Please enter integer greater than 1'
