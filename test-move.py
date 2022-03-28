from time import sleep
from pynput.keyboard import Controller
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, time, shutil, pyautogui
from tkinter import *
from selenium import webdriver
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess,pyautogui,time,cv2,sys
import tkinter as tk
from ctypes import *
from pynput.keyboard import Controller
import random

delay = 5
path = r'C:\Users\soren\Downloads'
files = os.listdir(path)
dir_path = r'C:\Users\soren\Downloads'
cloud = r'C:\Users\soren\OneDrive\Music'
x = 0
DT = 60
RDT = ""
chromedriver_path = r'C:\Users\soren\Desktop\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
main_page = webdriver.current_window_handle
webdriver.minimize_window()
print("so far so good 1")
print("so far so good 1,5")
prefs = {"download.default_directory" : cloud}
chromedriver = chromedriver_path

def ran():
    global d
    n = random.randint(1,4)
    if n==1 :
        d="up"
    if n == 2 :
        d="down"
    if n == 3 :
        d="left"
    if n == 4 :
        d="right"



pyautogui.moveTo(700, 340)
sleep(10)
mo=0

while 2<3 :
  img = cv2.imread(r"D:\ARCHIVES\Computer_stuff\ATOM\play.png")
  y = pyautogui.locateOnScreen(img)
  death=0
  d="left"
  while 2 < 3 :
      img = cv2.imread(r"D:\ARCHIVES\Computer_stuff\ATOM\play.png")
      y = pyautogui.locateOnScreen(img)
      if y == None :
          sleep(0)
          print("playing...")
      else :
          try :
              death=death+1
              print("died ",death," times")
              AC = webdriver.find_element_by_xpath('//*[@id="playBtn"]')
              AC.click()
              sleep(2)
          except :
            print("play button is actually not here")
      if d == "left" :
          pyautogui.moveTo(440, 325)
          for i in range(5):
              if d == "left":
                  x, y = pyautogui.position()
                  pix = pyautogui.pixel(x, y)
                  if pix != (17, 17, 17) or mo > 45 :
                      print("ALERT VIRUS HERE")
                      ran()
                      mo=0
                  if pix == (17, 17, 17):
                      mo=mo+1
                  pyautogui.move(0, 80)
          for i in range(5):
              if d == "left":
                  x, y = pyautogui.position()
                  pix = pyautogui.pixel(x, y)
                  if pix != (17, 17, 17) or mo > 45 :
                      print("ALERT VIRUS HERE")
                      ran()
                      mo=0
                  if pix == (17, 17, 17):
                      mo=mo+1
                  pyautogui.move(0, -80)


      if d == "right":
            pyautogui.moveTo(1240, 325)
            for i in range(5):
                if d == "right":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="down"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(0, 80, duration=0.01)
            for i in range(5):
                if d == "right":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="down"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(0, -80, duration=0.01)
      if d == "up":
            pyautogui.moveTo(640, 325)
            for i in range(5):
                if d == "up":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="right"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(80, 0, duration=0.01)
            for i in range(5):
                if d == "up":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="right"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(-80, 0, duration=0.01)
      if d == "down":
            pyautogui.moveTo(640, 825)
            for i in range(5):
                if d == "down":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="left"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(80, 0, duration=0.01)
            for i in range(5):
                if d == "down":
                    x, y = pyautogui.position()
                    pix = pyautogui.pixel(x, y)
                    if pix == (0, 255, 0) or pix == (205, 85, 100) or pix == (255, 155, 255) or mo > 45 :
                        print("ALERT VIRUS HERE")
                        d="left"
                        mo=0
                    if pix == (17, 17, 17):
                        mo=mo+1
                    pyautogui.move(-80, 0, duration=0.01)
