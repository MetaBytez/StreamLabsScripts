import clr
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

from SettingsModule import ChatPGSettings

global Settngs
Settngs = None

ScriptName = "ChatPG"
Website = "https://twitch.tv/MetaBytez"
Description = "A MUD Style game, for Twitch Chat"
Creator = "MetaBytez"
Version = "0.0.1"


def Init():
    global Settngs
    scriptPath = os.path.dirname(__file__)
    settingsFile = os.path.join(scriptPath, 'Settings\settings.json')
    Settngs = ChatPGSettings(settingsFile)


def Execute(data):
    pass


def Tick():
    pass


def ReloadSettings(json_data):
    Settngs.Load(json_data)
    Settngs.Save()


def ScriptToggled(state):
    if state:
        Parent.SendStreamMessage('ChatRPG is live!')
