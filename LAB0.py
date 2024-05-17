#Lab #0
#Due Date: 08/28/2021, 11:59PM

# More information on pass statement: 
#    https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement

#Ryan Talalai


def sumSquares(aList):
    """
        >>> sumSquares([1,5,-3,5.5,359,8,14,-25,1000])
        129171.25
        >>> sumSquares([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        2187.39
        >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
        390.0
        >>> sumSquares(5)
        >>> sumSquares('5') is None
        True
        >>> sumSquares(6.15)

    """
    # --- YOU CODE STARTS HERE
    if isinstance(aList, list) == True:
        sum_list = []
        total = 0
        for num in range(len(aList)):
            if isinstance(aList[num], (int, float)) == True and aList[num] > 5 and aList[num] < 500:
                result = (aList[num]) ** 2
                sum_list.append(result)

        for num in range(len(sum_list)):
            total = total + sum_list[num]
        return total 
    else:
        return None


## Uncomment next 3 lines if not running doctest in the command line
if __name__ == "__main__":
    import doctest
    doctest.testmod()
