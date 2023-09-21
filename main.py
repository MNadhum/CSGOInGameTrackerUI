import PySimpleGUI as sg
import os


import Data
from psgtray import SystemTray

def PopulatePlayerLayouts(playersList):
    """

    :param playersList:
    :return:
    """
    layoutList = [[],[],[],[],[]]
    for player in playersList:
        playerLayout = sg.Col([
                [sg.Push(background_color="#0c0f12"), sg.Image(player["rankImage"], subsample=3,
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # MM Rank

                [sg.Push(background_color="#0c0f12"),sg.Image(player["profileImage"],subsample=2,
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Profile Image

                [sg.Push(background_color="#0c0f12"), sg.Text(player["name"], font=(15),
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Player name

                [sg.Push(background_color="#0c0f12"), sg.Image(player["faceIT"],
                    background_color="#0c0f12", subsample=7) ,sg.Push(background_color="#0c0f12")], # Player FaceIt

                [sg.Push(background_color="#0c0f12"), sg.Text("Win Rate: " + str(player["winRate"]) + "%", font="bold",
                    background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")]], # Player Win rate

            pad=2, background_color="#0c0f12", justification="right")

        if player["group"] == 0:
            layoutList[0].append(playerLayout)
        elif player["group"] == 1:
            layoutList[1].append(playerLayout)
        elif player["group"] == 2:
            layoutList[2].append(playerLayout)
        elif player["group"] == 3:
            layoutList[3].append(playerLayout)
        else:
            layoutList[4].append(playerLayout)

    return layoutList

def CreateWindow():
    """

    :return:
    """
    preLoadLayout = [sg.Push(background_color="#0c0f12"),
                     sg.Text("Please Set CS:GO Path and Check For New Game in \"Game\" Toolbar Setting",
                              font=("bold", 20), justification="center", background_color="#0c0f12", key="preText"),
                     sg.Push(background_color="#0c0f12")]
    menuBarLayout = [["File", "Exit"], ["Game", ["Set CS:GO Path", "Check For New Game"]]]
    menuBar = sg.MenubarCustom(menuBarLayout, bar_background_color="#0c0f12", bar_text_color="white",
                               background_color="#0c0f12", text_color="white",)

    windowLayout = [[menuBar], [preLoadLayout]]
    sg.theme_background_color("#0c0f12")
    myWindow = sg.Window("CS:GO In-Game Tracker", windowLayout, finalize=True, background_color="#0c0f12",
                         icon="assets/icon.ico")

    return myWindow

def PopulateWindowLayouts(playerLayouts):

    newLayout = []

    soloGroupLayout = [sg.Text("Solo/Unknown: ", font=("bold", 20), justification="left",
                               background_color="#0c0f12"), sg.Push(background_color="#0c0f12")]
    IGroupLayout = [sg.Text("I: ", font=("bold", 20), justification="left",
                            background_color="#0c0f12"), sg.Push(background_color="#0c0f12")]
    IIGroupLayout = [sg.Text("II: ", font=("bold", 20), justification="left",
                             background_color="#0c0f12"), sg.Push(background_color="#0c0f12")]
    IIIGroupLayout = [sg.Text("III: ", font=("bold", 20), justification="left",
                              background_color="#0c0f12"), sg.Push(background_color="#0c0f12")]
    IVGroupLayout = [sg.Text("IV: ", font=("bold", 20), justification="left",
                             background_color="#0c0f12"), sg.Push(background_color="#0c0f12")]

    soloEnabled = False
    IEnabled = False
    IIEnabled = False
    IIIEnabled = False
    IVEnabled = False

    for player in playerLayouts[0]:
        soloEnabled = True
        soloGroupLayout.append(player)

    for player in playerLayouts[1]:
        IEnabled = True
        IGroupLayout.append(player)

    for player in playerLayouts[2]:
        IIEnabled = True
        IIGroupLayout.append(player)

    for player in playerLayouts[3]:
        IIIEnabled = True
        IIIGroupLayout.append(player)

    for player in playerLayouts[4]:
        IVEnabled = True
        IVGroupLayout.append(player)

    if soloEnabled:
        newLayout.append(soloGroupLayout)
    if IEnabled:
        newLayout.append(IGroupLayout)
    if IIEnabled:
        newLayout.append(IIGroupLayout)
    if IIIEnabled:
        newLayout.append(IIIGroupLayout)
    if IVEnabled:
        newLayout.append(IVGroupLayout)

    return newLayout

def main():
    """

    :return:
    """

    window = CreateWindow()
    csPath = ""

    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Set CS:GO Path':
            window.keep_on_top_clear()
            csPath = sg.popup_get_folder("Setting CS:GO Path", no_window=True, keep_on_top=True, history=True)
            window.keep_on_top_set()

            csPathFile = open("assets/path.txt", "w")
            csPathFile.write(csPath)
            csPathFile.close()

        elif event == 'Check For New Game':
            if csPath == "":
                try:
                    csPathFile = open("assets/path.txt", "r")
                    csPath = csPathFile.readlines()[0]
                    csPathFile.close()
                except:
                    pass

            if csPath != "":
                try:
                    fileName = Data.LoadFileName(csPath)
                    fileData = Data.FindDataInFile(fileName)
                except:
                    window.keep_on_top_clear()
                    sg.popup_ok("Invalid CS:GO path, please set path and try again.", keep_on_top=True,
                                no_titlebar=True, grab_anywhere=True, modal=True)
                    window.keep_on_top_set()
                apiData = Data.APIRequest(fileData)
                try:
                    playersData = Data.ProcessAPIData(apiData)
                    playerLoadouts = PopulatePlayerLayouts(playersData)
                    newLayout = PopulateWindowLayouts(playerLoadouts)

                    window["preText"].update(value="CS:GO In-Game Tracker")
                    window.extend_layout(window,newLayout)
                    window.refresh()
                except:
                    sg.popup_ok("Unknown Error Occured. Please Try Again.", keep_on_top=True, no_titlebar=True,
                                modal=True)

            else:
                window.keep_on_top_clear()
                sg.popup_ok("Invalid CS:GO path, please set path and try again.",
                            keep_on_top=True, no_titlebar=True, grab_anywhere=True, modal=True)
                window.keep_on_top_set()

    Data.CleanUpFiles()
    window.close()

if __name__ == "__main__":
    main()