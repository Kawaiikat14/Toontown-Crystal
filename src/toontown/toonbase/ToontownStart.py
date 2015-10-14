#!/usr/bin/env python2
import __builtin__

__builtin__.process = 'client'

import sys, os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../dependencies"
        )
    )
)

# Temporary hack patch:
import pandac.PandaModules
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
from direct.extensions_native import HTTPChannel_extensions
from direct.extensions_native import Mat3_extensions
from direct.extensions_native import VBase3_extensions
from direct.extensions_native import VBase4_extensions
from direct.extensions_native import NodePath_extensions


from panda3d.core import loadPrcFile

#Once WX is fixed it'll be re-enabled and NonWX will be disabled

#Please do not re-enable the injector, as we have came to a decision to remove it. At least, temporarily. 


#Added for when injector code detection is added.
######################from src.toontown.cheatdetection import CheatDector
 
if __debug__:
    import sys
    from direct.stdpy import threading

    loadPrcFile('src/dependencies/config/general.prc')
    loadPrcFile('src/dependencies/config/release/dev.prc')

    if os.path.isfile('src/dependencies/config/local.prc'):
        loadPrcFile('src/dependencies/config/local.prc')

    defaultText = ""


from direct.directnotify.DirectNotifyGlobal import directNotify

notify = directNotify.newCategory('ToontownStart')
notify.setInfo(True)

from src.otp.settings.Settings import Settings
from src.otp.otpbase import OTPGlobals

preferencesFilename = ConfigVariableString(
    'preferences-filename',
    'src/user/preferences.json'
).getValue()

notify.info('Reading %s...' % preferencesFilename)

__builtin__.settings = Settings(preferencesFilename)
if 'res' not in settings:
    settings['res'] = (1280, 720)
if 'fullscreen' not in settings:
    settings['fullscreen'] = False
if 'musicVol' not in settings:
    settings['musicVol'] = 1.0
if 'sfxVol' not in settings:
    settings['sfxVol'] = 1.0
if 'loadDisplay' not in settings:
    settings['loadDisplay'] = 'pandagl'
if 'toonChatSounds' not in settings:
    settings['toonChatSounds'] = True
if 'language' not in settings:
    settings['language'] = 'English'
if 'cogInterface' not in settings:
    settings['cogInterface'] = True
if 'speedchatPlus' not in settings:
    settings['speedchatPlus'] = True
if 'trueFriends' not in settings:
    settings['trueFriends'] = True
if 'fov' not in settings:
    settings['fov'] = OTPGlobals.DefaultCameraFov
if 'antialiasing' not in settings:
    settings['antialiasing'] = 0

loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings['res']))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: musicVol', 'audio-master-music-volume %s' % settings['musicVol'])
loadPrcFileData('Settings: sfxVol', 'audio-master-sfx-volume %s' % settings['sfxVol'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])
if settings['antialiasing']:
    loadPrcFileData('Settings: antialiasing',
                    'framebuffer-multisample 1')
    loadPrcFileData('Settings: antialiasing',
                    'multisamples %s' % settings['antialiasing'])
else:
    loadPrcFileData('Settings: antialiasing',
                    'framebuffer-multisample 0')

import time
import sys
import random
import __builtin__
from src.toontown.launcher.ttcyLauncher import ttcyLauncher

__builtin__.launcher = ttcyLauncher()

notify.info('Starting the game...')
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
notify.info('Setting the default font...')
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
import ToonBase
ToonBase.ToonBase()
from panda3d.core import *
if base.win is None:
    notify.error('Unable to open window; aborting.')
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').hide()
logo = OnscreenImage(
    image='phase_3/maps/toontown-logo.png',
    scale=(1 / (4.0/3.0), 1, 1 / (4.0/3.0)),
    pos=backgroundNodePath.find('**/fg').getPos())
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setBin('fixed', 20)
logo.reparentTo(backgroundNodePath)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
import TTLocalizer
if base.musicManagerIsValid:
    music = base.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
    if music:
        music.setLoop(1)
        music.play()
    notify.info('Loading the default GUI sounds...')
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
version = OnscreenText(serverVersion, pos=(-1.3, -0.975), scale=0.06, fg=Vec4(0, 0, 1, 0.6), align=TextNode.ALeft)
version.setPos(0.03,0.03)
version.reparentTo(base.a2dBottomLeft)
from src.toontown.suit import Suit
Suit.loadModels()
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE, 0)
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from src.toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from src.otp.friends import FriendManager
from src.otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun:
    try:
        base.run()
    except SystemExit:
        raise
    except:
        print describeException()
        raise
