import math
import heapq
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#DESCRIPTION
#NOTE: since this algorithm is similair to djiktras with a heuristic approach, the time complexity will be O(nlogn) where n is x*y corresponding

#CODE
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        self.g = 0.0
        self.h = 0.0
        self.f = 0.0

    def __lt__(self, other):
        return self.f < other.f




def astar(grid, start, end): # main code 
  openList = [] #
  closedList = []
  directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  startNode = Node(start, None)
 
  endNode = Node(end, None)
  
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
            

def plot_path(grid, path, start, end, elapsed_time): #not part of algo
    plt.figure(figsize=(6, 6))

    rows = len(grid)
    cols = len(grid[0])

    ax = plt.gca()

    #filled squares (white for open, gray for blocked)
    for y in range(rows):
        for x in range(cols):
            color = "gray" if grid[y][x] != 0 else "white"
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor=color, edgecolor="black"))

    # start and end squares
    ax.add_patch(Rectangle((start[0] - 0.5, start[1] - 0.5), 1, 1, facecolor="green", edgecolor="black", label="Start"))
    ax.add_patch(Rectangle((end[0] - 0.5, end[1] - 0.5), 1, 1, facecolor="red", edgecolor="black", label="End"))

    # plot path through cell centers
    if path:
        px = [p[0] + 0 for p in path]
        py = [p[1] + 0 for p in path]
        ax.plot(px, py, color="black", linewidth=2, marker='o', markersize=6, label="Path")

    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(rows - 0.5, -0.5)
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_aspect('equal')
    ax.grid(False)
    ax.legend(loc="upper right")
    ax.set_title(f"A* Pathfinding\nTime: {elapsed_time:.6f} seconds")
    plt.tight_layout()
    plt.show()
    


def calculateH(coord1, coord2):
    """sqrt[(x-x2)^2+(y-y2)]"""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

#....
def main():
    grid = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],  
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],  
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],  
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],  
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0], 
    ]

    start = (0, 9) 
    end   = (9, 0) 

    t0 = time.time()
    path = astar(grid, start, end)
    t1 = time.time()
    elapsed = t1 - t0

    print("Path:", path)
    print(f"Runtime: {elapsed:.6f} seconds")

    plot_path(grid, path, start, end, elapsed)


if __name__ == "__main__":
    #examples and results
    main()

  

