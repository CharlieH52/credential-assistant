from src.consts.constants import *
from src.mainFunctions import CredentialManager

cr = CredentialManager()

def server_path():
    CLEAR
    while True:
        if STATUS == True:
            cr.command_execution(f'START {TARGET_PATH}')
            break
        else:
            print('No hay credenciales para la instalacion.')
            break