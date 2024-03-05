import os 
import subprocess

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

    def command_execution(self, command):
        try:
            command = subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Hubo un error durante la ejecion del comando. {e}')

    def write_file(self, directory, input):
        with open(directory, 'w') as file:
            file.write(input)

if __name__ == '__main__':
    acces_data = CredentialReadder()
    serv = acces_data.serv_v
    user = acces_data.user_v
    cred = acces_data.cred_v

    while True:
        print('Selecciona la opcion a ejecutar:\n',
              '1. Asignar credenciales.\n',
              '2. Borrar credenciales.\n',
              '3. Salir'
        )
        option = input()
        if option == '1':
            inp_com = ['cmdkey', f'/add:{serv}', f'/user:{user}', f'/pass:{cred}']
            acces_data.command_execution(inp_com)
        if option == '2':
            inp_com = ['cmdkey', f'/delete:{serv}']
            acces_data.command_execution(inp_com)
        if option == '3':
            break