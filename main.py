import getpass
import os
from pystyle import *
import vlc

banner = '''

     _       ___       _ __  _       __     
    | |     / (_)___  (_) /_(_)___ _/ /____ 
    | | /| / / / __ \/ / __/ / __ `/ __/ _ |
    | |/ |/ / / / / / / /_/ / /_/ / /_/  __/
    |__/|__/_/_/ /_/_/\__/_/\__,_/\__/\___/ 
                                                                                          
    [1] Windows XP        [4] Windows 8   
    [2] Windows Vista     [5] Windows 10   
    [3] Windows 7         [6] Windows 11                                                                                  

'''

os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

print('\n\n')


main_input = Write.Input("Select OS to 'Winitiate' : ", Colors.yellow_to_red, interval=0)

if main_input == '1':
    p = vlc.MediaPlayer("http://your_mp3_url")
    p.play()
    Write.Print(f"Preparing To Winitiate Windows XP...", Colors.blue_to_green, interval=0)
