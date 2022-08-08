#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on August 08, 2022, at 21:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('latest')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.3'
expName = 'psycho-boilerplate'  # from the Builder filename that created this script
expInfo = {
    'controller': '[k]lawiatura/[m]yszka?',
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\XRYW\\git\\psychuw\\boiler-psychoplate\\psycho-boilerplate.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1600, 900], fullscr=False, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='lg', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup_and_instr_0" ---
# Run 'Begin Experiment' code from setup_code

###### setup_code ######

# kontrolery i ich kody
CONTROLLERS = {'klawiatura':0, 'k':0, 0:0,
               'myszka':1, 'm':1, 1:1}
               
               
# PLIKI Z OBRAZKAMI DO TRIALÓW:
# jak wyżej: pierwsze z listy są dzieciaki, drugie dorośli
# potem: pierwsza jest wersja z niebieskim pudelkiem po lewej
IMAGE_FILES = {'f': [['imgs/F/C-niebieskie-zolte.png','imgs/F/C-zolte-niebieskie.png'],
                     ['imgs/F/A-niebieskie-zolte.png','imgs/F/A-zolte-niebieskie.png']],
               'm': [['imgs/M/C-niebieskie-zolte.png','imgs/M/C-zolte-niebieskie.png'],
                     ['imgs/M/A-niebieskie-zolte.png','imgs/M/A-zolte-niebieskie.png']],
               'control':['imgs/control/pytajnik-n-z.png','imgs/control/pytajnik-z-n.png']}

#g = expInfo['gender'].lower()   # expInfo ustalane jest w gui, na starcie
# g niestety na potrzeby tego eksperymentu powinna byc f albo m
#
#if g != 'f' and g != 'm':
    # w przeciwnym wypadku jest przydzielana losowo
    # tak jak w prawdziwym życiu
#    logging.warning(f"GENDER?!? Expected 'F' or 'M', got: '{g}'.\tZatem ustawiam losowy zestaw obrazków.")
#    g = np.random.choice(['f','m'])

# ustawiam kontroler:
controller = expInfo['controller'].lower()
try:
    c = CONTROLLERS[controller]
    
except KeyError:
    logging.error(f"Niepoprawny kontroler: {controller}\t Dostępne opcje to {'/'.join(CONTROLLERS)}\nWyłączam sie.")
    logging.flush()
    core.quit()


# WSZYSTKIE STRINGI Z TEKSTEM

instr_texts = {0: "INSTR TEXT [0]", 1: "INSTR TEXT [1]"}

device_texts = {'continue':["Wciśnij spację aby kontynuować.","Wciśnij dowolny przycisk myszy aby kontynuować.","Wciśnij środkowy przycisk aby kontynuować."],
                'controls':["TEKST O TYM JAK KONTROLOWAĆ [0]",
                            "TEKST O TYM JAK KONTROLOWAĆ [1]"]}
#for i in range(len(device_texts['controls'])):
#    device_texts['controls'][i]+='\nStaraj się odpowiedzieć najszybciej jak potrafisz.'

S = {
    "pause_text": "Masz chwilę przerwy.\n"+device_texts['continue'][c].replace('.',' zadanie.'),
    "begin_blocks": "Koniec bloku treningowego. Za chwilę rozpoczniesz właściwą część zadania.",
    "begin_training": "Za chwilę rozpoczniesz blok treningowy.",
 
}

