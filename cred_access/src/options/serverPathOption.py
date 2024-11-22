from cred_access.src.consts.constants import *
from cred_access.src.mainFunctions import CredentialManager

cr = CredentialManager()

def server_path():
        WAIT
        while True:
            if STATUS == True:
                cr.command_execution(f'START {cr.main_folder_path}')
                break
            else:
                print('No hay credenciales para la instalacion.')
                break