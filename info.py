import os
import time
import platform
import cpuinfo
from screeninfo import get_monitors
from uptime import uptime
import psutil
import pyautogui
import colorama
from colorama import Fore, Back, Style
import argparse
#import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--screenshot", action="store_true",
                    help="create screenshot")
parser.add_argument("-t", "--time", action="append",
                    help="time in second")
args = parser.parse_args()

timesec = 0
if args.time != None:
	timesec = int(args.time)

start_y = 8
start_x = 40	

colorama.init()

def pos(x, y):
	return "\033[%d;%dH" % (y, x)

def PrintLogo():
	_y=0
	print(pos(0, _y) + Fore.CYAN + "                               ."); _y+=1
	print(pos(0, _y) + Fore.CYAN + "                   ....,,:;+ccll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "      ...,,+:  cllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + ",ccllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "                                "); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "lllllllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "`'cclllllllll  lllllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "       `' \\\\*  :ccllllllllllllll"); _y+=1
	print(pos(0, _y) + Fore.CYAN + "                      ````''*::c" + Style.RESET_ALL); _y+=1


OS = platform.system()


if OS == "Windows":
	os.system('cls')
else:
	os.system('clear')
	
PrintLogo()

host = ""
if OS == "Windows":
	host = os.getlogin()
else:
	host = os.uname()[0]
print(pos(start_x, start_y) + "Username:", host)
start_y+=1
	
print(pos(start_x, start_y) + "OS:", OS, platform.release())
start_y+=1

if OS == "Linux":
	print("Distro:", platform.linux_distribution())

print(pos(start_x, start_y) + "CPU:", cpuinfo.get_cpu_info()['brand'])
start_y+=1

if OS == "Windows":
	gpu = os.popen("wmic path win32_VideoController get name").read()
	gpu = gpu[26:]
	print(pos(start_x, start_y) + "GPU:", gpu)
else:
	print(pos(start_x, start_y) + "GPU:", os.popen("lspci | grep VGA").read())
start_y+=1

print(pos(start_x, start_y) + "Mem:", psutil.virtual_memory().used/1024/1024//1024+1, "/", psutil.virtual_memory().total/1024/1024//1024+1, "GB")
start_y+=1

print(pos(start_x, start_y) + "Disk:", psutil.disk_usage('/').used/1024/1024//1024+1, "/", psutil.disk_usage('/').total/1024/1024//1024+1, "GB")
start_y+=1

monitor = "Resolution: "
for m in get_monitors():
	mon = str(m)
	monitor += mon[8:mon.find("+")]
print(pos(start_x, start_y) + monitor)
start_y+=1

print(pos(start_x, start_y) + "Uptime:", uptime() // 3600 + 1, "h")
start_y+=3


#COLORS
space = "   "
print(pos(start_x, start_y) + Back.RED + space, Back.GREEN + space, 
	Back.YELLOW + space, Back.BLUE + space, Back.MAGENTA + space, 
	Back.CYAN + space, Back.WHITE + space, Back.BLACK + space + Style.RESET_ALL)

time.sleep(timesec)
if args.screenshot:
	pic = pyautogui.screenshot()
	pic.save('Screenshot.png') 