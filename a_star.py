import math
import heapq

#DESCRIPTION
#NOTE: since this algorithm is similair to djiktras with a heuristic approach, the time complexity will be O(nlogn) where n is x*y corresponding
#with grid size we use for testing. But I think we need ot implement a priority queue for this. I think the best case scenario would be 
#O(length of path * average number of direction(may or may not depend on how many "void spaces" or obstacles we add in the maze/grid))
#CODE
class Node:


#this Node needs:
  #parent and position ... for now    /// position is in (x,y) format
# a distance between the current node and the starting node as a value
# heuristic distance from current node to end node: sqrt(a^2 +b^2)
# a value for total cost of everything(the above two put together)
# Similair to Dijsktra's but the value specified above ^ will make it run more efficiently instead of checking every single path


def astar(grid, start, end) # main code 
  openList = [] #
  closedList = []
  directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  startNode = Node(#start)
  #create and initialize all the 3 values here for start node
  endNode = Node(#end)
  #create and initialize all the 3 values here for end node

  openList.append(startNode)
    
  while openList: #Find the end 
    currentNode = openList[0]
    for item in enumerate(openList):
        if item.(total cost) < currentNode.(total cost)
        currentNode = item

    openList.pop(currentNode's index)
    closedList.append(currentNode)

    findgoalorpath() #<- helper function?? maybe
                 #when current = end
                #use temp node
                 # find temp nodes parent and set it to tmep after saving its position in a list or heapq(not sure)
                 #reverse the path to get the right path
    children = []
        for newPosition in directions:
            updatedPosition = (currentNode[0] + newPosition[0], currentNode[1] + newPosition[1])
            #check if out of bounds or reach a "void" space
            nextNode = Node(updatedPosition, currentNode) #currentNode is the parent and updated posiiton is the new direction
            children.append(nextNode) # children will contain every direciton
          
          for child in children:
            # check if in closed list if it is, skip
            #for closed child in closedList, if closedChild == child's posiiton -> skip

            #compute node values
            #distance from starting to current = child value1->currentNodevalue1 + 1
            #distance to end - child value2 -> sqrt[(childposition[0] - endnodeposition[0])^2 + 
            #(childposition[1] - endnodeposition[1])^2]
            # value3(total cost in simple terms) -> child value3 = child value1 + child value2

            # skip if child with lower value3 already in open list(optimize)
            # ^ for openI in openList - : if any(openI.position = child.position and openI -totalcost- < child -totalcost-) then skip
            
            openList.append(child)
                 

def helperfunction1() #add more helper functions as needed

#I don't think we need the sqrt cause I don't see how that would affect end results but safer to try it out wiht this and then maybe remove it
def euclideanDistance(coord1, coord2):
    """sqrt[(x-x2)^2+(y-y2)]"""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

#....
def main()


if __name___ == "main":
  #examples and results

  
#add plots at end maybe
