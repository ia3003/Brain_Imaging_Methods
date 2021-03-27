from psychopy import visual, core, logging, event, gui  # import some libraries from PsychoPy, include logging for creating logfiles
from datetime import datetime # import datetime library for timestamp
from psychopy.hardware import keyboard # import keyboard library
import numpy as np
import csv
import random
from itertools import permutations 

# Set logging level and create log file
# getting the timestamp and including it into the logfile name
#timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
#lastLog = logging.LogFile("lastRun_"+timestamp+".log", level=logging.INFO, filemode='w')

# Get Participant ID
def get_id():  # GUI Dialogue Box
    mygui = gui.Dlg()
    mygui.addField("Subject ID:")
    mygui.show()
    participant_ID = mygui.data[0]
    return participant_ID
current_participant = get_id()

# create keyboard object
kb = keyboard.Keyboard()
clock = core.Clock()

no_hues = 8

trial_number = 0 # initializing trial tracker

data=[]
    
# change scale from 0 to 255 to -1 to 1
def change_scale(color):
  updated_val = []
  for val in color:
    if 0<=val<=127:
      new_val = (1/127)*val - 1
    else:
      new_val = (1/128)*(val - 127)
    updated_val.append(new_val)
  
  return tuple(updated_val)

#color list
blue_list = [(0,50,100),(0,50,120),(0,50,140),(0,50,160),(0,50,180),(0,50,200),(0,50,220),(0,50,240)]
red_list = [(100,0,30),(120,0,30),(140,0,30),(160,0,30),(180,0,30),(200,0,30),(220,0,30),(240,0,30)]
green_list = [(100,100,0),(100,120,0),(100,140,0),(100,160,0),(100,180,0),(100,200,0),(100,220,0),(100,140,0)]
purple_list=[(150,100,100),(150,100,120),(150,100,140),(150,100,160),(150,100,180),(150,100,200),(150,100,220),(150,100,240)]
orange_list=[(220,100,0),(220,120,0),(220,140,0),(220,160,0),(220,180,0),(220,200,0),(220,220,0),(220,240,0)]

color_list = [blue_list, red_list, green_list, purple_list, orange_list]
hue_ids = list(range(no_hues))
hue_comb = list(permutations(hue_ids,2)) #hue combinations

updated_color_list = []
for color in color_list:
  for idx in range(0,len(blue_list)):
    color[idx] = change_scale(color[idx])
  updated_color_list.append(color)
random.shuffle(updated_color_list)
 
#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")


#create fixation cross
fixation = visual.TextStim(mywin, '+', rgb=-1)

Participant_Instruction = visual.TextStim(mywin, 'You have to tell which one of the bottom squares matches the top square in terms of colour. To indicate your response, press the number key 1 if the bottom right square is of the same colour as the top square or 2 if the bottom left square has the same colour as the top square. Try to respond as quickly and as accurately as possible', 
rgb=-1)    
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['k'])

fixation.draw()
mywin.update()
core.wait(0.5)


for color in updated_color_list:
    random.shuffle(hue_comb)    
    for hue_pair in hue_comb: #(1,6)
        dist1_color = color[hue_pair[0]]
        dist2_color = color[hue_pair[1]]
        target_color = color[random.choice(hue_pair)]
        #create rectangular stimuli
        target = visual.Rect(win=mywin, width=5, height =5, pos=[0,0], fillColor=target_color, lineColor = None)
        dist1 = visual.Rect(win=mywin, width=5, height =5, pos=[-6,0], fillColor=dist1_color, lineColor = None)
        dist2 = visual.Rect(win=mywin, width=5, height =5, pos=[6,0], fillColor=dist2_color, lineColor = None)
        target.draw()
        mywin.update()
        core.wait(0.8)
        dist1.draw()
        dist2.draw()
        mywin.update()
        core.wait(0.8)
        #Subject_Response = event.waitKeys(keyList=['right', 'left'])
        

#print(Subject_Response)
#data.append(keys)
#keys = psychopy.event.waitKeys(timeStamped=clock)
#print(keys)
mywin.update()
logging.flush()  
   
Participant_Instruction.setText('End of the Experiment. Thank you')
Participant_Instruction.draw()
mywin.update()
core.wait(0.5)
