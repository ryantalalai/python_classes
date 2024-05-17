# Lab #1
# Ryan Talalai
# Date: 09/03/2021

########################################
# 
# Collaboration Statement: 
#      I referred to:
#       [1] https://docs.python.org/3/tutorial/datastructures.html
#     in order to complete the joinlist function
#       [2] https://www.w3resource.com/python-exercises/python-basic-exercise-86.php
#     in order to complete the isValid function
#
########################################


def joinList(n):
    if n < 1:
        return None
    else:
        lst_1 = []
        for num in range(1,n+1):
            lst_1.append(num)
        lst_2 = lst_1.copy()        #[1]
        lst_2.reverse()             #[1]
        final_lst = lst_1 + lst_2
        return final_lst


def isValid(txt):
    if isinstance(txt, str) == True:
        if len(txt) == 26:
            uppercase = 65           # Represents ASCII for uppercase letters [2]
            lowercase = 97           # Represents ASCII for lowercase letters [2]
            while uppercase < 91 and lowercase < 123:
                if chr(uppercase) in txt or chr(lowercase) in txt:
                    uppercase+=1
                    lowercase+=1
                else:
                    return False
                    break
            if uppercase == 91:      # uppercase will only equal 91 if the entire while loop completes,
                return True          # meaning that every letter of the alphabet is present in the string
        else:
            return False
    else:
        return None
    

def removePunctuation(aString):
    lst1 = list(aString)
    dict = {}
    for char in range(0,len(aString)):
        if lst1[char].isalpha() == False and lst1[char] != ' ':
            if lst1[char] in dict:              # If the non-alphabetic character already has a dictionary key,  
                dict[lst1[char]] += 1           # the dictionary value is updated with one higher
            else:
                dict[lst1[char]] = 1
            lst1[char] = ' '
    new_string = ''
    for item in lst1:
        new_string += item
    return new_string, dict

if __name__ == "__main__":
    import doctest
    doctest.testmod()