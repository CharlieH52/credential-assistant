from time import sleep
from os import system
from credential import CredentialManager

cr = CredentialManager()

class CLI:    
    def __init__(self):
        self.cred_checker = cr.credential_checker()
    
    def main(self):
        while True:
            print("Estado actual del acceso al servidor...\n")
            if self.cred_checker == True:
                print(f"Credenciales: {cr.server_credentials['SERVER']}\n")
            else:
                print('Credenciales: SIN ASIGNAR\n')    

            print('Selecciona la opcion a ejecutar:\n'
                '1. Asignar credenciales.\n'
                '2. Borrar credenciales.\n'
                '3. Ir a carpeta.\n'
                '4. Instalacion.\n'
                '5. Estatus.\n'
                '6. Salir.\n'
            )

            option = input()

            # Llama a la funcion que establece las credenciales.
            if option == '1':
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
            elif option == '2':
                system('cls')
                if self.cred_checker == False:
                    print('Aun no se han asignado credenciales a este equipo.\n')
                else:
                    cr.release_creds()
                    print('Se han eliminado las credenciales...\n')
            
            # Da acceso a la carpeta del servidor.
            elif option == '3':
                system('cls')
                if self.cred_checker == True:
                    cr.command_execution(f'START {cr.main_folder_path}')
                else:
                    print('No hay credenciales para la instalacion.')

            elif option == '4':
                system('cls')
                print('No se ha implementado ninguin modulo.')


            # Devuelve un mensaje del estado actual de las credenciales al servidor.  
            if option == '5':
                system('cls')
                if self.cred_checker == True:
                    print('Credenciales asignadas.\n')
                else:
                    print('Aun no se han asignado credenciales a este equipo.\n')

            # Sale del programa.
            if option == '6':
                break