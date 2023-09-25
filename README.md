
# CSGOInGameTrackerUI

This is an application which allows users, with a click of a single button, to receive
information regarding the players in their current CS:GO game. This part of the application handles the client-side 
functionality by collecting local data, contacting API, creating the GUI, and displaying relevant data based
on API response.

## Dependencies

* Libraries: PySimpleGUI, PIL (Python Imaging Library), requests

## How To Use
#### Set Up CS:GO Console
* We will need to set a bind to call the following commands: "clear", "status", "condump"
	* "clear" is used to clear the console of any previous data
	* "status" returns IDs of players in current game
	* "condump" dumps the console output into a txt file, found in the CS:GO path folder
* In order to set a single-key bind, we need to use aliases to run commands so that "condump" doesn't run until "status" has fully returned.
	* Type the following into the console (can replace "p" with preferred key, make sure to keep the quotes):
	    ```
	    alias "+tracker" "clear; status;"
	    alias "-tracker" "condump;"
	    bind "p" "+tracker"
	    ```
#### Run Program
1. Set the CS:GO path using "Game" menu in the toolbar, as shown [here](#menu-settings). By default, the path should be similar to this: 

   ```C:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\csgo```
3. Run the single-key bind in-game so that the "clear", "status", "condump" commands are run
4. Check for New Game using "Game" menu in toolbar, as shown [here](#menu-settings), and program will automatically display data once it has been retrieved, as shown [here](#example-game-output)

## Screenshots
##### Startup Screen
![Startup Screen](https://i.imgur.com/1hSN8ig.png)
##### Menu Settings
![Menu Settings](https://i.imgur.com/rEwKFqd.png)
##### Example Game Output
![Final Display](https://i.imgur.com/QkgP61T.png)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3.0 License - see the LICENSE.txt file for details
