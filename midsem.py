from psychopy import visual, core, logging, event  # import some libraries from PsychoPy, include logging for creating logfiles
from datetime import datetime # import datetime library for timestamp
from psychopy.hardware import keyboard # import keyboard library

# Set logging level and create log file

# this is for displaying logs on the console, if needed can be commented out
#logging.console.setLevel(logging.EXP)

# getting the timestamp and including it into the logfile name
timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
lastLog = logging.LogFile("lastRun_"+timestamp+".log", level=logging.INFO, filemode='w')

# create keyboard object
kb = keyboard.Keyboard()


#create a window
#the demo monitor specs are as follows 
#Aspect Ratio (pixel): 1024 x 768
#Screen width (cm): 30
#screen distance (cm): 30

mywin = visual.Window([800,600], monitor="testMonitor", units="deg")


#create some stimuli
target = visual.Rect(win=mywin, width=5, height =5, pos=[0,5], fillColor=(0,50,100))
target.colorSpace = 'rgb255'
dist1 = visual.Rect(win=mywin, width=5, height =5, pos=[-6,-5], fillColor=(0,50,0.100))
dist1.colorSpace = 'rgb255'
dist2 = visual.Rect(win=mywin, width=5, height =5, pos=[6,-5], fillColor=(0,50,120))
dist2.colorSpace = 'rgb255'

#it is a sine grating with a gaussian on top
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
target.draw()
dist1.draw()
dist2.draw()
fixation.draw()
mywin.update()

#pause, so you get a chance to see it!
core.wait(5.0)
logging.flush()
