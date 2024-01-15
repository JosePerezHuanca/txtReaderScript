from cytolk import tolk;
import os;
import wx;
import codecs;
import pyperclip;
from soundManager import Sound;
import time;

class Reader:
    def __init__(self):
        self.textContent=[];
        self.currentItem=0;
        self.fileName=None;
        self.reachedLimit={'start': False, 'end': False};

    sound=Sound();

    def openFile(self):
        dialog=wx.FileDialog(None, 'Habrir', wildcard='Archivos de texto (*.txt)|*.txt|Todos los archivos (*.*)|*.*',style=wx.FD_OPEN);
        try:
            if dialog.ShowModal()== wx.ID_OK:
                filePat=dialog.GetPath();
                if os.path.exists(filePat):
                    with codecs.open(filePat,'r',encoding='utf-8') as txtFile:
                        content=[line.strip() for line in txtFile.readlines()];
                        self.textContent.clear();
                        self.textContent.extend(content);
                        self.sound.openFileSound();
                        self.fileName=os.path.basename(filePat);
                        self.currentItem=0;
                else:
                    wx.MessageBox('Ese archivo no existe', 'Error', style=wx.OK | wx.ICON_ERROR);
        except Exception as e:
            wx.MessageBox(str(e));
        finally:
            dialog.Destroy();

    def speakCurrentLine(self):
        if not self.textContent:
            time.sleep(0.1);
            tolk.speak('Primero selecciona un archivo');
        else:
            time.sleep(0.1);
            tolk.speak(self.textContent[self.currentItem]);

    def speakTitle(self):
        if not self.fileName:
            time.sleep(0.1)
            tolk.speak('Primero selecciona un archivo');
        else:
            time.sleep(0.1);
            tolk.speak(self.fileName);

    def nextLine(self):
        self.currentItem=min(len(self.textContent)-1, self.currentItem+1);
        if self.currentItem== len(self.textContent)-1:
            if self.reachedLimit['end']:
                self.sound.limitSound();
                self.speakCurrentLine();
            else:
                self.reachedLimit['end']=True;
                self.speakCurrentLine();
        else:
            self.reachedLimit['start']=False;
            self.speakCurrentLine();

    def previousLine(self):
        self.currentItem=max(0, self.currentItem-1);
        if self.currentItem==0:
            if self.reachedLimit['start']:
                self.sound.limitSound();
                self.speakCurrentLine();
            else:
                self.reachedLimit['start']=True;
                self.speakCurrentLine();
        else:
            self.reachedLimit['end']=False;
            self.speakCurrentLine();

    def beginText(self):
        self.currentItem=0;
        self.speakCurrentLine();

    def endText(self):
        self.currentItem=len(self.textContent)-1;
        self.speakCurrentLine();

    def copyCurrentLine(self):
        if not self.textContent:
            tolk.speak('No hay nada para copiar');
        else:
            pyperclip.copy(self.textContent[self.currentItem]);
            tolk.speak('Copied');
