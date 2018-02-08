#Lesson 3 - blogging: www.wordpress.com
# Lesson 4 - jupiter notebook + anaconda - python packages management system
"""
tmp = [ex for ex in range(0,10)]
print tmp

tmp.append(1000)
print tmp

ex2 = tmp.pop()
print ex2
"""

#hash tables

"""obiektowość - przykład 
class Animal(Object):
    def __init__(self, attribute_value):
        self.attribute1 = attribute_value
        self.attribute1 = attribute_value

    def method1 (parameters):
        #Animal could do this action
        return outcome

class Dog(Animal):
    def __init__(self, attribute_value):
        Animal.__init__(self, attribute_value)
        self.attribute3 = default_value

    def method1 (parameters):
        #ADog could do this action
        return outcome
"""


"""
#[1] Fizz buz
def fizzbuzz():
    tmp = [ex for ex in range(0,100)]

    for val in tmp:
        if val % 3 == 0:
            tmp[val] = "Fizz"
        if val % 5 == 0:
            tmp[val] = "Buzz"
        if (val % 3 == 0) and (val % 5 == 0):
            tmp[val] = "FizzBuzz"
    print(tmp)
fizzbuzz()
"""


"""
# [2] adding binary numbers - binary calculator
def parse_binary_string(st):
    sum = 0
    for i in range(len(st)):
        if st[i] == "1":
            sum += 2**i
            #print(sum)
    return sum

def binary_multiply(st1, st2):
    tmp_st1 = parse_binary_string(st1)
    tmp_st2 = parse_binary_string(st2)
    multiply = tmp_st1 * tmp_st2
    print (bin(multiply))

binary_multiply("11", "1")
"""

# [3] adding numbers - liked list NOT DONE
#https://www.youtube.com/watch?v=Ast5sKQXxEU
#https://www.youtube.com/watch?v=j0-YASYqOFw

"""
# [4] finding anagrams
class Solution:
 def find_anagrams(strs):
    dict = {}
    for word in strs:
        #sorotwanie stringów: list.sort() sorts the list and save the sorted list, while sorted(list) returns a sorted list without changing the original list
        sortedword = ''.join(sorted(word))
        #dodawanie klucza do słownika - rezultat w przypadku anagramu: 1. ['anagram'] = ['anagram'] 2. ['anagram', 'nagaram'] = ['nagaram']
        dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
    anagrams = []
    for item in dict:
        if len(dict[item]) >= 2:
            anagrams  += dict[item]
    return anagrams

print(Solution.find_anagrams(["anagram", "nagaram", "racecar", "carraces", "test", "estt"]))
"""

# [5] buy and sell stock
#list[i] - price the first day
#list[i+1] - price the second day
"""
class Solution:
    def profit(list):
        profit = 0
        minPrice = list[0]
        for i in range(len(list)-1):
            if minPrice > list[i]:
                minPrice = list[i]
            if profit < list[i] - minPrice:
            #if list[i+1] > list[i]:
                profit = (list[i] - minPrice)
                #print(profit)
        return profit


print ( Solution.profit([7, 1, 5, 3, 6, 4]) ) 
print ( Solution.profit([7, 6, 4, 3, 1]) ) 
print(Solution.profit([2,3,6,3,7,5])) 
"""

"""
class Solution:
    def profit(list):
        index = 0
        minVal = float('inf')
        for i in range(len(list)-1):
            if list[i] < minVal:
                minVal = list[i]
                index = i

        k = index
        maxPrice = list[k]

        while (k < (len(list)-1)):
            if list[k] >= maxPrice:
                maxPrice = list[k]
            k += 1

        maxProfit = maxPrice-minVal
        return maxProfit

print (Solution.profit([7, 1, 5, 3, 6, 4]))
print (Solution.profit([7, 6, 4, 3, 1]))
print(Solution.profit([2,3,6,3,7,5]))
"""


"""
class Solution:
 def maxProfit(prices):
    #unbounded upper value for comparison - +infinity
    minValue = float("inf")
    maxBenefit = 0
    for price in prices:
        if minValue > price:
            minValue = price
        if maxBenefit < price - minValue:
            maxBenefit = price - minValue
    return maxBenefit

#print ( Solution.maxProfit([7, 1, 5, 3, 6, 4]) ) #5
#print ( Solution.maxProfit([7, 6, 4, 3, 1]) ) #0
print ( Solution.maxProfit([2,3,6,3,7,5])) #5
"""


# [6] buy and sell stock - NOT DONE
"""
prices = [1,2,3,0,2]
size = len(prices)
buys = [None] * size
print(buys)
print(prices[-1])
"""

"""
# [7] binary tree pre-order traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            return result


class Solution2:
    def inorderTraversal(root):
        stack = []
        node = root
        solution = []
        while node != None or len(stack) > 0:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                solution.append(node.val)
                node = node.right
        return solution


if __name__ == '__main__':
    BT, BT.right, BT.right.left = TreeNode(1), TreeNode(2), TreeNode(3)
    print ( Solution.preorderTraversal(BT) )
    print ( Solution2.inorderTraversal(BT) )
"""


