import os
import time
import colorama
import random
from colorama import Fore, Back, Style

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

colors = [Fore.CYAN, Fore.GREEN, Fore.RED, Fore.WHITE]

yMax = 25
xMax = 100

class ball:
	def __init__(self):
		self.ch = 'o'
		self.yspeed = random.randint(1, 2)
		self.xspeed = random.randint(1, 3)
		self.x = random.randint(0, 10)
		self.y = random.randint(0, 10)
		self.bounce = 1.1
		self.radius = 2
		self.color = colors[random.randint(0, 3)]
	
	def move(self):
		self.x = self.x + self.xspeed
		self.y = self.y + self.yspeed
		
		if self.x + self.radius/2 < 0:
			self.xspeed = -self.xspeed
		
		if self.x + self.radius/2 > xMax:
			self.xspeed = -self.xspeed
		
		if self.y + self.radius/2 > yMax or self.y + self.radius/2 < 0:
			self.yspeed = -self.yspeed
		
		self.x = round(self.x)
		self.y = round(self.y)
		#self.xspeed = self.xspeed * self.bounce
		#self.xspeed = self.xspeed * self.bounce
	def Print(self):
		print(pos(self.x, self.y) + self.color + self.ch)
	def Clean(self):
		print(pos(self.x, self.y) + self.color + ' ')
		#print(pos(0,0) + self.color + str(self.x)+" "+ str(self.y))

count = 30
def anime():
	balls = []
	for i in range(count):
		balls.append(ball())

	while True:
		time.sleep(0.1)
		for b in balls:
			b.Clean()
			b.move()
			b.Print()

os.system('cls')
colorama.init()
anime()

