import colorama
import os
from colorama import Fore, Back, Style
os.system('cls')
colorama.init()


frontColor = [30,31,32,33,34,35,36,37]

backColor = [40,41,42,43,44,45,46,47]

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

def printstr(s, colorFG, colorBG, x, y):
	print(pos(x, y) + '\x1b['+Style.NORMAL +";"+str(colorFG) + ";" + str(colorBG)+"m" + s +'\x1b[0m')

cubic1 = [" ┏━━━━━━━━━┓",
" ┃         ┃",
" ┃    ●    ┃",
" ┃         ┃",
" ┗━━━━━━━━━┛"]
cubic2 = [" ┏━━━━━━━━━┓",
" ┃      ●  ┃",
" ┃         ┃",
" ┃  ●      ┃",
" ┗━━━━━━━━━┛"]
cubic3 = [" ┏━━━━━━━━━┓",
" ┃      ●  ┃",
" ┃    ●    ┃",
" ┃  ●      ┃",
" ┗━━━━━━━━━┛"]
cubic4 = [" ┏━━━━━━━━━┓",
" ┃  ●   ●  ┃",
" ┃         ┃",
" ┃  ●   ●  ┃",
" ┗━━━━━━━━━┛"]
cubic5 = [" ┏━━━━━━━━━┓",
" ┃  ●   ●  ┃",
" ┃    ●    ┃",
" ┃  ●   ●  ┃",
" ┗━━━━━━━━━┛"]
cubic6 = [" ┏━━━━━━━━━┓",
" ┃  ●   ●  ┃",
" ┃  ●   ●  ┃",
" ┃  ●   ●  ┃",
" ┗━━━━━━━━━┛"]

cubics = [cubic1,cubic2,cubic3,cubic4,cubic5,cubic6]

def printCude(str, colorFG, colorBG, x, y):
	for i, s in enumerate(str):
		printstr(s, colorFG, colorBG, x, y+i)
#printCude(cubic5, Fore.GREEN, Back.BLUE, 0, 0)


isFront = True

def printShemeRect():
	step = len(cubic1[0]) + 2
	for i, color in enumerate(frontColor[1:] if isFront else backColor[1:]):
		if i >= len(cubics):
			return
		for stri, str in enumerate(cubics[i]):
			for si, s in enumerate(str):
				printstr(s, color, Back.BLACK, step*i+si, 1+stri)
				
printShemeRect()

