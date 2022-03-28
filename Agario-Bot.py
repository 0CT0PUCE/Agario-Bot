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
webdriver.maximize_window()
print("so far so good 1")
print("so far so good 1,5")
prefs = {"download.default_directory" : cloud}
chromedriver = chromedriver_path
def ran():
    global d
    n = random.randint(1,4)
    if n==4 :
        d="up"
    if n == 2 :
        d="down"
    if n == 3 :
        d="left"
    if n == 1 :
        d="right"
mo=0

if 2 < 3:
    keyboard = Controller()
    webdriver.maximize_window()
    webdriver.get('https://jeu.video/agario/fr/')
    sleep(1)
    connexion = webdriver.find_element_by_xpath('//*[@id="advertSlot"]/div[1]/div/div[4]/div/div[1]/a')
    connexion.click()
    sleep(2)
    login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input')
    login.click()
    keyboard.type('0CT0PUCE')
    PS = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input')
    PS.click()
    sleep(1)
    keyboard.type('legO2005')
    sleep(1)
    CO = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/button')
    CO.click()
    sleep(5)
    HA = webdriver.find_element_by_xpath('//*[@id="modeButton_2"]')
    HA.click()
    sleep(1)
    play = webdriver.find_element_by_xpath('//*[@id="playerStart_1"]')
    play.click()
    para = webdriver.find_element_by_xpath('//*[@id="slotForm"]/div[4]/div[1]/div[2]/button')
    para.click()
    para = webdriver.find_element_by_xpath('//*[@id="settings"]/div[2]/label[1]/input')
    para.click()
    A1 = webdriver.find_element_by_xpath('//*[@id="settings"]/div[2]/label[3]/input')
    A1.click()
    play = webdriver.find_element_by_xpath('//*[@id="playBtn"]')
    play.click()
    pyautogui.moveTo(700, 340)
    sleep(10)


    img = cv2.imread(r"D:\ARCHIVES\Computer_stuff\ATOM\play.png")
    y = pyautogui.locateOnScreen(img)
    death=0
    lvl=0
    d="left"
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
          else :
              try :
                  death=death+1
                  print("died ",death," times")
                  AC = webdriver.find_element_by_xpath('//*[@id="playBtn"]')
                  AC.click()
                  sleep(2)
              except :
                print("play button is actually not here")
          img = cv2.imread(r"D:\ARCHIVES\Computer_stuff\ATOM\replay.png")
          y = pyautogui.locateOnScreen(img)
          if y == None :
              sleep(0)
          else :
              try :
                  lvl=lvl+1
                  print("level : ",lvl)
                  RE = webdriver.find_element_by_xpath('//*[@id="levelModal"]/div/div/div[3]/button')
                  RE.click()
                  sleep(2)
              except :
                print("play button is actually not here")
          if d == "left" :
              pyautogui.moveTo(440, 325)
              for i in range(5):
                  if d == "left":
                      x, y = pyautogui.position()
                      pix = pyautogui.pixel(x, y)
                      if pix != (17, 17, 17) or mo > 20 :
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
                      if pix != (17, 17, 17) or mo > 20 :
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
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(0, 80)
                for i in range(5):
                    if d == "right":
                        x, y = pyautogui.position()
                        pix = pyautogui.pixel(x, y)
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(0, -80)
          if d == "up":
                pyautogui.moveTo(640, 325)
                for i in range(5):
                    if d == "up":
                        x, y = pyautogui.position()
                        pix = pyautogui.pixel(x, y)
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(80, 0)
                for i in range(5):
                    if d == "up":
                        x, y = pyautogui.position()
                        pix = pyautogui.pixel(x, y)
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(-80, 0)
          if d == "down":
                pyautogui.moveTo(640, 825)
                for i in range(5):
                    if d == "down":
                        x, y = pyautogui.position()
                        pix = pyautogui.pixel(x, y)
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(80, 0)
                for i in range(5):
                    if d == "down":
                        x, y = pyautogui.position()
                        pix = pyautogui.pixel(x, y)
                        if pix != (17, 17, 17) or mo > 20 :
                            print("ALERT VIRUS HERE")
                            ran()
                            mo=0
                        if pix == (17, 17, 17):
                            mo=mo+1
                        pyautogui.move(-80, 0)
