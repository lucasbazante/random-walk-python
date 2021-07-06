from random import choice

class RandomWalk:
  def __init__(self, gridWidth, gridHeight, stepNumber, stepSize):
    self.gridWidth = gridWidth
    self.gridHeight = gridHeight

    self.posX = (self.gridWidth // 2)
    self.posY = (self.gridHeight // 2)

    self.stepNumber = stepNumber
    self.stepSize = stepSize

  def walk(self):
    while True:
      nX = choice([-self.stepSize, 0, self.stepSize])
      nY = choice([-self.stepSize, 0, self.stepSize])

      if (self.posX+nX) > self.gridWidth or (self.posX+nX)<0 or (self.posY+nY) > self.gridHeight or (self.posY+nY) < 0:
        continue
      else:
        self.posX += nX
        self.posY += nY
        break