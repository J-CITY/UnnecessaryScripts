import os
import time
import colorama
import random
from colorama import Fore, Back, Style
import platform
import subprocess
import shlex
import struct
import argparse

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

colors = [Fore.CYAN, Fore.GREEN, Fore.RED, Fore.WHITE]


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
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
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

xMax, yMax = get_terminal_size()

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
		
		if self.x + self.radius/2 > xMax-1:
			self.xspeed = -self.xspeed
		
		if self.y + self.radius/2 > yMax-1 or self.y + self.radius/2 < 0:
			self.yspeed = -self.yspeed
		
		self.x = round(self.x)
		self.y = round(self.y)
		if self.y >= yMax-1:
			self.y = yMax-1
		if self.x >= xMax-1:
			self.x = xMax-1
		if self.y <= 0:
			self.y = 0
		if self.x <= 0:
			self.x = 0
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

OS = platform.system()
if OS == "Windows":
	os.system('cls')
else:
	os.system('clear')
colorama.init()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="Ball animation", description='Ball console animation.')
	parser.add_argument('-count', type=int, help="Ball count")
	args = parser.parse_args()
	if args.count is not None and args.count > 0:
		count = args.count
	anime()
