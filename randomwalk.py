import random
import copy

""" The random walk algorithm: In a city which its dimension is N X N square, what is the position of start and home(finish) 
squares so that people of the city can return home safely, in the shortest distance matter
"""

"""Approach: for every permutation of squares of the city, test out the random walk. For each combination of start and home 
there will be 50 walkers which record the distance it took to get home. The average distance is recorded of those 50 walkers,
and the distance is saved in a list, which will contain information of the starting position, home position and the average distance
"""

#For each start and home, an object is created to tract the location on the board
class position(object):
    
    
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    #walking function allows the current position of the walker to change its position in x and y coordinates. 
    #however when they hit the wall, they do not move in any direction
    def walkEast(self,val):
        if self.x <self.size-1:
            self.x += val
    
    def walkWest(self,val):
        if self.x >0:
            self.x -= val
    
    def walkNorth(self,val):
        if self.y < self.size-1:
            self.y += val
            
    def walkSouth(self,val):
        if self.y > 0:
            self.y -= val
            
    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)

#this is a class of list which will hold the average walk distance for all the combination of start positions and home positions
#This list was required to return the minimum avg distance while maintaining the relationship between the starting position, 
#home position and the average value.

class allWalk(object):
    alldist = []

    def add(self,lst):
        self.alldist.append(lst)

#returns the list which contains the value of the shortest average distance, and position of 'start' and 'home' 
    def getMin(self):
        shortest = self.alldist[0]
        for i in range(0,len(self.alldist)):
            if self.alldist[i][2] < shortest[2]:
                shortest = self.alldist[i]
        return shortest
#returns the list which contains the value of the longest average distance, and position of 'start'and 'home'
    def getMax(self):
        longest = self.alldist[0]
        for i in range(0,len(self.alldist)):
            if self.alldist[i][2] > longest[2]:
                longest = self.alldist[i]
        return longest



#asking for user to input the dimensions of the city
size = input("enter the size of the board")
size = int(size)

#the random walk function can walk in 4 directions. N,S,W,E. The direction is chosen by random generator. 
#a deep copy of the starting position is required to maintain the original position of the 'start'
#The parameter 'n' refers to the number of walkers per square
def walk(start,home,n):
    #list which will hold value of all the distance the walkers travelled to get home
    people = []
    

    #'n' number of walkers will be walking home
    for i in range(n):
        #a deep copy of starting position. Which is going to change to get to home
        tempStart = copy.deepcopy(start)
        #counter represents the distance, the walker took to arrive home
        counter = 0
        while tempStart != home:
            counter += 1
            step = random.choice(['N','E','S','W'])
            if step == 'N':
                tempStart.walkNorth(1)
            elif step == 'E':
                tempStart.walkEast(1)
            elif step == 'S':
                tempStart.walkSouth(1)
            elif step == 'W':
                tempStart.walkWest(1)
        people.append(counter)

    #the average of of all the walks are returned from the method
    sum = 0
    for e in range(n):
        sum += people[e]
    
    return sum/n

#this is a object which was created to hold tuples of data (starting position, home position, and the average distance)
alldata = allWalk()
#This block creates a permutation possible position of 'start' and 'home'
for a in range(0,size):
    for b in range(0,size):
        for c in range(0,size):
            for d in range(0,size):
                start = position(a,b,size)
                home = position(c,d,size)
                #we do not want the data for when 'start' is already 'home'
                if start != home: 
                    #we are testing each pair of 'start' and 'home' with 50 random walkers
                    lst = [start,home,walk(start,home,50)]
                    print(lst[0],lst[1],lst[2])
                    alldata.add(lst)
#holds the list that contains the position of 'start' and 'home' which has the shortest average distance
shortest = alldata.getMin()
longest = alldata.getMax()

print("With the dimension of the city: " ,size)
print("the shortest average distance between the start and home is: ", shortest[2])
print("where the starting position is: ", shortest[0], "and home is: ", shortest[1])

print("the longest average distance bewteen start and home is  ", longest[2])
print("where the starting position is: ", longest[0]," and home is: ",longest[1])

