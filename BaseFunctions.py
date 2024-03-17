import os 
import subprocess

class CredentialReadder():
    def __init__(self):
        self.file_directory = os.path.join(os.getcwd(), 'credential.config')
        self.id_base = self.file_manager()
        self.serv = str(self.id_base['SERVER']).strip()
        self.user = str(self.id_base['USER']).strip()
        self.cred = str(self.id_base['PASSWORD']).strip()
    
    def file_manager(self):
        credentials = {}
        if os.path.exists(self.file_directory) and os.path.isfile(self.file_directory):
            try:
                with open(self.file_directory, 'r') as file:
                    for lines in file:
                        try:
                            key, value = lines.strip().split('=')
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
                'SERVER= \n'
                'USER= \n'
                'PASSWORD= '
            )

            self.write_file(self.file_directory, base_file)
    
    def credential_checker(self):
        command = ['cmdkey', '/list']
        server_cred = ''
        output_command = subprocess.getoutput(command).split('\n')
        new_list = [item.strip() for item in output_command if item.strip()]
        for item in new_list:
            if ('Destino:' in item and f'{self.serv}' in item):      
                server_cred = item.split('=')[1]
                break
        if (server_cred == self.serv):
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
        inp_com = ['cmdkey', f'/add:{self.serv}', f'/user:{self.user}', f'/pass:{self.cred}']
        self.command_execution(inp_com)
        
    def release_creds(self):
        inp_com = ['cmdkey', f'/delete:{self.serv}']
        self.command_execution(inp_com)

    def open_server_folder(self):
        string = r'\\'
        server_path = f'{string}{self.serv}'
        command = f'START {server_path}'
        self.command_execution(command)