import tkinter

class Canvas:
  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.canvas = None
    self.root = tkinter.Tk()
  
  def start(self):
    self.canvas = tkinter.Canvas(self.root, height = self.height, width = self.width)
    self.canvas.pack()
    
    
  def draw(self, cX, cY, pX, pY):
    self.canvas.create_line(cX, cY, pX, pY, fill="black")