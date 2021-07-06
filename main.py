from random_walk import RandomWalk
from canvas import Canvas
from time import sleep #workaround

if __name__ == "__main__":
  stepNumber = int(input("[Number of random steps]-> "))
  stepSize = int(input("[Size of the randomized step]-> "))
  gridWidth = int(input("[Width of the grid]-> "))
  gridHeight = int(input("[Height of the grid]-> "))
  
  randomWalk = RandomWalk(gridWidth, gridHeight, stepNumber, stepSize)

  print("\n---[CREATING CANVAS]---")
  cv = Canvas(width = randomWalk.gridWidth, height = randomWalk.gridHeight)
  cv.start()

  for i in range(0, randomWalk.stepNumber):
    currentX = randomWalk.posX
    currentY = randomWalk.posY
    randomWalk.walk()
    #print(f'[FROM: {currentX} | {currentY}] [TO: {randomWalk.posX} | {randomWalk.posY}]')

    cv.draw(currentX, currentY, randomWalk.posX, randomWalk.posY)
    cv.root.update()
    sleep(0.015) #workaround

print("\n---[RANDOM WALK DONE]---")