import pygame;

class Sound:
    pygame.mixer.init();
    def openSound(self):
        sound=pygame.mixer.Sound('sound/open.ogg');
        sound.play();

    def limitSound(self):
        sound=pygame.mixer.Sound('sound/limit.ogg');
        sound.play();

    def openFileSound(self):
        sound=pygame.mixer.Sound('sound/openFile.ogg');
        sound.play();

    def exitSound(self):
        sound=pygame.mixer.Sound('sound/close.ogg');
        sound.play();
