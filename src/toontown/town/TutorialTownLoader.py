import TownLoader
import TTTownLoader
import TutorialStreet
from src.toontown.suit import Suit
from src.toontown.toon import Toon
from src.toontown.hood import ZoneUtil

class TutorialTownLoader(TTTownLoader.TTTownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TTTownLoader.TTTownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = TutorialStreet.TutorialStreet

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadTutorialSuit()
        dnaFile = 'phase_3.5/dna/tutorial_street.pdna'
        self.createHood(dnaFile, loadStorage=0)
        self.alterDictionaries()

    def loadBattleAnims(self):
        Toon.loadTutorialBattleAnims()

    def unloadBattleAnims(self):
        Toon.unloadTutorialBattleAnims()

    def alterDictionaries(self):
        zoneId = ZoneUtil.tutorialDict['exteriors'][0]
        self.nodeDict[zoneId] = self.nodeDict[20001]
        del self.nodeDict[20001]
