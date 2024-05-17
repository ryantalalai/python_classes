# LAB2
# Date: 09/17/2021
# Ryan Talalai

import random

class Vendor:

    def __init__(self, name):
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        return machine._restock(item, amount)
        


class VendingMachine:
    def __init__(self):
        self.dict = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.balance = 0
        



    def purchase(self, item, qty=1):
        self.item = item
        self.qty = qty
        if self.item in self.dict:
            if self.dict == {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}:
                return 'Machine out of stock'
                
            lst = self.dict[self.item]

            if lst[1] == 0:
                return 'Item out of stock'

            if self.qty > lst[1]:
                return f'Current {self.item} stock: {lst[1]}, try again'

            if self.balance < lst[0]*self.qty:
                remaining = lst[0]*self.qty - self.balance
                return f'Please deposit ${remaining}'
            
            if self.balance == lst[0]*self.qty:
                lst[1] -= self.qty
                self.dict[self.item] = lst
                self.balance = 0
                return 'Item dispensed'

            if self.balance > lst[0]*self.qty:
                lst[1] -= self.qty
                self.dict[self.item] = lst
                change = self.balance - lst[0]*qty
                self.balance = 0
                return f'Item dispensed, take your ${change} back'

        else:
            return 'Invalid item'
        
        


    def deposit(self, amount):
        self.amount = amount
        if self.dict == {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}:
            return f'Machine out of stock. Take your ${self.amount} back'
        else:
            self.balance += self.amount
            return f'Balance: ${self.balance}'
        


    def _restock(self, item, stock):
        self.item = item
        self.stock = stock

        if self.item in self.dict:
            lst = self.dict[self.item]
            lst[1] += self.stock
            total_stock = lst[1]
            return f'Current item stock: {total_stock}'

        else:
            return 'Invalid item'


    @property
    def isStocked(self):
        if self.dict == {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}:
            return False
        else:
            return True
        

    @property
    def getStock(self):
        return self.dict


    def cancelTransaction(self):
        if self.balance == 0:
            return None
        else:
            amount = self.balance
            self.balance = 0
            return f'Take your ${amount} back'
       


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        

    @property
    def getDistance(self):
        import math
        ans = math.sqrt((self.point2.x-self.point1.x)**2 + (self.point2.y-self.point1.y)**2)
        distance = round(ans,3)

        return distance


    @property
    def getSlope(self):
        if (self.point2.x-self.point1.x) == 0:
            return float('inf')
        else:
            ans = (self.point2.y-self.point1.y) / (self.point2.x-self.point1.x)
            slope = round(ans,3)
            
            return slope


    def __repr__(self):
        if (self.point2.x-self.point1.x) == 0:
            return 'Undefined'
        else:
            m = (self.point2.y-self.point1.y) / (self.point2.x-self.point1.x)
            b = self.point1.y - (m*self.point1.x)
            m = round(m,3)
            b = round(b,3)
            if m == 0:
                return f'y = {b}'
            else:
                return f'y = {m}x + {b}'

    def __eq__(self, other):
        if type(other) == int:
            return False
        else:
            if self.point1.x == other.point1.x and self.point1.y == other.point1.y and self.point2.x == other.point2.x and self.point2.y == other.point2.y:
                return True
            else:
                return False
    

    
    def __mul__(self, other):
        p1 = Point2D(self.point1.x * other, self.point1.y * other)
        p2 = Point2D(self.point2.x * other, self.point2.y * other)

        return Line(p1, p2)

    def __rmul__(self, other):
        p1 = Point2D(self.point1.x * other, self.point1.y * other)
        p2 = Point2D(self.point2.x * other, self.point2.y * other)

        return Line(p1, p2)
