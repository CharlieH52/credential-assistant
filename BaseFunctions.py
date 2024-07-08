import os 
import re
import subprocess

# Clase que maneja lo relacionado a las rutas, el manejo de archivos y carpetas
class FileManager:
    def __init__(self):
        self.config_path = os.path.join(os.getcwd(), "credential.config")
        self.srv_creds = self._dictionary_cred()

    def validate_config(self):
        return os.path.exists(self.config_path)
    
    def read_config(self):
        if self.validate_config():
                with open(self.config_path, 'r') as file:
                    return file.read()
        else:
            raise FileNotFoundError(f"No se ha encontrad el archivo {self.config_path}")
    
    def _clean_keys(self):
        key = r"(.*):\s"
        config_file = self.read_config().split('\n')
        lb = [re.search(key, label).group(1) for label in config_file]
        return lb

    def _clean_creds(self):
        cred = r":\s*(.*)$"
        config_file = self.read_config().split('\n')
        data = [re.search(cred, item).group(1) for item in config_file]
        return data
            

    def _dictionary_cred(self):
        keys = self._clean_keys()
        creds = self._clean_creds()
        if len(keys) != len(creds):
            raise ValueError("La cantidad de claves y credenciales no coinciden.")

        cred_dict = {keys[i]: creds[i] for i in range(len(keys))}

        return cred_dict


    def write_config(self):
        if not self.validate_config():
            with open(self.config_path, 'w') as file:
                file.write(
                    "SERVER: \n"
                    "USER: \n"
                    "PASSWORD: "
                    )

class OperativeSystem(FileManager):
    def __init__(self):
        super().__init__()

    def command_execution(self, args):
        subprocess.run(args, shell=True)

    # Establece las credenciales a partir de los atributos de clase.
    def renew_creds(self):
        inp_com = ["cmdkey",
                   f"/add:{self.srv_creds['SERVER']}",
                   f"/user:{self.srv_creds['USER']}",
                   f"/pass:{self.srv_creds['PASSWORD']}"
                   ]
        self.command_execution(inp_com)

    # Ejecuta una linea de comandos para eliminar las credenciales.
    def release_creds(self):
        inp_com = ["cmdkey", f"/delete:{self.srv_creds['SERVER']}"]
        self.command_execution(inp_com)

    def open_server_folder(self):
        string = r'\\'
        server_path = f"{string}{self.srv_creds['SERVER']}"
        command = f"START {server_path}"
        self.command_execution(command)

# Clase que maneja la lectura del diccionario.
class CredentialReader(FileManager):
    def __init__(self):
        super().__init__()
        self.map_obj = f"\\\\{self.srv_creds['SERVER']}\\sis_cuauh\\PRINCIPAL\\MapObjects-v2.4.EXE"
        self.emp_sof = f"\\\\{self.srv_creds['SERVER']}\\sis_cuauh\\PRINCIPAL\\Instalador.Sistemas.EMPRESS_SRV-CUAUHTEMOC3-v4.0.exe"

    def config_creds(self):
        print(self.read_config())
    
    # Lista las credenciales almacenadas y la compara con la ingresada en el archivo .config, para determinar si las credenciales ya existen en el equipo.
    def credential_checker(self):
        server_cred = ''
        output_command = subprocess.getoutput("cmdkey /list").split('\n')
        new_list = [item.strip() for item in output_command if item.strip()]
        for item in new_list:
            if ("Destino:" in item and f"{self.srv_creds['SERVER']}" in item):      
                server_cred = item.split('=')[1]
                break
        if (server_cred == self.srv_creds['SERVER']):
            return True
        else:
            return False

    def empress_instalation(self):
        try:
            subprocess.run(f"START {str(f'{self.emp_sof}')}",
                        shell=True
                        )
        except Exception:
            print("Ocurrio un problema al ejecutar el proceso de instalacion.")