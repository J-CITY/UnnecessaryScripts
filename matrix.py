import os
import random
import time
import shlex
import struct
import platform
import subprocess
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
import argparse
import platform

#pip install asciimatics argparse

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
		tuple_xy = (80, 25) # default value
	return tuple_xy


def _get_terminal_size_windows():
	try:
		from ctypes import windll, create_string_buffer
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
			cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
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

xMax, yMax = get_terminal_size()
map = []

delay = 0.02

#foreColor = [30,31,32,33,34,35,36,37]
foreColor = [0,1,2,3,4,5,6,7]
backColor = [40,41,42,43,44,45,46,47]
mapColorBg = dict()
mapColorBg[0] = 40
mapColorBg[1] = 41
mapColorBg[2] = 42
mapColorBg[3] = 43
mapColorBg[4] = 44
mapColorBg[5] = 45
mapColorBg[6] = 46
mapColorBg[7] = 47
isColorRandom = False

fcolor = 2
gcolor = 0

OS = platform.system()

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

def classic(screen):
	global xMax, yMax
	while True:
		event = screen.get_event()
		if screen.has_resized():
			xMax, yMax = get_terminal_size()
		if isinstance(event, KeyboardEvent):
			key = event.key_code
			if key in (ord('q'), ord('Q')):
				return

		row = ''
		for i in range(xMax):
			ch = random.randint(0, 255)
			if ch >=33 and ch <= 126:
				row += chr(ch)
			else:
				row += ' '
		
		if len(map) >= yMax:
			del map[0]
		map.append(row)
		for y, m in enumerate(map):
			for x, s in enumerate(m):
				screen.print_at(s, x, y, (random.choice(foreColor) if isColorRandom else fcolor), 2, gcolor)
		time.sleep(delay)
		screen.refresh()
		
def randmatrix(screen):
	global xMax, yMax
	while True:
		event = screen.get_event()
		if screen.has_resized():
			xMax, yMax = get_terminal_size()
		if isinstance(event, KeyboardEvent):
			key = event.key_code
			if key in (ord('q'), ord('Q')):
				return
		row = ''
		for i in range(xMax):
			ch = random.randint(0, 255)
			if ch >=33 and ch <= 126:
				row = chr(ch)
			else:
				row = ' '
			screen.print_at(row, random.randint(0, xMax), random.randint(0, yMax), (random.choice(foreColor) if isColorRandom else fcolor), 2, gcolor)
		
		time.sleep(delay)
		screen.refresh()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="Matrix script", description='Print matrix to console. Q - for exit.')
	parser.add_argument('-fg', type=int, help="Foreground color 0-7 [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]")
	parser.add_argument('-bg', type=int, help="Background color 0-7 [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]")
	parser.add_argument('-type', type=str, help="Mode randmatrix or classic")
	parser.add_argument('-r', action='store_true', help="Use random colors")
	parser.set_defaults(r=False)

	args = parser.parse_args()
	if args.r is not None:
		isColorRandom = args.r

	if args.fg is not None and args.fg >= 0 and args.fg <= 7:
		fcolor = args.fg

	if args.bg is not None and args.bg >= 0 and args.bg <= 7:
		bcolor = mapColorBg[args.bg]

	fun = classic
	if args.type is not None and args.type == "randmatrix":
		fun = randmatrix

	if OS == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	Screen.wrapper(fun)
