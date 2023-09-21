import PIL.Image
import requests
import os

API_KEY = os.getenv("API_KEY")
API_ENDPOINT = os.getenv("ENDPOINT")

def LoadFileName(path):
    """
    Looks at given path and loads the newest console dump, in order to retrieve players' uniqueid.

    :param path (string): CSGO filepath in system
    :return: Name of newest condump file
    """

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

    return file

def FindDataInFile(fileName):
    """
    Gathers player's data from the console dump text file.

    :param fileName (string): Name of condump file to extract data from
    :return (str): Player data taken from the condump file to be used in API request
    """

    file = open(fileName, "r", encoding="utf8")
    here = False
    playerData = ""

    for line in file:
        # Checks if current line is the header of the table with player information
        if line == "# userid name uniqueid connected ping loss state rate\n":
            here = True
        if here:
            if line == "#end\n":
                playerData += line
                break
            playerData += line

    file.close()

    return playerData

def ConvertRankToFileName(rank):
    """
    Maps player's rank to the name of the image file correlating to the player's rank.
    :param rank: Player's rank
    :return: Path of image file
    """
    if rank == "unranked":
        rank = "assets/skillgroup_none.png"
    elif rank == "Silver 1":
        rank = "assets/skillgroup_s1.png"
    elif rank == "Silver 2":
        rank = "assets/skillgroup_s2.png"
    elif rank == "Silver 3":
        rank = "assets/skillgroup_s3.png"
    elif rank == "Silver 4":
        rank = "assets/skillgroup_s4.png"
    elif rank == "Silver Elite":
        rank = "assets/skillgroup_se.png"
    elif rank == "Silver Elite Master":
        rank = "assets/skillgroup_sem.png"
    elif rank == "Gold Nova 1":
        rank = "assets/skillgroup_gn1.png"
    elif rank == "Gold Nova 2":
        rank = "assets/skillgroup_gn2.png"
    elif rank == "Gold Nova 3":
        rank = "assets/skillgroup_gn3.png"
    elif rank == "Gold Nova Master":
        rank = "assets/skillgroup_gnm.png"
    elif rank == "Master Guardian 1":
        rank = "assets/skillgroup_mg1.png"
    elif rank == "Master Guardian 2":
        rank = "assets/skillgroup_mg2.png"
    elif rank == "Master Guardian Elite":
        rank = "assets/skillgroup_mge.png"
    elif rank == "Distinguished Master Guardian":
        rank = "assets/skillgroup_dmg.png"
    elif rank == "Legendary Eagle":
        rank = "assets/skillgroup_le.png"
    elif rank == "Legendary Eagle Master":
        rank = "assets/skillgroup_lem.png"
    elif rank == "Supreme Master First Class":
        rank = "assets/skillgroup_smfc.png"
    elif rank == "The Global Elite":
        rank = "assets/skillgroup_ge.png"
    return rank

def GetProfileImage(url, playerNum):
    """
    Player images are received as URLs, this function downloads the image.

    :param url: URL of the player's image
    :param playerNum: The player's local number, used for distinguishing between all the player's images
    :return: Path to the players' image file
    """
    imagePathJPG = "assets/" + str(playerNum) + "_profile.jpg"
    with open(imagePathJPG, "wb") as f:
        f.write(requests.get(url).content)
    im = PIL.Image.open(imagePathJPG)
    imagePathPNG = imagePathJPG[:-3] + "png"
    im.save(imagePathPNG)

    return imagePathPNG

def APIRequest(sendingData):
    """
    Handles API request with back end.

    :param sendingData: Data to be sent to the API (retrieved from condump file)
    :return: List of dictionaries, each dictionary containing a player's data
    """

    requestHeaders = {"Content-Type" : "text/plain", "x-api-key" : API_KEY}

    request = requests.get(API_ENDPOINT, headers=requestHeaders,data=sendingData.encode("utf-8"), timeout=90)
    apiResponse = request.json()
    playersList = []
    for player in apiResponse.values():
        playersList.append(player)

    return playersList

def ProcessAPIData(playerList):
    """
    Processes the data from the API and keeps relevant information.

    :param playerList: List of player dictionaries
    :return: List of new player dictionaries, which contain required to display relevant information
    """
    groups = [[],[],[],[]]
    playerNum = 0
    retList = []
    for player in playerList:
        newPlayer = {}
        newPlayer["name"] = player["name"]
        newPlayer["winRate"] = round(player["winRate"] * 100)
        newPlayer["faceIT"] = "assets/f0.png"

        if player["faceIT"] != -1:
            newPlayer["faceIT"] = "assets/f" + str(player["faceIT"]) + ".png"

        newPlayer["rankImage"] = ConvertRankToFileName(player["rank"])
        newPlayer["profileImage"] = GetProfileImage(player["avatar"], playerNum)

        # Assigns each player a group based on who they are queued with
        queuedWithList = list(player["queuedWith"].items())
        newPlayer["group"] = -1
        if len(queuedWithList) != 0:
            for friend in queuedWithList:
                if str(friend[1]) in groups[0]:
                    newPlayer["group"] = 1
                    break
                elif str(friend[1]) in groups[1]:
                    newPlayer["group"] = 2
                    break
                elif str(friend[1]) in groups[2]:
                    newPlayer["group"] = 3
                    break
                elif str(friend[1]) in groups[3]:
                    newPlayer["group"] = 4
                    break
            if newPlayer["group"] == -1:
                if len(groups[0]) == 0:
                    groups[0].append(str(player["steamID"]))
                    newPlayer["group"] = 1
                elif len(groups[1]) == 0:
                    groups[1].append(str(player["steamID"]))
                    newPlayer["group"] = 2
                elif len(groups[2]) == 0:
                    groups[2].append(str(player["steamID"]))
                    newPlayer["group"] = 3
                else:
                    groups[3].append(str(player["steamID"]))
                    newPlayer["group"] = 4
        else:
            newPlayer["group"] = 0

        retList.append(newPlayer)
        playerNum += 1

    return retList

def CleanUpFiles():
    """
    Cleans up files that were downloaded for displaying purposes (player images).

    :return: None
    """
    for fileName in os.listdir("assets/"):
        if (fileName.endswith("_profile.png")) or (fileName.endswith("_profile.jpg")):
            os.remove(("assets/" + str(fileName)))