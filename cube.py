import colorama
import os
from colorama import Fore, Back, Style
import platform
import argparse

OS = platform.system()
if OS == "Windows":
	os.system('cls')
else:
	os.system('clear')
colorama.init()


#frontColor = [30,31,32,33,34,35,36,37]
#backColor = [40,41,42,43,44,45,46,47]
frontColor = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, 
	Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
backColor = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, 
	Back.MAGENTA, Back.CYAN, Back.WHITE]

mapColorFg = dict()
mapColorFg[0] = Fore.BLACK
mapColorFg[1] = Fore.RED
mapColorFg[2] = Fore.GREEN
mapColorFg[3] = Fore.YELLOW
mapColorFg[4] = Fore.BLUE
mapColorFg[5] = Fore.MAGENTA
mapColorFg[6] = Fore.CYAN
mapColorFg[7] = Fore.WHITE

mapColorBg = dict()
mapColorBg[0] = Fore.BLACK
mapColorBg[1] = Fore.RED
mapColorBg[2] = Fore.GREEN
mapColorBg[3] = Fore.YELLOW
mapColorBg[4] = Fore.BLUE
mapColorBg[5] = Fore.MAGENTA
mapColorBg[6] = Fore.CYAN
mapColorBg[7] = Fore.WHITE

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

#def printstr(s, colorFG, colorBG, x, y):
#	format = ';'.join([str(22), str(colorFG), str(colorBG)])
#	s1 = '\x1b[%sm%s\x1b[0m' % (format, s)
#	print(pos(x, y) + s1)

def printstr(s, colorFG, colorBG, x, y):
	print(pos(x, y) + colorFG + colorBG + s)

cubic1 = ["┏━━━━━━━━━┓",
"┃         ┃",
"┃    ●    ┃",
"┃         ┃",
"┗━━━━━━━━━┛"]
cubic2 = ["┏━━━━━━━━━┓",
"┃      ●  ┃",
"┃         ┃",
"┃  ●      ┃",
"┗━━━━━━━━━┛"]
cubic3 = ["┏━━━━━━━━━┓",
"┃      ●  ┃",
"┃    ●    ┃",
"┃  ●      ┃",
"┗━━━━━━━━━┛"]
cubic4 = ["┏━━━━━━━━━┓",
"┃  ●   ●  ┃",
"┃         ┃",
"┃  ●   ●  ┃",
"┗━━━━━━━━━┛"]
cubic5 = ["┏━━━━━━━━━┓",
"┃  ●   ●  ┃",
"┃    ●    ┃",
"┃  ●   ●  ┃",
"┗━━━━━━━━━┛"]
cubic6 = ["┏━━━━━━━━━┓",
"┃  ●   ●  ┃",
"┃  ●   ●  ┃",
"┃  ●   ●  ┃",
"┗━━━━━━━━━┛"]

cubics = [cubic1,cubic2,cubic3,cubic4,cubic5,cubic6]

def printCude(str, colorFG, colorBG, x, y):
	for i, s in enumerate(str):
		printstr(s, colorFG, colorBG, x, y+i)

#printCude(cubic5, Fore.RED, Back.CYAN, 0, 1)


isFront = True

bgColor = Back.BLACK
fgColor = Fore.WHITE
cube = None

def printShemeRect(fg, bg):
	step = len(cubic1[0]) + 2
	for i, color in enumerate(frontColor[1:] if isFront else backColor[1:]):
		if i >= len(cubics):
			return
		for stri, str in enumerate(cubics[i]):
			if isFront:
				printstr(str, color, bgColor, step*i, 1 + stri)
			else:
				printstr(str, fgColor, color, step*i, 1 + stri)

#printShemeRect(bgColor, fgColor)
#printstr("INFO", Fore.RED, Back.CYAN, 0, 2)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="Cube color script", description='Print cube to console.')
	parser.add_argument('-fg', type=int, help="Foreground color 0-7 [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]")
	parser.add_argument('-bg', type=int, help="Background color 0-7 [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]")
	parser.add_argument('-cube', type=int, help="Cube 1-6")
	parser.add_argument('-isFront', action="store_true", help="Change bg color or fg")
	parser.set_defaults(isFront=False)

	args = parser.parse_args()

	if args.fg is not None and args.fg >= 0 and args.fg <= 7:
		fgColor = mapColorFg[args.fg]

	if args.bg is not None and args.bg >= 0 and args.bg <= 7:
		bgColor = mapColorBg[args.bg]

	if args.cube is not None and args.cube >= 1 and args.cube <= 6:
		cube = args.cube

	if cube is not None:
		printCude(cubic5, fgColor, bgColor, 0, 1)
	else:
		printShemeRect(bgColor, fgColor)
