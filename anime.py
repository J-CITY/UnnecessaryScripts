import os
import time
import colorama
import random
from colorama import Fore, Back, Style

import os
import shlex
import struct
import platform
import subprocess
import argparse

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


def pos(x, y):
	return "\033[%d;%dH" % (y, x)

x = [5, 5, 20, 20]
y = [5, 20, 5, 20]	

dir = [0, 1, 2, 3]

colors = [Fore.CYAN, Fore.GREEN, Fore.RED, Fore.WHITE]

xMax, yMax = get_terminal_size()

def move(a, i):
	ch = ""
	if a == 0:
		ch = "/"
		#if y[i] > 0 and x[i] < 20:
		y[i]-=1
		x[i]+=1
		if y[i] < 0:
			y[i]=yMax-1
		if x[i] >= xMax-1:
			x[i]=0
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 1:
		ch = "/"
		#if x[i] > 0 and y[i] < 20:
		x[i]-=1
		y[i]+=1
		if x[i] < 0:
			x[i]=xMax-1
		if y[i] >= yMax-1:
			y[i]=0
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 2:
		ch = "\\"
		#if y[i] > 0 and x[i] > 0:
		y[i]-=1
		x[i]-=1
		if x[i] < 0:
			x[i]=xMax-1
		if y[i] < 0:
			y[i]=yMax-1
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 3:
		ch = "\\"
		#if y[i] < 20 and x[i] < 20:
		y[i]+=1
		x[i]+=1
		if y[i] >= yMax-1:
			y[i]=0
		if x[i] >= xMax-1:
			x[i]=0
		print(pos(x[i], y[i]) + colors[i] + ch);
			
def newMove(i):
	if dir[i] == 0:
		if y[i] > 0:
			#y[i]-=1
			x[i]+=1; ch="\\"; dir[i] = 3
			print(pos(x[i], y[i]) + colors[i] + ch);
	elif dir[i] == 1:
		if x[i] > 0:
			x[i]-=1; ch="\\"; dir[i] = 2
			#y[i]+=1
			print(pos(x[i], y[i]) + colors[i] + ch);
	elif dir[i] == 2:
		if y[i] > 0 and x[i] > 0:
			#y[i]-=1
			x[i]-=1; ch="/"; dir[i]=1
			print(pos(x[i], y[i]) + colors[i] + ch);
	elif dir[i] == 3:
		if y[i] < 20 and x[i] < 20:
			y[i]+=1; ch="/"; dir[i]=0
			#x[i]+=1
			print(pos(x[i], y[i]) + colors[i] + ch);
	
	
def anime():
	while True:
		time.sleep(0.1)
		a = random.randint(0, 10)
		if a < 1:
			newMove(0)
		a = random.randint(0, 10)
		if a < 1:
			newMove(1)
		a = random.randint(0, 10)
		if a < 1:
			newMove(2)
		a = random.randint(0, 10)
		if a < 1:
			newMove(3)
		move(dir[0], 0)
		move(dir[1], 1)
		move(dir[2], 2)
		move(dir[3], 3)
########################
def move1(a, i):
	ch = ""
	if a == 0:
		ch = "─"
		x[i]+=1
		if x[i] >= xMax-1:
			x[i]=0
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 1:
		ch = "─"
		x[i]-=1
		if x[i] < 0:
			x[i]=xMax-1
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 2:
		ch = "|"
		y[i]+=1
		if y[i] > yMax-1:
			y[i]=0
		print(pos(x[i], y[i]) + colors[i] + ch);
	elif a == 3:
		ch = "|"
		y[i]-=1
		if y[i] < 0:
			y[i]=yMax
		print(pos(x[i], y[i]) + colors[i] + ch.encode);
			
def newMove1(i):
	ch=""
	if dir[i] == 0:#x++
		if x[i] < xMax-1:
			#x[i]+=1 ch="┛"; dir[i] = 3
			x[i]+=1; ch="\\"; dir[i] = 2
	#		print(pos(x[i], y[i]) + colors[i] + str(ch).strip().encode('utf-8'));
	elif dir[i] == 1:
		if x[i] > 0:
			x[i]-=1; ch="/"; dir[i] = 2
			#x[i]-=1; ch=""; dir[i] = 3
	#		print(pos(x[i], y[i]) + colors[i] + str(ch).strip().encode('utf-8'));
	elif dir[i] == 2:
		if y[i] < yMax-1:
			#y[i]+=1; ch="┗"; dir[i]=0
			y[i]+=1; ch="/"; dir[i]=1
	#		print(pos(x[i], y[i]) + colors[i] + str(ch).strip().encode('utf-8'));
	elif dir[i] == 3:
		if y[i] < 20 and x[i] < 20:
			y[i]-=1; ch="/"; dir[i]=0
			#y[i]-=1; ch="┓"; dir[i]=1
	else:
		return
	print(pos(x[i], y[i]) + colors[i] + ch);
		
def anime1():
	while True:
		time.sleep(0.1)
		
		a = random.randint(0, 10)
		if a < 1:
			newMove1(0)
		move1(dir[0], 0)
		
		a = random.randint(0, 10)
		if a < 1:
			newMove1(1)
		move1(dir[1], 1)
		
		a = random.randint(0, 10)
		if a < 1:
			newMove1(2)
		move1(dir[2], 2)
		
		a = random.randint(0, 10)
		if a < 1:
			newMove1(2)
		move1(dir[2], 2)
		
OS = platform.system()
if OS == "Windows":
	os.system('cls')
else:
	os.system('clear')
colorama.init()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="Line animation", description='Line console animation.')
	parser.add_argument('-type', type=int, help="Animation type: 1 or 2")
	args = parser.parse_args()
	if args.type is not None and args.type == 1:
		anime()
	else:
		anime1()



