import PySimpleGUI as sg
import Data

def PopulatePlayerLayouts(playersList):
    """
    Uses list of players to populate layouts, each player gets a layout that will be filled with their relevant info.

    :param playersList: list of dicts, each dict contains one player's information
    :return: List of layouts of all the players containing all relevant information to be displayed
    """

    # Players are placed in one of these lists depending on which group they belong to, in order to make it much
    # easier to know which player to display where in the PopulateWindowLayouts function
    layoutList = [[],[],[],[],[]]
    for player in playersList:
        playerLayout = sg.Col([
                [sg.Push(background_color="#0c0f12"), sg.Image(player["rankImage"], subsample=3,
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # MM Rank

                [sg.Push(background_color="#0c0f12"),sg.Image(player["profileImage"],subsample=2,
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Profile Image

                [sg.Push(background_color="#0c0f12"), sg.Text(player["name"], font=(15),
                    background_color="#0c0f12"), sg.Push(background_color="#0c0f12")], # Player Name

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
    Sets up Window object with a layout informing users on how to use software.

    :return: Window object
    """
    # Layout to be displayed before any information is loaded
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
    """
    Uses playerLayouts to populate each row layout with the correct players, based on which group they belong to.

    :param playerLayouts: List of layouts, each player has one layout

    :return: The final layout to be displayed, where players are grouped by who they are queued with
    """

    newLayout = []

    # Each game can have a maximum of 5 Groups, with one of the groups being for solo players, or players whose info.
    # is not known

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

    # Checks which group is being used and adds each player layout to the relevant group layout
    # Not all groups will always be used, which is why it is necessary to see which groups are being used
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
    Main function, runs entire program

    :return: None
    """

    window = CreateWindow()
    csPath = ""

    # Main loop for the software
    while True:
        # Gets data when window is updated
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == 'Set CS:GO Path':
            # Here the user is attempting to set the path to their CS:GO directory, which is where relevant game data
            # is dumped from in-game console
            window.keep_on_top_clear()
            csPath = sg.popup_get_folder("Setting CS:GO Path", no_window=True, keep_on_top=True, history=True)
            window.keep_on_top_set()

            # Saving the CS:GO path so that user doesn't have to set the path everytime software is closed and re-opened
            csPathFile = open("assets/path.txt", "w")
            csPathFile.write(csPath)
            csPathFile.close()
        elif event == 'Check For New Game':
            # User is attempting to "refresh" the software and check for a new game, this requires for csPath to be set
            if csPath == "":
                # Assuming program has been closed and reopened, checks if csPath was previously saved so that user
                # does not need to set it again
                try:
                    csPathFile = open("assets/path.txt", "r")
                    csPath = csPathFile.readlines()[0]
                    csPathFile.close()
                except:
                    pass

            if csPath != "":
                # Load local data
                try:
                    fileName = Data.LoadFileName(csPath)
                    fileData = Data.FindDataInFile(fileName)
                except:
                    window.keep_on_top_clear()
                    sg.popup_ok("Invalid CS:GO path, please set path and try again.", keep_on_top=True,
                                no_titlebar=True, grab_anywhere=True, modal=True)
                    window.keep_on_top_set()

                # Handling API response, populating layouts, and updating window to display information
                try:
                    apiData = Data.APIRequest(fileData)
                except:
                    sg.popup_ok("Error with API, please ensure condump file is not modified.", keep_on_top=True,
                                no_titlebar=True, grab_anywhere=True, modal=True)
                try:
                    playersData = Data.ProcessAPIData(apiData)
                    playerLoadouts = PopulatePlayerLayouts(playersData)
                    newLayout = PopulateWindowLayouts(playerLoadouts)

                    window["preText"].update(value="CS:GO In-Game Tracker")
                    window.extend_layout(window,newLayout)
                    window.maximize()
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