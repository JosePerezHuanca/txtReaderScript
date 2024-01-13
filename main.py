from cytolk import tolk;
import keyboard;
import wx;
from textReader import Reader;
from soundManager import Sound;
import time;


with tolk.tolk():
    if tolk.has_speech:
        tolk.speak('Listo');
    sound=Sound();
    sound.openSound();
    
    reader=Reader();
    app=wx.App(False);
    keyboard.add_hotkey('alt+shift+o', reader.openFile);
    keyboard.add_hotkey('alt+shift+down', reader.nextLine);
    keyboard.add_hotkey('alt+shift+up', reader.previousLine);
    keyboard.add_hotkey('alt+shift+home', reader.beginText);
    keyboard.add_hotkey('alt+shift+end', reader.endText);
    keyboard.add_hotkey('alt+shift+r', reader.speakCurrentLine);
    keyboard.add_hotkey('alt+shift+c', reader.copyCurrentLine);
    keyboard.add_hotkey('alt+shift+t', reader.speakTitle);
    exitBool=False;
    while not exitBool:
        if keyboard.is_pressed('alt+shift+q'):
            exitBool=True;
            sound.exitSound();
            time.sleep(0.9);
            app.ExitMainLoop();
    app.MainLoop();
