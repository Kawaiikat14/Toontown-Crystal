from direct.directnotify import DirectNotifyGlobal
from src.toontown.parties.DistributedPartyDanceActivityBaseAI import DistributedPartyDanceActivityBaseAI

class DistributedPartyValentineDance20ActivityAI(DistributedPartyDanceActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyValentineDance20ActivityAI")
