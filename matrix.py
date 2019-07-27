from colorama import Fore, Back, Style
import os
import colorama
import random
import time
import shlex
import struct
import platform
import subprocess
 
 
def get_terminal_size():
	current_os = platform.system()
	tuple_xy = None
	if current_os == 'Windows':
		tuple_xy = _get_terminal_size_windows()
		if tuple_xy is None:
			tuple_xy = _get_terminal_size_tput()
			# needed for window's python in cygwin's xterm!
	if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
		tuple_xy = _get_terminal_size_linux()
	if tuple_xy is None:
		#print "default"
		tuple_xy = (80, 25)      # default value
	return tuple_xy


def _get_terminal_size_windows():
	try:
		from ctypes import windll, create_string_buffer
		# stdin handle is -10
		# stdout handle is -11
		# stderr handle is -12
		h = windll.kernel32.GetStdHandle(-12)
		csbi = create_string_buffer(22)
		res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
		if res:
			(bufx, bufy, curx, cury, wattr,
				left, top, right, bottom,
				maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
			sizex = right - left + 1
			sizey = bottom - top + 1
			return sizex, sizey
	except:
		pass


def _get_terminal_size_tput():
	try:
		cols = int(subprocess.check_call(shlex.split('tput cols')))
		rows = int(subprocess.check_call(shlex.split('tput lines')))
		return (cols, rows)
	except:
		pass


def _get_terminal_size_linux():
	def ioctl_GWINSZ(fd):
		try:
			import fcntl
			import termios
			cr = struct.unpack('hh',
								fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
			return cr
		except:
			pass
	cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
	if not cr:
		try:
			fd = os.open(os.ctermid(), os.O_RDONLY)
			cr = ioctl_GWINSZ(fd)
			os.close(fd)
		except:
			pass
	if not cr:
		try:
			cr = (os.environ['LINES'], os.environ['COLUMNS'])
		except:
			return None
	return int(cr[1]), int(cr[0])

chars = ''
xMax, yMax = get_terminal_size()
map = []

delay = 0.02

#foreColor = [30,31,32,33,34,35,36,37]
foreColor = [0,1,2,3,4,5,6,7]
backColor = [40,41,42,43,44,45,46,47]
isColorRandom = False

fcolor = 2
gcolor = 4

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

def classic(screen):
	while True:
		#screen.clear()
		
		row = ''
		for i in range(xMax):
			ch = random.randint(0, 255)
			if ch >=33 and ch <= 126:
				#row += ('\x1b['+str(0) +";"+ (str(random.choice(foreColor)) if isColorRandom else str(fcolor)) + ";" + str(gcolor)+"m" + chr(ch) +'\x1b[0m')
				row += chr(ch)
			else:
				#row += ('\x1b['+str(0) +";"+ (str(random.choice(foreColor)) if isColorRandom else str(fcolor)) + ";" + str(gcolor)+"m" + ' ' +'\x1b[0m')
				row += ' '
		
		if len(map) >= yMax:
			del map[0]
		map.append(row)
		#for y, m in enumerate(map):
		#	print(pos(1, 1+y) + m)
		for y, m in enumerate(map):
			for x, s in enumerate(m):
				screen.print_at(s, x, y, (random.choice(foreColor) if isColorRandom else fcolor), 2, gcolor)
		time.sleep(delay)
		screen.refresh()
		#sleep(0.02)
		
def randmatrix(screen):
	while True:
		#screen.clear()
		row = ''
		for i in range(xMax):
			ch = random.randint(0, 255)
			if ch >=33 and ch <= 126:
				#row += ('\x1b['+str(0) +";"+ (str(random.choice(foreColor)) if isColorRandom else str(fcolor)) + ";" + str(gcolor)+"m" + chr(ch) +'\x1b[0m')
				row = chr(ch)
			else:
				#row += ('\x1b['+str(0) +";"+ (str(random.choice(foreColor)) if isColorRandom else str(fcolor)) + ";" + str(gcolor)+"m" + ' ' +'\x1b[0m')
				row = ' '
			screen.print_at(row, random.randint(0, xMax), random.randint(0, yMax), (random.choice(foreColor) if isColorRandom else fcolor), 2, gcolor)
		
		time.sleep(delay)
		screen.refresh()
		#sleep(0.02)

os.system('cls')
#colorama.init()

from asciimatics.screen import Screen
from time import sleep

Screen.wrapper(randmatrix)


#classic()