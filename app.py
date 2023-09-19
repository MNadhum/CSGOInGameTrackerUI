import PySimpleGUI as sg
import requests
import PIL.Image
import os

#
# -----------  GET USER IMAGE, PRE-LOAD ALL RANK IMAGES, AND FACEIT LEVELS -------------------
imagePath = "assets/" + "0" + "_profile.jpg"
url = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/d5/d541f3f783d166f2af9c237d2087da6170c8baff_full.jpg"
with open(imagePath, "wb") as f:
    f.write(requests.get(url).content)
im = PIL.Image.open("assets/0_profile.jpg")
im.save("assets/0_profile.png")


imagePath = "assets/" + "1" + "_profile.jpg"
url = "https://avatars.akamai.steamstatic.com/235e6e10cd66af9a6c42020f8053cf3a32508522_full.jpg"
with open(imagePath, "wb") as f:
    f.write(requests.get(url).content)
im = PIL.Image.open("assets/1_profile.jpg")
im.save("assets/1_profile.png")


playerDict = {0:{"group" : "I", "wr" : "50%", "faceit" : "assets/faceit.png", "rankImage" : "assets/skillgroup_none.png", "profileImage" : "assets/0_profile.png", "name" : "WOW"}, 1:{"group" : "IV","wr" : "12%", "faceit" : "assets/faceit.png", "rankImage" : "assets/skillgroup_none.png", "profileImage" : "assets/1_profile.png", "name" : "WOW"}}

player0Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[0]["rankImage"], size=(100,40), subsample=2, key="p0r"), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[0]["profileImage"], size=(184, 184), key="p0i"), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[0]["name"], key="p0n"), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[0]["faceit"], subsample=6, key="p0f") ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[0]["wr"], font="bold", key="p0w") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[0]["group"], font=("bold", 45), justification="center",key="p0g" ) ,sg.Push()], # Player Group
                ], p=2)
player1Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[1]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[1]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[1]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[1]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[1]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[1]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player2Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[1]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[1]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[1]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[1]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[1]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[1]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player3Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[0]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[0]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[0]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[0]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[0]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[0]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player4Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[1]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[1]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[1]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[1]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[1]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[1]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player5Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[0]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[0]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[0]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[0]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[0]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[0]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player6Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[1]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[1]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[1]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[1]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[1]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[1]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player7Layout = sg.Col([
                [sg.Push(), sg.Image(playerDict[0]["rankImage"], size=(100,40), subsample=2), sg.Push()], # MM Rank
                [sg.Push(),sg.Image(playerDict[0]["profileImage"], size=(184, 184)), sg.Push()], # Profile Image
                [sg.Push(), sg.Text(playerDict[0]["name"]), sg.Push()], # Player name
                [sg.Push(), sg.Image(playerDict[0]["faceit"], subsample=6) ,sg.Push()], # Player FaceIt Level
                [sg.Push(), sg.Text("Win Rate: " + playerDict[0]["wr"], font="bold") ,sg.Push()], # Player Win rate
                [sg.Push(), sg.Text(playerDict[0]["group"], font=("bold", 45), justification="center", ) ,sg.Push()], # Player Group
                ], p=2)
player8Layout = sg.Col([
                [sg.Push(background_color="#0c0f12"), sg.Image(playerDict[1]["rankImage"], size=(100,40), subsample=2, background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # MM Rank
                [sg.Push(background_color="#0c0f12"),sg.Image(playerDict[1]["profileImage"], size=(184, 184), background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Profile Image
                [sg.Push(background_color="#0c0f12"), sg.Text(playerDict[1]["name"], background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Player name
                [sg.Push(background_color="#0c0f12"), sg.Image(playerDict[1]["faceit"], subsample=6, background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player FaceIt Level
                [sg.Push(background_color="#0c0f12"), sg.Text("Win Rate: " + playerDict[1]["wr"], font="bold", background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player Win rate
                [sg.Push(background_color="#0c0f12"), sg.Text(playerDict[1]["group"], font=("bold", 45), justification="center", background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player Group
                ], p=2, background_color="#0c0f12")
player9Layout = sg.Col([
                [sg.Push(background_color="#0c0f12"), sg.Image(playerDict[0]["rankImage"], size=(100,40), subsample=2, background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # MM Rank
                [sg.Push(background_color="#0c0f12"),sg.Image(playerDict[0]["profileImage"], size=(184, 184), background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Profile Image
                [sg.Push(background_color="#0c0f12"), sg.Text(playerDict[0]["name"], background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Player name
                [sg.Push(background_color="#0c0f12"), sg.Image(playerDict[0]["faceit"], subsample=6, background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player FaceIt Level
                [sg.Push(background_color="#0c0f12"), sg.Text("Win Rate: " + playerDict[0]["wr"], font="bold", background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player Win rate
                [sg.Push(background_color="#0c0f12"), sg.Text(playerDict[0]["group"], font=("bold", 45), justification="center", background_color="#0c0f12") ,sg.Push(background_color="#0c0f12")], # Player Group
                ], p=2, background_color="#0c0f12")

tSideLayout = [player0Layout, player1Layout, player2Layout, player3Layout, player4Layout]

ctSideLayout = [player5Layout, player6Layout, player7Layout, player8Layout, player9Layout]

topWindowLayout = [[tSideLayout], [ctSideLayout]]

rightClickMenu = ["", ["Set CS:GO Path", "Check For New Game", "Exit"]]
sg.Window._move_all_windows = True

#background_image = "assets/bg.png"
#background_layout = [[sg.Image(background_image)]]
#bgWindow = sg.Window('Background', background_layout, grab_anywhere=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=rightClickMenu, no_titlebar=True)
topWindow = sg.Window("Top Window", topWindowLayout, finalize=True, background_color="#0c0f12", keep_on_top=True)


path = ""
while True:
    lastUsedWindow, event, values = sg.read_all_windows()
    # lastUsedWindow is whatever window had the event
    # For example, if right click comes from top window, then lastUsedWIndow = topWindow ...

    print(event, values)

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == 'Set CS:GO Path':
        topWindow.keep_on_top_clear()
        #bgWindow.keep_on_top_clear()

        path = sg.popup_get_folder("Setting CS:GO Path", no_window=True, keep_on_top=True, history=True)

        topWindow.keep_on_top_set()

    elif event == 'Check For New Game':
        if path != "":
            dumpNum = -1
            dumpNumString = ""

            for fileName in os.listdir(path):
                # Find the newest condump file
                # console dumps are saved as condumpX.txt with X starting at 000 and going up
                if (fileName.startswith("condump")):
                    thisNum = int(fileName[fileName.find('p') + 1:fileName.find('.')])
                    if (thisNum > dumpNum):
                        dumpNum = thisNum
                        dumpNumString = fileName

            file = path + '/' + dumpNumString
            print(file)
        else:
            topWindow.keep_on_top_clear()
            #bgWindow.keep_on_top_clear()

            sg.popup_ok("Invalid CS:GO path, please set path and try again.", keep_on_top=True, no_titlebar=True, grab_anywhere=True, modal=True)

            topWindow.keep_on_top_set()


topWindow.close()
#bgWindow.close()