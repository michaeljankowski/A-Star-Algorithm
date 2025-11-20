import math
import heapq

#DESCRIPTION
#NOTE: since this algorithm is similair to djiktras with a heuristic approach, the time complexity will be O(nlogn) where n is x*y corresponding
#with grid size we use for testing. But I think we need ot implement a priority queue for this. I think the best case scenario would be 
#O(length of path * average number of direction(may or may not depend on how many "void spaces" or obstacles we add in the maze/grid))
#CODE
class Node:
  def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        self.g = 0.0
        self.h = 0.0
        self.f = 0.0

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
  startNode = Node(start, None)
  #create and initialize all the 3 values here for start node
  endNode = Node(end, None)
  #create and initialize all the 3 values here for end node
  startNode.g = 0.0
  startNode.h = calculateH(startNode.position, endNode.position)
  startNode.f = startNode.g + startNode.h

  heapq.heappush(openList, startNode)
    
  while openList: #Find the end 
    currentNode = heapq.heappop(openList)
    closedList.append(currentNode)
    
    if currentNode.position == endNode.position:
            # reconstruct path
            path = []
            temp = currentNode  #use temp node
            #tmep nodes parents -> temp
            while temp is not None:
                path.append(temp.position)
                temp = temp.parent
            #reverse back to start
            return path[::-1]

    children = []
    for newPosition in directions:
      updatedPosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
      rows = len(grid) 
      cols = len(grid[0])
      x, y = updatedPosition
      
      if x < 0 or x >= cols or y < 0 or y >= rows:
                continue  #out of bounds
      if grid[y][x] != 0: #void space
          continue
      
      nextNode = Node(updatedPosition, currentNode)  #parent and direction
      children.append(nextNode) #has every direction

      
      for child in children:
            # check if in closed list if it is, skip
            #for closed child in closedList, if closedChild == child's posiiton -> skip
            if any(closedChild.position == child.position for closedChild in closedList):
                continue
            #compute node values
            #distance from starting to current = child value1->currentNodevalue1 + 1
            child.g = currentNode.g + 1.0
            #distance to end - child value2 -> sqrt[(childposition[0] - endnodeposition[0])^2 + 
            #(childposition[1] - endnodeposition[1])^2]
            child.h = calculateH(child.position, endNode.position)
            # value3(total cost in simple terms) -> child value3 = child value1 + child value2
            child.f = child.g + child.h
            # skip if child with lower value3 already in open list(optimize)
            # ^ for openI in openList - : if any(openI.position = child.position and openI -totalcost- < child -totalcost-) then skip
            skip = False
            for i in openList:
                if i.position == child.position and i.f <= child.f:
                    skip = True
                    break
            if skip:
                continue
              
            heapq.heappush(openList, child)
            

def helperfunction1() #add more helper functions as needed
  pass
#I don't think we need the sqrt cause I don't see how that would affect end results but safer to try it out wiht this and then maybe remove it
def calculateH(coord1, coord2):
    """sqrt[(x-x2)^2+(y-y2)]"""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

#....
def main()
  grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    start = (0, 0)  # (x, y)
    end = (4, 4)

    path = astar(grid, start, end)
    print("Path:", path)


if __name__ == "__main__":
    #examples and results
    main()

  
#add plots at end maybe
