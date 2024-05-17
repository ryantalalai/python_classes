# HW3
# Date: 10/16/2021
# Ryan Talalai


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    def __init__(self):
        self.top = None
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}           # Added for helper method
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


    def __len__(self): 
        temp = self.top
        count = 0

        while(temp):
            count += 1
            temp = temp.next
        return count

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

     
    def pop(self):
        if self.isEmpty() == False:
            pop_node = self.top
            self.top = self.top.next
            pop_node.next = None
            return pop_node.value

    def peek(self):
        if self.isEmpty() == False:
            return self.top.value

    def greaterthan(self, operator):                    # Helper Method for Part II
        try:
            a = self.precedence[operator]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False


class Calculator:
    def __init__(self):
        self.__expr = None



    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        try:
            float(txt)
            return True
        except ValueError:
            return False



    def _getPostfix(self, txt):
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        output = []

        lst = txt.split(' ')
        num = 0
        while num < len(lst):
            if self._isNumber(lst[num]):
                lst[num] = float(lst[num])
                lst[num] = str(lst[num])
            num += 1

        i = 0
        while i < len(lst):
            if self._isNumber(lst[i]):
                output.append(lst[i])
                i += 1
             
            elif lst[i]  == '(':
                postfixStack.push(lst[i])
                i += 1
 
            elif lst[i] == ')':
                while not postfixStack.isEmpty() and postfixStack.peek() != '(':
                    output.append(postfixStack.pop())
                if not postfixStack.isEmpty() and postfixStack.peek() != '(':
                    return -1
                else:
                    postfixStack.pop()
                i += 1
                
            else:
                while not postfixStack.isEmpty() and postfixStack.greaterthan(lst[i]):
                    output.append(postfixStack.pop())
                postfixStack.push(lst[i])
                i += 1
 
        while not postfixStack.isEmpty():
            output.append(postfixStack.pop())
 
        
        return ' '.join(output)

        



    @property
    def calculate(self):

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        expr = self.getExpr
        post_fix = self._getPostfix(expr)

        lst = post_fix.split(' ')
        for i in lst:
            try:
                calcStack.push(float(i))
            except ValueError:
                val_1 = calcStack.pop()
                val_2 = calcStack.pop()
                
                operations = {'+':val_2 + val_1, '-':val_2 - val_1, '*':val_2 * val_1, '/':val_2 / val_1, '^':val_2 ** val_1}
                calcStack.push(operations.get(i))

        return float(calcStack.pop())
        




#=============================================== Part III ==============================================

class AdvancedCalculator:
   
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
       
        self.word = word
        lst = list(self.word)
        valid = ''

        i = 0
        while i < len(lst):
            if lst[i].isalnum() == True or lst[i] == '_':
                valid = True
            else:
                valid = False
                break
            i += 1

        if lst[0].isdigit():
            valid = False

        return valid
       

    def _replaceVariables(self, expr):
    
        self.expr = expr
        lst = self.expr.split(' ')
        
        i = 0
        while i < len(lst):
            if self._isVariable(lst[i]) and lst[i] in self.states:
                lst[i] = str(self.states[lst[i]])
            if self._isVariable(lst[i]) and lst[i] not in self.states:
                return None
            i += 1
        
        output = ' '.join(lst)
        return output

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        d = {}
        lst = self.expressions.split(';')
        i = 0
        while i < (len(lst)-1):
            lst2 = lst[i].split(' = ') 
            calcObj.setExpr(lst2[1])
            self.states[lst2[0]] = calcObj.calculate
            d[lst[i]] = self.states
            i += 1
        pos = lst[(len(lst)-1)]
        exp = pos.split('return ')
        calcObj.setExpr(exp[1])
        d['_return_'] = calcObj.calculate