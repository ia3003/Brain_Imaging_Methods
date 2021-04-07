from psychopy import visual, core, logging, event, gui  # import some libraries from PsychoPy, include logging for creating logfiles
from datetime import datetime # import datetime library for timestamp
from psychopy.hardware import keyboard # import keyboard library
import numpy as np

#color list
blue_list = [(0,50,100),(0,50,110),(0,50,120),(0,50,130),(0,50,140),(0,50,150),(0,50,160),(0,50,170)]
red_list = [(100,0,30),(110,0,30),(120,0,30),(130,0,30),(140,0,30),(150,0,30),(160,0,30),(170,0,30)]
green_list = [(100,100,0),(100,110,0),(100,120,0),(100,130,0),(100,140,0),(100,150,0),(100,160,0),(100,170,0)]
purple_list=[(150,100,100),(150,100,110),(150,100,120),(150,100,130),(150,100,140),(150,100,150),(150,100,160),(150,100,170)]
orange_list=[(220,100,0),(220,110,0),(220,120,0),(220,130,0),(220,140,0),(220,150,0),(220,160,0),(220,170,0)]

color_list = [blue_list, red_list, green_list, purple_list, orange_list]

