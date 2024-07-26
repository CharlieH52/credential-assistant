from time import sleep
import subprocess

class OperativeSystem():
    def __init__(self):
        self.server_credentials = {
            'SERVER': r'SRV-CUAUHTEMOC3',
            'USER': r'SRV-CUAUHTEMOC3\U_SISTEMAS',
            'PASSWORD': r'USis.cuauh'
        }
        self.main_folder_path = r'\\\\SRV-CUAUHTEMOC3\sis_cuauh\PRINCIPAL'

    def command_execution(self, args):
        subprocess.run(args, shell=True)

    # Establece las credenciales a partir de los atributos de clase.
    def renew_creds(self):
        inp_com = ["cmdkey",
                   f"/add:{self.server_credentials['SERVER']}",
                   f"/user:{self.server_credentials['USER']}",
                   f"/pass:{self.server_credentials['PASSWORD']}"
                   ]
        self.command_execution(inp_com)

    # Ejecuta una linea de comandos para eliminar las credenciales.
    def release_creds(self):
        inp_com = ["cmdkey", f"/delete:{self.server_credentials['SERVER']}"]
        self.command_execution(inp_com)

    def open_server_folder(self):
        string = r'\\'
        server_path = f"{string}{self.server_credentials['SERVER']}"
        command = f"START {server_path}"
        self.command_execution(command)

# Clase que maneja la lectura del diccionario.
class CredentialReader(OperativeSystem):
    def __init__(self):
        super().__init__()
        self.map_obj = f'{self.main_folder_path}\\MapObjects-v2.4.EXE'
        self.emp_sof = f'{self.main_folder_path}\\Instalador.Sistemas.EMPRESS_SRV-CUAUHTEMOC3-v4.0.exe'
        self.web_view = f'{self.main_folder_path}\\MicrosoftEdgeWebView2-x86.exe'
    
    # Lista las credenciales almacenadas y la compara con la ingresada en el archivo .config, para determinar si las credenciales ya existen en el equipo.
    def credential_checker(self):
        server_cred = ''
        output_command = subprocess.getoutput("cmdkey /list").split('\n')
        new_list = [item.strip() for item in output_command if item.strip()]
        for item in new_list:
            if ("Destino:" in item and f"{self.server_credentials['SERVER']}" in item):      
                server_cred = item.split('=')[1]
                break
        if (server_cred == self.server_credentials['SERVER']):
            return True
        else:
            return False

    def empress_installer(self):
        try:
            subprocess.run(f"START {self.emp_sof}", shell=True)
        except Exception:
            print("Ocurrio un problema al ejecutar el proceso de instalacion.")

    def mapobjects_installer(self):
        try:
            subprocess.run(f"START {self.map_obj}", shell=True)
        except Exception:
            print("Ocurrio un problema al ejecutar el proceso de instalacion.")

    def webview_installer(self):
        try:
            subprocess.run(f"START {self.web_view}", shell=True)
        except Exception:
            print("Ocurrio un problema al ejecutar el proceso de instalacion.")

if __name__ == '__main__':

    cr = CredentialReader()
    op = OperativeSystem()
    
    while True:
        cred_checker = cr.credential_checker()
        print("Estado actual del acceso al servidor...\n")
        if cred_checker == True:
            print(f"Credenciales: {cr.server_credentials['SERVER']}\n")
        else:
            print('Credenciales: SIN ASIGNAR\n')    

        print('Selecciona la opcion a ejecutar:\n'
              '1. Asignar credenciales.\n'
              '2. Borrar credenciales.\n'
              '3. Instalar EMPRESS.\n'
              '4. Instalar MapObjects.\n'
              '5. Instalar WebView.\n'
              '6. Ir a carpeta.\n'
              '7. Estatus.\n'
              '8. Salir.\n'
        )

        option = input()

        # Llama a la funcion que establece las credenciales.
        if option == '1':
                while True:
                    if cred_checker == True:
                        print('Ya se encuentran asignadas las credenciales en este equipo.\n')
                        print('Deseas renovarlas?(Y/N)\n')

                        cred_rep = input().upper()

                        if cred_rep == 'Y':
                            op.release_creds()
        
                            print('Credenciales removidas...\n')
                            op.renew_creds()
        
                            print('Credenciales renovadas...\n')
                            sleep(2)
                            break
                        elif cred_rep == 'N':
                            break
                    if cred_checker == False:
                        op.renew_creds()
                        sleep(2)
                        print('Se han generado las credenciales...\n')
                        break

        # Si las credenciales no han sido establecidas omite la decisión, sino, llama la funcion que elimina las credenciales.
        if option == '2':
            if cred_checker == False:
                print('Aun no se han asignado credenciales a este equipo.\n')
            else:
                op.release_creds()
                print('Se han eliminado las credenciales...\n')

        # Instala EMPRESS unicamente si las credenciales estan instaladas.
        if option == '3':
            if cred_checker == True:
                print('Comenzando instalacion...')
                cr.empress_installer()
            else:
                print('No hay credenciales para la instalacion.')
        
        # Instala MapObjects unicamente si las credenciales estan instaladas.
        if option == '4':
            if cred_checker == True:
                print('Comenzando instalacion...')
                cr.mapobjects_installer()
            else:
                print('No hay credenciales para la instalacion.')
        
        # Instala WebView unicamente si las credenciales estan instaladas.
        if option == '5':
            if cred_checker == True:
                print('Comenzando instalacion...')
                cr.webview_installer()
            else:
                print('No hay credenciales para la instalacion.')
        
        # Da acceso a la carpeta del servidor.
        if option == '6':
            if cred_checker == True:
                op.command_execution(f'START {op.main_folder_path}')
            else:
                print('No hay credenciales para la instalacion.')

        # Devuelve un mensaje del estado actual de las credenciales al servidor.  
        if option == '7':
            if cred_checker == True:
                print('Credenciales asignadas.\n')
            else:
                print('Aun no se han asignado credenciales a este equipo.\n')

        # Sale del programa.
        if option == '8':
            break