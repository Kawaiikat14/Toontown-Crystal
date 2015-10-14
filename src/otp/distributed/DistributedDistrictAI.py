from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from src.toontown.toonbase import ToontownGlobals

class DistributedDistrictAI(DistributedObjectAI):
    notify = directNotify.newCategory('DistributedDistrictAI')

    name = 'District'
    available = 0

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        doId = self.doId - (self.doId % 100000000 % 1000000)
        self.air.groupManager.shardGroups[doId] = {
            ToontownGlobals.SellbotHQ: ['VP Group', []],
            ToontownGlobals.CashbotHQ: ['CFO Group', []],
            ToontownGlobals.LawbotHQ:  ['CJ Group', []],
            ToontownGlobals.BossbotHQ: ['CEO Group', []],
        }

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def setAvailable(self, available):
        self.available = available

    def d_setAvailable(self, available):
        self.sendUpdate('setAvailable', [available])

    def b_setAvailable(self, available):
        self.setAvailable(available)
        self.d_setAvailable(available)

    def getAvailable(self):
        return self.available
