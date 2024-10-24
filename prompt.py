from time import sleep
from os import system
from credential_manager import CredentialManager

cr = CredentialManager()

class CLI:    
    def __init__(self):
        self.cred_checker = cr.credential_checker()

    def cred_status(self):
        system('cls')
        print("Estado actual del acceso al servidor...\n")
        if self.cred_checker == True:
            print(f"Credenciales: {cr.server_credentials['SERVER']} [ASIGNADAS]\n")
        else:
            print('Credenciales: SIN ASIGNAR\n') 

    def main(self):   
        print('Selecciona la opcion a ejecutar:\n'
            '1. Asignar credenciales.\n'
            '2. Borrar credenciales.\n'
            '3. Ir a carpeta.\n'
            '4. Instalacion.\n'
            '5. Estatus.\n'
            '6. Salir.\n'
        )

    def decision_Y_N(self):
        pass

    def add_credentials(self):
        system('cls')
        while True:
            if self.cred_checker == True:
                print('Ya se encuentran asignadas las credenciales en este equipo.\n')
                print('Deseas renovarlas?(Y/N)\n')

                cred_rep = input().upper()

                if cred_rep == 'Y':
                    cr.release_creds()

                    print('Credenciales removidas...\n')
                    cr.renew_creds()

                    print('Credenciales renovadas...\n')
                    sleep(2)
                    break
                elif cred_rep == 'N':
                    break

            if self.cred_checker == False:
                cr.renew_creds()
                sleep(2)
                print('Se han generado las credenciales...\n')
                break

    def delete_credentials(self):
        system('cls')
        while True:
            if self.cred_checker == False:
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
    
    def server_path(self):
        system('cls')
        while True:
            if self.cred_checker == True:
                cr.command_execution(f'START {cr.main_folder_path}')
                break
            else:
                print('No hay credenciales para la instalacion.')
                break
    
    def instalation_checker(self):
        pass

    def software_list(self):
        while True:
            print('Selecciona el programa a instalar')