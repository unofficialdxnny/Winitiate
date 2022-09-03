import getpass
import os
from pystyle import *
import playsound
from time import sleep
from elevate import elevate

elevate()

banner = '''
                    
     _       ___       _ __  _       __     
    | |     / (_)___  (_) /_(_)___ _/ /____ 
    | | /| / / / __ \/ / __/ / __ `/ __/ _ |
    | |/ |/ / / / / / / /_/ / /_/ / /_/  __/
    |__/|__/_/_/ /_/_/\__/_/\__,_/\__/\___/ 
                                                                                          
    Type 'winitiate' for syntax                                                                       

'''

os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

print('\n\n')



while True:
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

    print('\n\n')
    main_input = Write.Input(" Winitiate >>> ", Colors.yellow_to_red, interval=0).lower()
    
    split = main_input.split()

    if main_input == 'winitiate':
        print(Colorate.Color(Colors.red, f'The syntax is "winitiate windows version type"', True))

    elif split[0] == 'winitiate' and split[1] == 'windows' and split[2] == 'xp' and split[3] == 'home':
        print(Colorate.Horizontal(Colors.yellow_to_red, "Preparing to winitiate Windows XP Home...", 1))
        playsound.playsound('./Sounds/XP su.mp3')
        os.system('slmgr/ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 & slmgr /skms s9.us.to & slmgr /ato')
        print(Colorate.Color(Colors.green, f'Windows 7 Home Winitiated Successfully!"', True))

    elif split[0] == 'winitiate' and split[1] == 'windows' and split[2] == 'xp' and split[3] == 'professional':
        print(Colorate.Horizontal(Colors.yellow_to_red, "Preparing to winitiate Windows XP Professional...", 1))
        playsound.playsound('./Sounds/XP su.mp3')
        os.system('slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX & slmgr /skms s9.us.to & slmgr /ato')
        print(Colorate.Color(Colors.green, f'Windows 7 Professional Winitiated Successfully!"', True))


    elif main_input == '':
        print(Colorate.Color(Colors.red, f"Input can't be empty...", True))
        sleep(3)

    else:
        print(Colorate.Color(Colors.red, f'Invalid Syntax type "winitiate" for help', True))
        sleep(3)
