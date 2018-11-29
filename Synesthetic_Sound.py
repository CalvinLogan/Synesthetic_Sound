import os
import gui
from gui import *

#input: none
#return: the width of the screen
def getScreenWidth():
  return Toolkit.getDefaultToolkit().getScreenSize().width

#input: none
#return: the height of the screen
def getScreenHeight():
  return Toolkit.getDefaultToolkit().getScreenSize().height

#input: none
#return: none
#sets up the display
def setup():
  window = Display("Synesthetic Sound", getScreenWidth(), getScreenHeight())

setup()