# pomocne zmienne 
corrects = 0
trials = None
# Run 'Begin Experiment' code from cedrus_setup
#
###### cedrus_setup ######
#
#import pyxid2 as pyxid
#
#if c == 2:
#    # szukamy urządzenia:
#    cedrusTimer = core.Clock()
#    while cedrusTimer.getTime() < 5:    # czekamy max 5 sekundy na objawienie sie sprzętu
#        
#        devices = pyxid.get_xid_devices()
#        if len(devices) > 0:
#            cedrus = devices[0]
#            logging.info(f"Znaleziony kontroler to {cedrus.device_name}")
#            break
#        else:
#            core.wait(0.1)
#    else:
#        logging.warning("Nie znaleziono zadnego sprzetu XID.")
#        core.quit()
#    
#    # konkretnie szukamy Cedrusa RB-530
#    if cedrus.is_response_device() and cedrus.device_name == 'Cedrus RB-530':
#        cedrus.reset_base_timer()
#        cedrus.reset_rt_timer()
#    else:
#        logging.warning("Znaleziony urzadzenie XID nie jest wlasciwym kontrolerem do tego zadania.")
#        core.quit()
#
instr_text_0 = visual.TextStim(win=win, name='instr_text_0',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
press_space_text_6 = visual.TextStim(win=win, name='press_space_text_6',
    text='',
    font='Cambria',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
space_resp_8 = keyboard.Keyboard()
mouse_continue = event.Mouse(win=win)
x, y = [None, None]
mouse_continue.mouseClock = core.Clock()

# --- Initialize components for Routine "instr_1" ---
instr_text_1 = visual.TextStim(win=win, name='instr_text_1',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_resp_1 = keyboard.Keyboard()
press_space_text_1 = visual.TextStim(win=win, name='press_space_text_1',
    text=device_texts['continue'][c],
    font='Cambria',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
mouse_continue_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_1.mouseClock = core.Clock()
image_1 = visual.ImageStim(
    win=win,
    name='image_1', 
    image='imgs/Animals_166_v.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0.1), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "begin_training" ---
space_resp = keyboard.Keyboard()
begin_training_text = visual.TextStim(win=win, name='begin_training_text',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.06, wrapWidth=1.1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_continue_13 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_13.mouseClock = core.Clock()
press_space_text_12 = visual.TextStim(win=win, name='press_space_text_12',
    text='',
    font='Cambria',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "fixation" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from trial_setup

pauseText = S["pause_text"]

# --- Initialize components for Routine "actual_trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Times New Roman',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0,-0.05), size=[0.8],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "training_results" ---
results_text_2 = visual.TextStim(win=win, name='results_text_2',
    text='',
    font='Cambria',
    pos=(-0.1, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from training_results_code

trainingDone = False 
space_resp_13 = keyboard.Keyboard()
press_space_text_10 = visual.TextStim(win=win, name='press_space_text_10',
    text=device_texts['continue'][c],
    font='Cambria',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse_continue_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_12.mouseClock = core.Clock()

# --- Initialize components for Routine "pause_1" ---
pause_text_2 = visual.TextStim(win=win, name='pause_text_2',
    text='',
    font='Times New Roman',
    pos=(-0.1, -0.1), height=0.06, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_resp_12 = keyboard.Keyboard()
mouse_continue_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_9.mouseClock = core.Clock()
press_space_text_11 = visual.TextStim(win=win, name='press_space_text_11',
    text='',
    font='Cambria',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "fixation" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from trial_setup

pauseText = S["pause_text"]

# --- Initialize components for Routine "actual_trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Times New Roman',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0,-0.05), size=[0.8],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()

# --- Initialize components for Routine "pause_2" ---
pause_text = visual.TextStim(win=win, name='pause_text',
    text='',
    font='Times New Roman',
    pos=(-0.25, -0.1), height=0.06, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_resp_11 = keyboard.Keyboard()
mouse_continue_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_8.mouseClock = core.Clock()

# --- Initialize components for Routine "results" ---
results_text = visual.TextStim(win=win, name='results_text',
    text='',
    font='Cambria',
    pos=(-0.1, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_resp_10 = keyboard.Keyboard()
press_space_text_9 = visual.TextStim(win=win, name='press_space_text_9',
    text='To koniec zadania. Dziękujemy za udział w eksperymencie.',
    font='Times New Roman',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse_continue_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_4.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup_and_instr_0" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_text_0.setText(instr_texts[0])
press_space_text_6.setText(device_texts['continue'][c])
space_resp_8.keys = []
space_resp_8.rt = []
_space_resp_8_allKeys = []
# setup some python lists for storing info about the mouse_continue
gotValidClick = False  # until a click is received
# keep track of which components have finished
setup_and_instr_0Components = [instr_text_0, press_space_text_6, space_resp_8, mouse_continue]
for thisComponent in setup_and_instr_0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup_and_instr_0" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text_0* updates
    if instr_text_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text_0.frameNStart = frameN  # exact frame index
        instr_text_0.tStart = t  # local t and not account for scr refresh
        instr_text_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_0, 'tStartRefresh')  # time at next scr refresh
        instr_text_0.setAutoDraw(True)
    
    # *press_space_text_6* updates
    if press_space_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_6.frameNStart = frameN  # exact frame index
        press_space_text_6.tStart = t  # local t and not account for scr refresh
        press_space_text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_6, 'tStartRefresh')  # time at next scr refresh
        press_space_text_6.setAutoDraw(True)
    
    # *space_resp_8* updates
    waitOnFlip = False
    if space_resp_8.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        space_resp_8.frameNStart = frameN  # exact frame index
        space_resp_8.tStart = t  # local t and not account for scr refresh
        space_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_8, 'tStartRefresh')  # time at next scr refresh
        space_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_8_allKeys.extend(theseKeys)
        if len(_space_resp_8_allKeys):
            space_resp_8.keys = _space_resp_8_allKeys[-1].name  # just the last key pressed
            space_resp_8.rt = _space_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouse_continue* updates
    if mouse_continue.status == NOT_STARTED and t >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue.frameNStart = frameN  # exact frame index
        mouse_continue.tStart = t  # local t and not account for scr refresh
        mouse_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue, 'tStartRefresh')  # time at next scr refresh
        mouse_continue.status = STARTED
        mouse_continue.mouseClock.reset()
        prevButtonState = mouse_continue.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    # Run 'Each Frame' code from cedrus_continue
    #
    # cedrus_continue
    #
    # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
    
    #if c == 2:
    #    cedrus.poll_for_response()
    #    while cedrus.has_response():
    #        response = cedrus.get_next_response()
    #        
    #        if response['pressed'] and response['key'] == 2:
    #            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setup_and_instr_0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup_and_instr_0" ---
for thisComponent in setup_and_instr_0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "setup_and_instr_0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instr_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_text_1.setText(instr_texts[1])
space_resp_1.keys = []
space_resp_1.rt = []
_space_resp_1_allKeys = []
# setup some python lists for storing info about the mouse_continue_1
gotValidClick = False  # until a click is received
# keep track of which components have finished
instr_1Components = [instr_text_1, space_resp_1, press_space_text_1, mouse_continue_1, image_1]
for thisComponent in instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instr_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text_1* updates
    if instr_text_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_text_1.frameNStart = frameN  # exact frame index
        instr_text_1.tStart = t  # local t and not account for scr refresh
        instr_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_1, 'tStartRefresh')  # time at next scr refresh
        instr_text_1.setAutoDraw(True)
    
    # *space_resp_1* updates
    waitOnFlip = False
    if space_resp_1.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        space_resp_1.frameNStart = frameN  # exact frame index
        space_resp_1.tStart = t  # local t and not account for scr refresh
        space_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_1, 'tStartRefresh')  # time at next scr refresh
        space_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_1_allKeys.extend(theseKeys)
        if len(_space_resp_1_allKeys):
            space_resp_1.keys = _space_resp_1_allKeys[-1].name  # just the last key pressed
            space_resp_1.rt = _space_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_text_1* updates
    if press_space_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_1.frameNStart = frameN  # exact frame index
        press_space_text_1.tStart = t  # local t and not account for scr refresh
        press_space_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_1, 'tStartRefresh')  # time at next scr refresh
        press_space_text_1.setAutoDraw(True)
    # *mouse_continue_1* updates
    if mouse_continue_1.status == NOT_STARTED and t >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue_1.frameNStart = frameN  # exact frame index
        mouse_continue_1.tStart = t  # local t and not account for scr refresh
        mouse_continue_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue_1, 'tStartRefresh')  # time at next scr refresh
        mouse_continue_1.status = STARTED
        mouse_continue_1.mouseClock.reset()
        prevButtonState = mouse_continue_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    # Run 'Each Frame' code from cedrus_continue_2
    
    # cedrus_continue
    
    # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
    
    if c == 2:
        cedrus.poll_for_response()
        while cedrus.has_response():
            response = cedrus.get_next_response()
            
            if response['pressed'] and response['key'] == 2:
                continueRoutine = False
    
    # *image_1* updates
    if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_1.frameNStart = frameN  # exact frame index
        image_1.tStart = t  # local t and not account for scr refresh
        image_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
        image_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_1" ---
for thisComponent in instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "begin_training" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_resp.keys = []
space_resp.rt = []
_space_resp_allKeys = []
begin_training_text.setText(S['begin_training'])
# setup some python lists for storing info about the mouse_continue_13
gotValidClick = False  # until a click is received
press_space_text_12.setText(device_texts['continue'][c])
# keep track of which components have finished
begin_trainingComponents = [space_resp, begin_training_text, mouse_continue_13, press_space_text_12]
for thisComponent in begin_trainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "begin_training" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_resp* updates
    waitOnFlip = False
    if space_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp.frameNStart = frameN  # exact frame index
        space_resp.tStart = t  # local t and not account for scr refresh
        space_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp, 'tStartRefresh')  # time at next scr refresh
        space_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp.status == STARTED and not waitOnFlip:
        theseKeys = space_resp.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_allKeys.extend(theseKeys)
        if len(_space_resp_allKeys):
            space_resp.keys = _space_resp_allKeys[-1].name  # just the last key pressed
            space_resp.rt = _space_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *begin_training_text* updates
    if begin_training_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_training_text.frameNStart = frameN  # exact frame index
        begin_training_text.tStart = t  # local t and not account for scr refresh
        begin_training_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_training_text, 'tStartRefresh')  # time at next scr refresh
        begin_training_text.setAutoDraw(True)
    # *mouse_continue_13* updates
    if mouse_continue_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue_13.frameNStart = frameN  # exact frame index
        mouse_continue_13.tStart = t  # local t and not account for scr refresh
        mouse_continue_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue_13, 'tStartRefresh')  # time at next scr refresh
        mouse_continue_13.status = STARTED
        mouse_continue_13.mouseClock.reset()
        prevButtonState = mouse_continue_13.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue_13.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue_13.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *press_space_text_12* updates
    if press_space_text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_12.frameNStart = frameN  # exact frame index
        press_space_text_12.tStart = t  # local t and not account for scr refresh
        press_space_text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_12, 'tStartRefresh')  # time at next scr refresh
        press_space_text_12.setAutoDraw(True)
    # Run 'Each Frame' code from cedrus_continue_12
    
    # cedrus_continue
    
    # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
    
    if c == 2:
        cedrus.poll_for_response()
        while cedrus.has_response():
            response = cedrus.get_next_response()
            
            if response['pressed'] and response['key'] == 2:
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_trainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "begin_training" ---
for thisComponent in begin_trainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "begin_training" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('training.csv'),
    seed=None, name='training')
thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in training:
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_setup
    
    ###### trial_setup ###### 
    
    hadResponse = False
    
    if trainingDone:
        
        tHandler = trials
        trialNum = tHandler.thisN + len(trials.trialList) * blocks.thisN
        if blocks.thisN == blocks.nReps - 1:
    
            pauseText = f"To już koniec zadania.\n {device_texts['continue'][c]}"
    else:
        tHandler = training
        trialNum = tHandler.thisN
    
    
    # tHandler.addData('food', food)  # zapisuję jedzenie do csv, czemu by nie.
    
    imgFile = IMAGE_FILES[group][stimulus]
    
    # przypadek dla kontrolnego trialu
    if control:
        imgFile = IMAGE_FILES['control']
        
    
    # keep track of which components have finished
    fixationComponents = [cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # --- Prepare to start Routine "actual_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    trial_text.setText(trialText)
    trial_image.setImage(imgFile)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    mouse_resp.x = []
    mouse_resp.y = []
    mouse_resp.leftButton = []
    mouse_resp.midButton = []
    mouse_resp.rightButton = []
    mouse_resp.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from cedrus_resp
    
    timer = core.Clock()
    timer.add(1.6)  # 1.6 s czyli czas od rozpoczęcia routine do momentu pojawienia sie obrazka
    # keep track of which components have finished
    actual_trialComponents = [trial_text, trial_image, key_resp, mouse_resp]
    for thisComponent in actual_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "actual_trial" ---
    while continueRoutine and routineTimer.getTime() < 3.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_text* updates
        if trial_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            trial_text.frameNStart = frameN  # exact frame index
            trial_text.tStart = t  # local t and not account for scr refresh
            trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
            trial_text.setAutoDraw(True)
        if trial_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_text.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                trial_text.tStop = t  # not accounting for scr refresh
                trial_text.frameNStop = frameN  # exact frame index
                trial_text.setAutoDraw(False)
        
        # *trial_image* updates
        if trial_image.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            trial_image.frameNStart = frameN  # exact frame index
            trial_image.tStart = t  # local t and not account for scr refresh
            trial_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
            trial_image.setAutoDraw(True)
        if trial_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_image.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                trial_image.tStop = t  # not accounting for scr refresh
                trial_image.frameNStop = frameN  # exact frame index
                trial_image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','p'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        if mouse_resp.status == NOT_STARTED and t >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
        if mouse_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_resp.tStop = t  # not accounting for scr refresh
                mouse_resp.frameNStop = frameN  # exact frame index
                mouse_resp.status = FINISHED
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_resp.getPos()
                    mouse_resp.x.append(x)
                    mouse_resp.y.append(y)
                    buttons = mouse_resp.getPressed()
                    mouse_resp.leftButton.append(buttons[0])
                    mouse_resp.midButton.append(buttons[1])
                    mouse_resp.rightButton.append(buttons[2])
                    mouse_resp.time.append(mouse_resp.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        # Run 'Each Frame' code from cedrus_resp
        
        # ten kod sprawdza czy dostalismy odpowiedź na cedrusie
        
        if c == 2:
            cedrus.poll_for_response()
            if cedrus.response_queue_size() > 0:
                response = cedrus.get_next_response()
        #        logging.exp(f"Cedrus response: {response} at t={timer.getTime()}. remaining responses in queue = {cedrus.response_queue_size()}")
                if response['pressed']:
                    logging.exp(f"Got a cedrus keypress: {response['key']} at t={timer.getTime()}")
        
                # jeśli minęło już 1.6s to możemy faktycznie akceptować odpowiedzi
                    if timer.getTime() > 0:
                        tHandler.addData('cedrus.keyPressed',response['key'])
                        tHandler.addData('responseTime',timer.getTime())
                
                        # 1 to lewy, 3 to prawy, pozostałe ignorujemy
                        if response['key'] == 1:
                            continueRoutine = False
                            hadResponse = True
                            corrects += corrAns == 'q'
                            tHandler.addData('responseCorrect', int(corrAns == 'q'))
                            cedrus.clear_response_queue()
                            
                        elif response['key'] == 3:
                            continueRoutine = False
                            hadResponse = True
                            corrects += corrAns == 'p'
                            tHandler.addData('responseCorrect', int(corrAns == 'p'))
                            cedrus.clear_response_queue()
                            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in actual_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "actual_trial" ---
    for thisComponent in actual_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    training.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        training.addData('key_resp.rt', key_resp.rt)
    # store data for training (TrialHandler)
    training.addData('mouse_resp.x', mouse_resp.x)
    training.addData('mouse_resp.y', mouse_resp.y)
    training.addData('mouse_resp.leftButton', mouse_resp.leftButton)
    training.addData('mouse_resp.midButton', mouse_resp.midButton)
    training.addData('mouse_resp.rightButton', mouse_resp.rightButton)
    training.addData('mouse_resp.time', mouse_resp.time)
    # Run 'End Routine' code from counter
    
    ###### counter ######
    
    # ten kod liczy poprawne odpowiedzi i zapisuje dane
    
    if not hadResponse:
        # odpowiedzi z klawiatury:
        if key_resp.keys:
            hadResponse = True
            corrects += key_resp.corr
            tHandler.addData('responseCorrect', key_resp.corr)
            tHandler.addData('responseTime',key_resp.rt)
    
        # z myszki:
        elif sum(mouse_resp.getPressed()) == 1:
            hadResponse = True
            tHandler.addData('responseTime', mouse_resp.time[0])
            if corrAns == 'q':
                corrects += mouse_resp.leftButton[0]
                tHandler.addData('responseCorrect', mouse_resp.leftButton[0])
            elif corrAns == 'p':
                corrects += mouse_resp.rightButton[0]
                tHandler.addData('responseCorrect', mouse_resp.rightButton[0])
            
    
    if not hadResponse:
        # brak odpowiedzi
        tHandler.addData('responseCorrect', 99)
        
    print(f"{tHandler.name}#{trialNum} | poprawnych odpowiedzi: {corrects}")
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.100000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'training'


# --- Prepare to start Routine "training_results" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from training_results_code
correctsMessage = f"Poprawnych odpowiedzi:{corrects}/{len(training.trialList)}"
corrects = 0
t = trials
trainingDone = True 
space_resp_13.keys = []
space_resp_13.rt = []
_space_resp_13_allKeys = []
# setup some python lists for storing info about the mouse_continue_12
gotValidClick = False  # until a click is received
# keep track of which components have finished
training_resultsComponents = [results_text_2, space_resp_13, press_space_text_10, mouse_continue_12]
for thisComponent in training_resultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_results" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *results_text_2* updates
    if results_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        results_text_2.frameNStart = frameN  # exact frame index
        results_text_2.tStart = t  # local t and not account for scr refresh
        results_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(results_text_2, 'tStartRefresh')  # time at next scr refresh
        results_text_2.setAutoDraw(True)
    if results_text_2.status == STARTED:  # only update if drawing
        results_text_2.setText(correctsMessage, log=False)
    
    # *space_resp_13* updates
    waitOnFlip = False
    if space_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp_13.frameNStart = frameN  # exact frame index
        space_resp_13.tStart = t  # local t and not account for scr refresh
        space_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_13, 'tStartRefresh')  # time at next scr refresh
        space_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_13_allKeys.extend(theseKeys)
        if len(_space_resp_13_allKeys):
            space_resp_13.keys = _space_resp_13_allKeys[-1].name  # just the last key pressed
            space_resp_13.rt = _space_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_text_10* updates
    if press_space_text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_10.frameNStart = frameN  # exact frame index
        press_space_text_10.tStart = t  # local t and not account for scr refresh
        press_space_text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_10, 'tStartRefresh')  # time at next scr refresh
        press_space_text_10.setAutoDraw(True)
    # *mouse_continue_12* updates
    if mouse_continue_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue_12.frameNStart = frameN  # exact frame index
        mouse_continue_12.tStart = t  # local t and not account for scr refresh
        mouse_continue_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue_12, 'tStartRefresh')  # time at next scr refresh
        mouse_continue_12.status = STARTED
        mouse_continue_12.mouseClock.reset()
        prevButtonState = mouse_continue_12.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue_12.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue_12.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    # Run 'Each Frame' code from cedrus_continue_11
    
    # cedrus_continue
    
    # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
    
    if c == 2:
        cedrus.poll_for_response()
        while cedrus.has_response():
            response = cedrus.get_next_response()
            
            if response['pressed'] and response['key'] == 2:
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_resultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_results" ---
for thisComponent in training_resultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "training_results" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pause_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pause_text_2.setText(S['begin_blocks'])
space_resp_12.keys = []
space_resp_12.rt = []
_space_resp_12_allKeys = []
# setup some python lists for storing info about the mouse_continue_9
gotValidClick = False  # until a click is received
press_space_text_11.setText(device_texts['continue'][c])
# keep track of which components have finished
pause_1Components = [pause_text_2, space_resp_12, mouse_continue_9, press_space_text_11]
for thisComponent in pause_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pause_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pause_text_2* updates
    if pause_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_text_2.frameNStart = frameN  # exact frame index
        pause_text_2.tStart = t  # local t and not account for scr refresh
        pause_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_text_2, 'tStartRefresh')  # time at next scr refresh
        pause_text_2.setAutoDraw(True)
    
    # *space_resp_12* updates
    waitOnFlip = False
    if space_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp_12.frameNStart = frameN  # exact frame index
        space_resp_12.tStart = t  # local t and not account for scr refresh
        space_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_12, 'tStartRefresh')  # time at next scr refresh
        space_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_12_allKeys.extend(theseKeys)
        if len(_space_resp_12_allKeys):
            space_resp_12.keys = _space_resp_12_allKeys[-1].name  # just the last key pressed
            space_resp_12.rt = _space_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouse_continue_9* updates
    if mouse_continue_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue_9.frameNStart = frameN  # exact frame index
        mouse_continue_9.tStart = t  # local t and not account for scr refresh
        mouse_continue_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue_9, 'tStartRefresh')  # time at next scr refresh
        mouse_continue_9.status = STARTED
        mouse_continue_9.mouseClock.reset()
        prevButtonState = mouse_continue_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *press_space_text_11* updates
    if press_space_text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_11.frameNStart = frameN  # exact frame index
        press_space_text_11.tStart = t  # local t and not account for scr refresh
        press_space_text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_11, 'tStartRefresh')  # time at next scr refresh
        press_space_text_11.setAutoDraw(True)
    # Run 'Each Frame' code from cedrus_continue_8
    
    # cedrus_continue
    
    # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
    
    if c == 2:
        cedrus.poll_for_response()
        while cedrus.has_response():
            response = cedrus.get_next_response()
            
            if response['pressed'] and response['key'] == 2:
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pause_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pause_1" ---
for thisComponent in pause_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "pause_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials2.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trial_setup
        
        ###### trial_setup ###### 
        
        hadResponse = False
        
        if trainingDone:
            
            tHandler = trials
            trialNum = tHandler.thisN + len(trials.trialList) * blocks.thisN
            if blocks.thisN == blocks.nReps - 1:
        
                pauseText = f"To już koniec zadania.\n {device_texts['continue'][c]}"
        else:
            tHandler = training
            trialNum = tHandler.thisN
        
        
        # tHandler.addData('food', food)  # zapisuję jedzenie do csv, czemu by nie.
        
        imgFile = IMAGE_FILES[group][stimulus]
        
        # przypadek dla kontrolnego trialu
        if control:
            imgFile = IMAGE_FILES['control']
            
        
        # keep track of which components have finished
        fixationComponents = [cross]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 0.4:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.400000)
        
        # --- Prepare to start Routine "actual_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        trial_text.setText(trialText)
        trial_image.setImage(imgFile)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # setup some python lists for storing info about the mouse_resp
        mouse_resp.x = []
        mouse_resp.y = []
        mouse_resp.leftButton = []
        mouse_resp.midButton = []
        mouse_resp.rightButton = []
        mouse_resp.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from cedrus_resp
        
        timer = core.Clock()
        timer.add(1.6)  # 1.6 s czyli czas od rozpoczęcia routine do momentu pojawienia sie obrazka
        # keep track of which components have finished
        actual_trialComponents = [trial_text, trial_image, key_resp, mouse_resp]
        for thisComponent in actual_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "actual_trial" ---
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_text* updates
            if trial_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                trial_text.frameNStart = frameN  # exact frame index
                trial_text.tStart = t  # local t and not account for scr refresh
                trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
                trial_text.setAutoDraw(True)
            if trial_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_text.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_text.tStop = t  # not accounting for scr refresh
                    trial_text.frameNStop = frameN  # exact frame index
                    trial_text.setAutoDraw(False)
            
            # *trial_image* updates
            if trial_image.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                trial_image.frameNStart = frameN  # exact frame index
                trial_image.tStart = t  # local t and not account for scr refresh
                trial_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
                trial_image.setAutoDraw(True)
            if trial_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_image.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_image.tStop = t  # not accounting for scr refresh
                    trial_image.frameNStop = frameN  # exact frame index
                    trial_image.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['q','p'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_resp* updates
            if mouse_resp.status == NOT_STARTED and t >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp.frameNStart = frameN  # exact frame index
                mouse_resp.tStart = t  # local t and not account for scr refresh
                mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
                mouse_resp.status = STARTED
                mouse_resp.mouseClock.reset()
                prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
            if mouse_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse_resp.tStop = t  # not accounting for scr refresh
                    mouse_resp.frameNStop = frameN  # exact frame index
                    mouse_resp.status = FINISHED
            if mouse_resp.status == STARTED:  # only update if started and not finished!
                buttons = mouse_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouse_resp.getPos()
                        mouse_resp.x.append(x)
                        mouse_resp.y.append(y)
                        buttons = mouse_resp.getPressed()
                        mouse_resp.leftButton.append(buttons[0])
                        mouse_resp.midButton.append(buttons[1])
                        mouse_resp.rightButton.append(buttons[2])
                        mouse_resp.time.append(mouse_resp.mouseClock.getTime())
                        
                        continueRoutine = False  # abort routine on response
            # Run 'Each Frame' code from cedrus_resp
            
            # ten kod sprawdza czy dostalismy odpowiedź na cedrusie
            
            if c == 2:
                cedrus.poll_for_response()
                if cedrus.response_queue_size() > 0:
                    response = cedrus.get_next_response()
            #        logging.exp(f"Cedrus response: {response} at t={timer.getTime()}. remaining responses in queue = {cedrus.response_queue_size()}")
                    if response['pressed']:
                        logging.exp(f"Got a cedrus keypress: {response['key']} at t={timer.getTime()}")
            
                    # jeśli minęło już 1.6s to możemy faktycznie akceptować odpowiedzi
                        if timer.getTime() > 0:
                            tHandler.addData('cedrus.keyPressed',response['key'])
                            tHandler.addData('responseTime',timer.getTime())
                    
                            # 1 to lewy, 3 to prawy, pozostałe ignorujemy
                            if response['key'] == 1:
                                continueRoutine = False
                                hadResponse = True
                                corrects += corrAns == 'q'
                                tHandler.addData('responseCorrect', int(corrAns == 'q'))
                                cedrus.clear_response_queue()
                                
                            elif response['key'] == 3:
                                continueRoutine = False
                                hadResponse = True
                                corrects += corrAns == 'p'
                                tHandler.addData('responseCorrect', int(corrAns == 'p'))
                                cedrus.clear_response_queue()
                                
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in actual_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "actual_trial" ---
        for thisComponent in actual_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # store data for trials (TrialHandler)
        trials.addData('mouse_resp.x', mouse_resp.x)
        trials.addData('mouse_resp.y', mouse_resp.y)
        trials.addData('mouse_resp.leftButton', mouse_resp.leftButton)
        trials.addData('mouse_resp.midButton', mouse_resp.midButton)
        trials.addData('mouse_resp.rightButton', mouse_resp.rightButton)
        trials.addData('mouse_resp.time', mouse_resp.time)
        # Run 'End Routine' code from counter
        
        ###### counter ######
        
        # ten kod liczy poprawne odpowiedzi i zapisuje dane
        
        if not hadResponse:
            # odpowiedzi z klawiatury:
            if key_resp.keys:
                hadResponse = True
                corrects += key_resp.corr
                tHandler.addData('responseCorrect', key_resp.corr)
                tHandler.addData('responseTime',key_resp.rt)
        
            # z myszki:
            elif sum(mouse_resp.getPressed()) == 1:
                hadResponse = True
                tHandler.addData('responseTime', mouse_resp.time[0])
                if corrAns == 'q':
                    corrects += mouse_resp.leftButton[0]
                    tHandler.addData('responseCorrect', mouse_resp.leftButton[0])
                elif corrAns == 'p':
                    corrects += mouse_resp.rightButton[0]
                    tHandler.addData('responseCorrect', mouse_resp.rightButton[0])
                
        
        if not hadResponse:
            # brak odpowiedzi
            tHandler.addData('responseCorrect', 99)
            
        print(f"{tHandler.name}#{trialNum} | poprawnych odpowiedzi: {corrects}")
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # --- Prepare to start Routine "pause_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    pause_text.setText(pauseText)
    space_resp_11.keys = []
    space_resp_11.rt = []
    _space_resp_11_allKeys = []
    # setup some python lists for storing info about the mouse_continue_8
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pause_2Components = [pause_text, space_resp_11, mouse_continue_8]
    for thisComponent in pause_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_text* updates
        if pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pause_text.frameNStart = frameN  # exact frame index
            pause_text.tStart = t  # local t and not account for scr refresh
            pause_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pause_text, 'tStartRefresh')  # time at next scr refresh
            pause_text.setAutoDraw(True)
        
        # *space_resp_11* updates
        waitOnFlip = False
        if space_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_resp_11.frameNStart = frameN  # exact frame index
            space_resp_11.tStart = t  # local t and not account for scr refresh
            space_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_resp_11, 'tStartRefresh')  # time at next scr refresh
            space_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = space_resp_11.getKeys(keyList=['space'], waitRelease=False)
            _space_resp_11_allKeys.extend(theseKeys)
            if len(_space_resp_11_allKeys):
                space_resp_11.keys = _space_resp_11_allKeys[-1].name  # just the last key pressed
                space_resp_11.rt = _space_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *mouse_continue_8* updates
        if mouse_continue_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_continue_8.frameNStart = frameN  # exact frame index
            mouse_continue_8.tStart = t  # local t and not account for scr refresh
            mouse_continue_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_continue_8, 'tStartRefresh')  # time at next scr refresh
            mouse_continue_8.status = STARTED
            mouse_continue_8.mouseClock.reset()
            prevButtonState = mouse_continue_8.getPressed()  # if button is down already this ISN'T a new click
        if mouse_continue_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_continue_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # abort routine on response        # Run 'Each Frame' code from cedrus_continue_7
        
        # cedrus_continue
        
        # kod dzięki któremu można przeklikiwać slajdy środkowym przyciskiem cedrusa
        
        if c == 2:
            cedrus.poll_for_response()
            while cedrus.has_response():
                response = cedrus.get_next_response()
                
                if response['pressed'] and response['key'] == 2:
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_2" ---
    for thisComponent in pause_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for blocks (TrialHandler)
    # the Routine "pause_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 4 repeats of 'blocks'


