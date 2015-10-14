from panda3d.core import *

from DistributedNPCToonBase import *
from src.toontown.hood import ZoneUtil
from src.otp.nametag.NametagConstants import *
from src.toontown.quest import QuestChoiceGui
from src.toontown.quest import QuestParser
from src.toontown.quest import MultiTrackChoiceGui
from src.toontown.toonbase import TTLocalizer


SPAMMING = 1
DOUBLE_ENTRY = 2

class DistributedSmartNPC(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.accept('chatUpdate', self.chatUpdate)

    def disable(self):
        self.ignoreAll()
        DistributedNPCToonBase.disable(self)

    def delayDelete(self):
        DistributedNPCToonBase.delayDelete(self)
        self.disable()

    def handleCollisionSphereEnter(self, collEntry):
        self.sendUpdate('avatarEnter', [])

    def chatUpdate(self, message, chatFlags):
        self.sendUpdate('talkMessage', [base.localAvatar.doId, message])

    def greet(self, npcId, avId):
        if avId in base.cr.doId2do:
            avName = base.cr.doId2do.get(avId).getName()
            self.setChatAbsolute('Hello, %s' % avName + '!', CFSpeech | CFTimeout)

    def dismiss(self, avId, statusCode):
        if avId in base.cr.doId2do:
            avName = base.cr.doId2do.get(avId).getName()
            if statusCode == SPAMMING:
                self.setChatAbsolute('Slow down there, %s' % avName + '. I can\'t even understand you!', CFSpeech | CFTimeout)
            elif statusCode == DOUBLE_ENTRY:
                self.setChatAbsolute('Well hey there %s' % avName + ', didn\'t we JUST talk?', CFSpeech | CFTimeout)

    def respond(self, npcId, message, avId):
        try:
            name = base.cr.doId2do.get(avId).getName()
            self.setChatAbsolute(message, CFSpeech | CFTimeout)
        except:
            print 'Responding to non-available character!'
