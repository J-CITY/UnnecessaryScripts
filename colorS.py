from colorama import Fore, Back, Style
import os
import colorama
import random


#foreColor = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, 
#	Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
#backColor = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, 
#	Back.MAGENTA, Back.CYAN, Back.WHITE]
foreColor = [30,31,32,33,34,35,36,37]

backColor = [40,41,42,43,44,45,46,47]

def pos(x, y):
	return "\033[%d;%dH" % (y, x)
def printstr(s, colorFG, colorBG, x, y):
	print(pos(x, y) + '\x1b['+Style.NORMAL +";"+str(colorFG) + ";" + str(colorBG)+"m" + s +'\x1b[0m')

one = ["   ",
"   ",
"   ",
"   "]
two = ["###",
"###",
"###",
"###"]

def printCude(str, colorFG, colorBG, x, y):
	for i, s in enumerate(str):
		printstr(s, colorFG, colorBG, x, y+i)

		
os.system('cls')
colorama.init()

def printShemeRect():
	shift = 2
	step = shift + len(one[0]) + 2
	for i, color in enumerate(backColor):
		printCude(one, Fore.WHITE, color, 0+step*i, 1)
		printCude(two, foreColor[i], Back.WHITE, shift+step*i, shift+1)
		
#printShemeRect()

casper = [
"   ###     ",
"  #####    ",
"   # ##  # ",
"# #######  ",
" #######   ",
"   ######  ",
"    #####  ",
"      #### ",
"          #"]

def printShemeRect():
	step = len(casper[0]) + 2
	for i, color in enumerate(backColor):
		for stri, str in enumerate(casper):
			for si, s in enumerate(str):
				if s == '#':
					printstr(' ', Fore.WHITE, color, step*i+si, 1+stri)
				else:
					pass
#printShemeRect()


def print_format_table():

    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()

