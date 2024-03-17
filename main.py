import os 
import subprocess
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
            try:
                with open(self.file_directory, 'r') as file:
                    for lines in file:
                        try:
                            key, value = lines.strip().split(':')
                        except KeyError as e:
                            print('Se ha detectado un error en el archivo ID_Card.txt\n'
                                  f'{e}'
                            )
                        credentials[key] = value
                        
                return credentials
            except FileNotFoundError as e:
                print('No se ha encontrado el archivo con las credenciales necesarias.\n',
                      'Se ha creado un archivo opcional para el ingreso de las credenciales.\n',
                      f'{e}'                     
                )
        else:
            base_file =(
                'SERVER: \n'
                'USER: \n'
                'PASSWORD: \n'
            )

            self.write_file(self.file_directory, base_file)
    
    def credential_checker(self):
        command = ['cmdkey', '/list']
        server_cred = ''
        output_command = subprocess.getoutput(command).split('\n')
        new_list = [item.strip() for item in output_command if item.strip()]
        for item in new_list:
            if ('Destino:' in item and f'{self.serv_v}' in item):      
                server_cred = item.split('=')[1]
                break
        if (server_cred == self.serv_v):
            return True
        else:
            return False


    def command_execution(self, command):
        try:
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Hubo un error durante la ejecion del comando. {e}')

    def write_file(self, directory, input):
        with open(directory, 'w') as file:
            file.write(input)

    def renew_creds(self):
        inp_com = ['cmdkey', f'/add:{serv}', f'/user:{user}', f'/pass:{cred}']
        acces_data.command_execution(inp_com)
        
    def release_creds(self):
        inp_com = ['cmdkey', f'/delete:{serv}']
        acces_data.command_execution(inp_com)

    def open_server_folder(self):
        string = r'\\'
        server_path = f'{string}{self.serv_v}'
        command = f'START {server_path}'
        self.command_execution(command)

if __name__ == '__main__':
    acces_data = CredentialReadder()
    serv = acces_data.serv_v
    user = acces_data.user_v
    cred = acces_data.cred_v
    cred_checker = acces_data.credential_checker()

    while True:
        print('Estado actual del acceso al servidor...\n')
        if cred_checker == True:
            print('Ya se encuentran asignadas las credenciales en este equipo.\n'
                 f'Credenciales: {serv}\n'
                  'Quieres sustituirlas?(Y/N)\n'
            )
            cred_rep = input()
            while True:
                if cred_rep == 'Y' or cred_rep == 'y':
                    acces_data.release_creds()
                    sleep(1)
                    print('Credenciales removidas...\n')
                    acces_data.renew_creds()
                    sleep(1)
                    print('Credenciales renovadas...\n')
                    sleep(2)
                    acces_data.open_server_folder()
                    sleep(2)
                    break
                elif cred_rep == 'N' or cred_rep == 'n':
                    break
        else:
            print('Credenciales: SIN ASIGNAR\n')    

        print('Selecciona la opcion a ejecutar:\n'
              '1. Asignar credenciales.\n'
              '2. Borrar credenciales.\n'
              '3. Estatus.\n'
              '4. Salir.\n'
        )
        option = input()
        if option == '1':
            acces_data.renew_creds()
            sleep(1)
            print('Se han generado las credenciales...\n')
            acces_data.open_server_folder()
        if option == '2':
            if cred_checker == False:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')
            else:
                acces_data.release_creds()
                sleep(1)
                print('Se han eliminado las credenciales...\n')
        if option == '3':
            if cred_checker == True:
                sleep(1)
                print('Credenciales asignadas.\n')
            else:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')
        if option == '4':
            break