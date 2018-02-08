"""
import wx
#from wx.lib.pubsub import setupkwargs #I need this to force pubsub to work. I don't know why.
#from wx.lib.pubsub import pub

ID_MYBUTTON = wx.NewId()

class App1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init___(self, parent)

        button = wx.Button(self, ID_MYBUTTON, "Show App2")
        self.Bind(wx.EVT_BUTTON, self.handleButton, id=ID_MYBUTTON

    def handleButton(self, event):
        pubsub.sendMessage("mybutton.pressed") #send the message

class App2(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent)

        self.Hide() #I don't want to be seen yet

        pubsub.subscribe(self.gotMessage, "mybutton.pressed") #listen for the message

    def gotMessage(self):
        self.Show() #Now I want to be seen!
"""

"""
#operands
def adding(x, y):
    return x + y

print(adding(2,4))

def operations(x, y, z):
    return x + y * z

print(operations(2,3,4))
"""

"""
#strings formatting
#[1]
programmingLanguage = "Python"
print("{} is a great programming language".format(programmingLanguage))

#[2]
text = "sample text"
text.upper()
text.lower()

#[3]
text = "sample text"
print(text.replace("sample", "some"))

#[4]
text = "sample text"
print(text[0:6])
"""

"""
#[5] lists
list = []

list.append("item1")
list.insert(2, "item2") #2 - która pozycja na liscie
list.remove("item1")
list.sort() #sortuje i zmienia liste
sorted(list) #zwraca posortowaną listę ale jej nie zmienia
list.reverse() #sortuje liste w odwrotnym kierunku
list.pop() #usuwa ostatni element z listy i go zwraca
print(list)


#tupla
tuple1 = (1914, 1939)
print(tuple1(1))
del tuple1
"""

"""
#Dictionary
dictionaryName = {"key1": "value1", "key2": "value2"}
dictionaryName["key2"] = 100
print(dictionaryName)

#dictionary keys
print(dictionaryName.keys())
#dictionary values
print(dictionaryName.values())
# dictionary copy - copies one dictionary into another
dictionary_copy = dictionaryName.copy()
#deleting element of the dictionary (by key)
del dictionary_copy["key1"]
#cleaning the dictionary
dictionaryName.clear()


newDict = {1:"el1",2:"el2", 3:"el3", 4:"el4", 5:"el5"}
newDict[1] = 1000
newDict2 = newDict.copy()
"""

"""
programmingLanguage = "Python"
test = "test"
print("{} is a great programming {} language".format(programmingLanguage, test))
"""

"""
#condition
def multiple():
    a = int(input("Podaj liczbę: "))
    if ((a % 3 == 0) and (a % 7 == 0)):
        print("wielokrotność 3 i 7")
    elif (a % 3 == 0 and a % 7 != 0):
        print("Wielokrotność 3")
    elif (a % 7 == 0 and a % 3 != 0):
        print("Wielokrotność 7")
    else:
        print("ani 3 ani 7")
multiple()
"""

"""
#looping statements - loops: for, while
number = 1
for i in range(3):
    for column in range(3):
        print(number, end = " ")
        number += 1
    print()

def findBook():
    collectionOfBooks = ["aaa", "bbb", "ccc"]
    bookToCheck = input("podaj nazwe ksiazki: ")

    for book in collectionOfBooks:
        if book == bookToCheck:
            print("ksiazka istnieje w zbiorze")
            break
    else:
        print("ksiazka nie istnieje w zbiorze")
findBook()
"""

"""
#Eceptions
try:
    length = 10
    width = 0
    length / width
except Exception:
    print("Divisiona by zero is invalid, change your input")

try:
    width = 0
    length / width
except NameError:
    print("vaariable has been used before being defined")
except ZeroDivisionError:
    print("Divisiona by zero is invalid, change your input")
"""




#PROGRAM NA ZAKONCZENIE
"""
totalMarks = {"student1": 500, "student2": 500, "student3": 400, "student4": 100, "student5": 300, "student6": 300}
dict = {}

for key, value in totalMarks.items():
    dict[value] = [key] if value not in dict else dict[value] + [key]
#print(dict)
"""

def find_max(dictionary):
        max = -(float('inf'))
        for key in dictionary.keys():
            if key > max:
                max = key
        return max

    #for key, value in dict.items():

def rankStudents(dict):
    try:
        print("\n" + "Top 3 students ranks: ")
        pomDict = {}
        for i in range(0,3):
            max = find_max(dict)
            pomDict[max] = dict[max]
            print(str(dict[max]))
            del dict[max]
        return pomDict
    except KeyError:
        print("Enter minimum 3 students")
        quit()

def rewardStudents(dict, rewards):
    try:
        print("\n" + "Rewards for students are:")
        """
        entriesToAdd = len(dict) - 3
        if entriesToAdd == 2:
            dict[1] = -1; dict[2] = -1
        if entriesToAdd == 1:
            dict[2] = -1
        """
        pomDict = dict.copy()
        for i in range(0, len(pomDict)):
            max = find_max(pomDict)
            print(str(pomDict[max])+ ": " + rewards[i])
            del pomDict[max]          

    except NoneType:
        print("Error occured")
        quit()

#class incorrectStudentsNumberException:
#    print("Numher of students must be >= 3")
#    quit()

def readStudentDetails():
    try:
        numberOfStudents = int(input("Enter a number of students in class: "))
        if (numberOfStudents < 3):
            raise RuntimeError('Number of students must be >=3')

        i = 1
        dict = {}
        while i <= numberOfStudents:
            pom = "student" + str(i)
            GPA = int(input("Enter GPA(int value) for {}: ".format(pom)))
            dict[pom] = GPA
            i += 1

        pomDict = {}
        for key, value in dict.items():
            pomDict[value] = [key] if value not in pomDict else pomDict[value] + [key]

        return pomDict
    except ValueError:
        print("Number of students must be an integer number")
        quit()
    except RuntimeError as error:
        print(error)
        quit()


def appreciateStudents(dict, val):
    print("\n" + "Appreciate:")
    for key, value in dict.items():
        if key > val:
            print("Appreciate  {} : {} GPA".format(value, key))

studentRecord = readStudentDetails()
#print(dict2)

# rank students
rewardedStudents = rankStudents(studentRecord)

#reward students
rewards = ("$500", "$300", "$100")
rewardStudents(rewardedStudents, rewards)

#Appreciate students with GPA > 200
#print(rewardedStudents)
appreciateStudents(rewardedStudents, 200)







#Dictionary
# nie można posortować słownika wg kluczy - ponieważ słownik jest z definicji - unordered
# rozwiązaniem jest przekonwertowanie słownika na listę tupli, przykład:
"""
import operator
#[('Mark': 980), ('David': 200), ...]
#key = operator.itemgetter(1) - oznacza, że sortujemy po 2wartości czyli liczbach
sortedDictionary =  sorted(sortedDictionary.items(), key = operator.itemgetter(1), reverse = False)

  #odwołujjemy się do tego - przykład -> słownik = ('Maciek': 100, 'Tomek':200) 
 sortedDictionary [0][0] #Maciek
 sortedDictionary [0][1] #100
 sortedDictionary [1][0] #Tomek
 sortedDictionary [1][1] #200
"""






































