import subprocess

from src.consts.constants import *

class CredentialManager:
    def command_execution(self, args):
        subprocess.run(args, shell=True)

    # Establece las credenciales a partir de los atributos de clase.
    def renew_creds(self):
        inp_com = ["cmdkey",
                   f"/add:{SERVER}",
                   f"/user:{USER}",
                   f"/pass:{PASSWORD}"
                   ]
        self.command_execution(inp_com)

    # Ejecuta una linea de comandos para eliminar las credenciales.
    def release_creds(self):
        inp_com = ["cmdkey", f"/delete:{SERVER}"]
        self.command_execution(inp_com)
    
    # Lista las credenciales almacenadas y la compara con la ingresada en el archivo .config, para determinar si las credenciales ya existen en el equipo.
    def credential_checker(self):
        server_cred = ''
        output_command = subprocess.getoutput("cmdkey /list").split('\n')
        new_list = [item.strip() for item in output_command if item.strip()]
        for item in new_list:
            if ("Destino:" in item and f"{SERVER}" in item):      
                server_cred = item.split('=')[1]
                break
        if (server_cred == SERVER):
            return True
        else:
            return False