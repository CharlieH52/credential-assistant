from src.consts.constants import *
from src.mainFunctions import CredentialManager

cr = CredentialManager()

def delete_credentials():
    CLEAR
    while True:
        if STATUS == False:
            print('Aun no se han asignado credenciales a este equipo.\n')
            break
        else:
            print('Confrima la accion ingresando (Y/N)\n')

            cred_rep = input().upper()

            if cred_rep == 'Y':
                cr.release_creds()
                print('Credenciales removidas...\n')
                break
            elif cred_rep == 'N':
                break