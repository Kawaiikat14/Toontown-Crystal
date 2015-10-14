from direct.task.Task import Task
import random

from src.toontown.town import Street


class BRStreet(Street.Street):
    def enter(self, requestStatus):
        Street.Street.enter(self, requestStatus)
        taskMgr.doMethodLater(1, self.__windTask, 'BR-wind')
        self.loader.hood.setFog()

    def exit(self):
        Street.Street.exit(self)
        taskMgr.remove('BR-wind')
        self.loader.hood.setNoFog()

    def __windTask(self, task):
        base.playSfx(random.choice(self.loader.windSound))
        time = random.random() * 8.0 + 1
        taskMgr.doMethodLater(time, self.__windTask, 'BR-wind')
        return Task.done
