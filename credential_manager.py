import subprocess

class CredentialManager:
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