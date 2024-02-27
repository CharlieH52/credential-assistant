import os

from time import sleep
from pyautogui import keyDown, keyUp, hotkey, typewrite

class CredentialReadder():
    def __init__(self):
        self.file_directory = os.path.join(os.getcwd(), 'ID_Card.txt')
        self.id_base = self.file_manager()
        self.serv_v = str(self.id_base['SERVER']).strip()
        self.user_v = str(self.id_base['USER']).strip()
        self.cred_v = str(self.id_base['PASSWORD']).strip()
    
    def file_manager(self):
        credentials = {}
        if os.path.exists(self.file_directory) and os.path.isfile(self.file_directory):
            with open(self.file_directory, 'r') as file:
                for lines in file:
                    key, value = lines.strip().split(':')
                    credentials[key] = value
            return credentials
        else:
            base_file =(
                'SERVER: \n'
                'USER: \n'
                'PASSWORD: \n'
            )

            self.write_file(self.file_directory, base_file)

    def write_file(self, directory, input):
        with open(directory, 'w') as file:
            file.write(input)

class KeyFunctions():
    def execute(self):
        hotkey('win', 'r')
        sleep(1)
    
    def key_work(self, option):
        if option == 1:
            keyDown('enter')
            keyUp('enter')
            sleep(2)

        if option == 2:
            keyDown('tab')
            keyUp('tab')
            sleep(1)

        if option == 3:
            keyDown('space')
            keyUp('space')
            sleep(1)
    
    def input_work(self, option):
        if option == 1:
            typewrite(acces_data.serv_v)
            sleep(1)
        
        if option == 2:
            typewrite(acces_data.user_v)
            sleep(1)

        if option == 3:
            typewrite(acces_data.cred_v)
            sleep(1)

    def input_credentials(self):
        self.execute()
        self.input_work(1)
        self.key_work(1)
        self.input_work(2)
        self.key_work(2)
        self.input_work(3)
        self.key_work(2)
        self.key_work(3)
        self.key_work(1)
        sleep(5)

if __name__ == '__main__':
    acces_data = CredentialReadder()
    k_control = KeyFunctions()

    k_control.input_credentials()
    