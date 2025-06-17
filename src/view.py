import os
from time import sleep
from src.common_classes import FileManager, CommandProcessor
from src.server_manager import ServerManager
  
class View:
    def __init__(self):
        self.fm = FileManager()
        self.cp = CommandProcessor()
        self.f_creds = self.fm.get_credentials_from_file()
        self.sm = ServerManager(self.f_creds, self.cp)

    def __clear(self):
        os.system('cls')
    
    def __wait(self):
        sleep(2)

    def __press_key(self):
        input("Presiona una tecla para salir...")
    
    def main(self):
        while True:
            self.__clear()
            self.check_credential_status()
            self.options()
            option = int(input())
            if option == 1:
                self.add_credentials()
            if option == 2:
                self.delete_credentials()
            if option == 3:
                self.server_path()
            if option == 4:
                break

    def check_credential_status(self):
        self.__clear()
        c_creds = self.sm.get_credentials_in_system()
        print("Estado actual del acceso al servidor...\n")
        if self.sm.has_credentials():
            print(f"Credenciales: {c_creds['DESTINO']} [ASIGNADAS]\n")
        else:
            print('Credenciales: SIN ASIGNAR\n') 

    def options(self):   
        print('Selecciona la opcion a ejecutar:\n'
            '1. Asignar credenciales.\n'
            '2. Borrar credenciales.\n'
            '3. Ir a carpeta.\n'
            '4. Salir.\n'
            )

    def add_credentials(self):
        while True:
            self.__clear()
            if self.sm.has_credentials():
                print('Ya se encuentran asignadas las credenciales en este equipo.\n')
                print('Deseas renovarlas?(Y/N)\n')

                cred_rep = input().upper()

                if cred_rep == 'Y':
                    self.sm.release_creds()
                    print('Credenciales eliminadas...\n')
                    self.sm.add_creds()
                    print('Credenciales agregadas...\n')
                    self.__press_key()
                    break
                elif cred_rep == 'N':
                    break

            if not self.sm.has_credentials():
                self.sm.add_creds()
                self.__wait()
                print('Se han agregado las credenciales...\n')
                self.__press_key()
                break

    def delete_credentials(self):
        self.__clear()
        while True:
            if not self.sm.has_credentials():
                print('Aun no se han asignado credenciales a este equipo.\n')
                self.__press_key()
                break
            else:
                print('Confrima la accion ingresando (Y/N)\n')
                cred_rep = input().upper()
                if cred_rep == 'Y':
                    self.sm.release_creds()
                    print('Credenciales removidas...\n')
                    self.__press_key()
                    break
                elif cred_rep == 'N':
                    break
    
    def server_path(self):
        self.__clear()
        while True:
            if self.sm.has_credentials():
                self.sm.open_server_path()
                break
            else:
                print('No hay credenciales acceder a esta ruta.')
                self.__press_key()
                break