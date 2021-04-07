from psychopy import visual, core, logging, event, gui  # import some libraries from PsychoPy, include logging for creating logfiles
from datetime import datetime # import datetime library for timestamp
from psychopy.hardware import keyboard # import keyboard library
import numpy as np
import csv
import random
from itertools import permutations

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
blue_list = [(0,50,100),(0,50,110),(0,50,120),(0,50,130),(0,50,140),(0,50,150),(0,50,160),(0,50,170)]
red_list = [(100,0,30),(110,0,30),(120,0,30),(130,0,30),(140,0,30),(150,0,30),(160,0,30),(170,0,30)]
green_list = [(100,100,0),(100,110,0),(100,120,0),(100,130,0),(100,140,0),(100,150,0),(100,160,0),(100,170,0)]
purple_list=[(150,100,100),(150,100,110),(150,100,120),(150,100,130),(150,100,140),(150,100,150),(150,100,160),(150,100,170)]
orange_list=[(220,100,0),(220,110,0),(220,120,0),(220,130,0),(220,140,0),(220,150,0),(220,160,0),(220,170,0)]

color_list = [blue_list, red_list, green_list, purple_list, orange_list]

updated_color_list = []
for color in color_list:
  for idx in range(0,len(blue_list)):
    color[idx] = change_scale(color[idx])
  updated_color_list.append(color)

hue_list = []
for item in updated_color_list:
    hue_list+=item
    
final_list = []
for color in updated_color_list:
  final_list+=list(permutations(color,2))
random.shuffle(final_list)
 
#create a window
mywin = visual.Window([1200,800], monitor="testMonitor", units="deg")


#create fixation cross
fixation = visual.TextStim(mywin, '+', rgb=-1)

Participant_Instruction = visual.TextStim(mywin, 'You have to tell which one of the bottom squares matches the top square in terms of colour. To indicate your response, press the number right arrow key if the bottom right square is of the same colour as the top square or the left arrow ley if the bottom left square has the same colour as the top square. Try to respond as quickly and as accurately as possible. Press the k key to continue.', 
rgb=-1)    
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['k'])

fixation.draw()
mywin.update()
core.wait(0.5)

fields =  ['Participant ID', 'Trial no', 'Target Color', 'Dist1', 'Dist2', 'Response', 'Accuracy']
filename = 'Expt1_Participant_'+str(current_participant)+'.csv'
trial_no=1
with open (filename,'a') as my_file:
    writer = csv.DictWriter(my_file, fieldnames = fields)
    writer.writeheader()


for hue_comb in final_list:
    dist1_color = hue_comb[0]
    dist2_color = hue_comb[1]
    target_color = random.choice(hue_comb)
    if target_color == dist1_color:
        correct_resp = 'left'
    else:
        correct_resp = 'right'
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
    Subject_Response = event.waitKeys(keyList=['right', 'left'])
    #print(Subject_Response)
    if Subject_Response[0]==correct_resp:
        accuracy = 1
    else:
        accuracy = 0
    resp_dict = [{'Participant ID': current_participant, 'Trial no': trial_no, 'Target Color': target_color,'Dist1':dist1_color, 'Dist2': dist2_color,'Response': Subject_Response[0], 'Accuracy': accuracy}]
   
    trial_no+=1
    with open(filename,'a') as my_file:
        writer = csv.DictWriter(my_file, fieldnames = fields)
        writer.writerows(resp_dict)

mywin.update()
logging.flush()  

random.shuffle(hue_list)

Participant_Instruction = visual.TextStim(mywin, 'Now, a colored square will appear on the screen followed by a dialog box. You have to type the name of that colour or describe it in all the languages you know in the dialog box. Press the k key to continue.', 
rgb=-1)    
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['k'])

def get_names():  # GUI Dialogue Box
    color_name = gui.Dlg()
    color_name.addField("Color Name")
    color_name.show()
    naming_data = color_name.data[0]
    return naming_data
#current_color = get_names()

fields =  ['Participant ID', 'Trial no', 'Hue Color', 'Verbal Labels']
filename = 'Expt2_Participant_'+str(current_participant)+'.csv'
trial_no=1
with open (filename,'a') as my_file:
    writer = csv.DictWriter(my_file, fieldnames = fields)
    writer.writeheader()

for hue in hue_list:
    target = visual.Rect(win=mywin, width=5, height =5, pos=[0,0], fillColor=hue, lineColor = None)
    fixation.draw()
    mywin.update()
    core.wait(0.5)
    target.draw()
    mywin.update()
    core.wait(1)
    current_color = get_names()
    resp_dict = [{'Participant ID': current_participant, 'Trial no': trial_no, 'Hue Color':hue,'Verbal Labels': current_color}]
   
    trial_no+=1
    with open(filename,'a') as my_file:
        writer = csv.DictWriter(my_file, fieldnames = fields)
        writer.writerows(resp_dict)


mywin.update()
logging.flush()  
 
Participant_Instruction.setText('End of the Experiment. Thank you')
Participant_Instruction.draw()
mywin.update()
core.wait(0.5)