# --- Prepare to start Routine "results" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from results_code
import random

resultsMessage = f"Twój wynik to: {random.randint(10)}"
space_resp_10.keys = []
space_resp_10.rt = []
_space_resp_10_allKeys = []
# setup some python lists for storing info about the mouse_continue_4
gotValidClick = False  # until a click is received
# keep track of which components have finished
resultsComponents = [results_text, space_resp_10, press_space_text_9, mouse_continue_4]
for thisComponent in resultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "results" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *results_text* updates
    if results_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        results_text.frameNStart = frameN  # exact frame index
        results_text.tStart = t  # local t and not account for scr refresh
        results_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(results_text, 'tStartRefresh')  # time at next scr refresh
        results_text.setAutoDraw(True)
    if results_text.status == STARTED:  # only update if drawing
        results_text.setText(resultsMessage, log=False)
    
    # *space_resp_10* updates
    waitOnFlip = False
    if space_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp_10.frameNStart = frameN  # exact frame index
        space_resp_10.tStart = t  # local t and not account for scr refresh
        space_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_10, 'tStartRefresh')  # time at next scr refresh
        space_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_10_allKeys.extend(theseKeys)
        if len(_space_resp_10_allKeys):
            space_resp_10.keys = _space_resp_10_allKeys[-1].name  # just the last key pressed
            space_resp_10.rt = _space_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *press_space_text_9* updates
    if press_space_text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space_text_9.frameNStart = frameN  # exact frame index
        press_space_text_9.tStart = t  # local t and not account for scr refresh
        press_space_text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space_text_9, 'tStartRefresh')  # time at next scr refresh
        press_space_text_9.setAutoDraw(True)
    # *mouse_continue_4* updates
    if mouse_continue_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_continue_4.frameNStart = frameN  # exact frame index
        mouse_continue_4.tStart = t  # local t and not account for scr refresh
        mouse_continue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_continue_4, 'tStartRefresh')  # time at next scr refresh
        mouse_continue_4.status = STARTED
        mouse_continue_4.mouseClock.reset()
        prevButtonState = mouse_continue_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_continue_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_continue_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "results" ---
for thisComponent in resultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "results" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
