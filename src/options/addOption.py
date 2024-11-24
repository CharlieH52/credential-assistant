from src.consts.constants import *

def add_credentials():
    CLEAR
    while True:
        if STATUS == True:
            print('Ya se encuentran asignadas las credenciales en este equipo.\n')
            print('Deseas renovarlas?(Y/N)\n')

            cred_rep = input().upper()

            if cred_rep == 'Y':
                cr.release_creds()

                print('Credenciales removidas...\n')
                cr.renew_creds()

                print('Credenciales renovadas...\n')
                WAIT
                break
            elif cred_rep == 'N':
                break

        if STATUS == False:
            cr.renew_creds()
            WAIT
            print('Se han generado las credenciales...\n')
            break