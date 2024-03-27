import os
import shutil
import subprocess
from time import strftime

class CommonInformation:
    def __init__(self):
        self.acc_name = os.getlogin()

class LogManagerSystem:
    folder_name = 'LOGS'
    
    def __init__(self):
        self.output_path = self.output_route()
        
    def output_route(self):
        logs_directory = os.path.join(os.getcwd(), self.folder_name)
        return logs_directory

    def error_log_print(self, directory, log):
        date = str(strftime('%d-%m-%Y_%H-%M-%S'))
        log_name = f'ERROR_LOG-{date}.log'
        new_directory = os.path.join(directory, log_name)       
        with open(new_directory, 'w') as file:
            file.write(log)

class FileManager:
    def __init__(self):
        self.dictionary = {}
        self.db_path = os.path.join(os.getcwd())

    # Comprueba la existencia del directorio entrante.
    def is_valid_directory(self, in_path):
        return os.path.isdir(in_path)
    
    # Comprueba la existencia del archivo entrante
    def is_valid_file(self, in_file):
        return os.path.isfile(in_file)
    
    # Crea una nueva ruta para el archivo ingresado'
    def new_path(self, path, file):
        return os.path.join(path, file)

    # Ejecuta y divide en lineas la salida de un comando CMD.
    def cmd_command_execute(self, command_line):
        return subprocess.getoutput(command_line).split('\n')

    # Carga y lee un diccionario.
    def dictionary_reader(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for items in file.readlines():
                    key, name = items.strip().split(': ')
                    self.dictionary[key] = name
                return self.dictionary
            
        except FileNotFoundError as e:
            make_log = f'No se ha localizado el archivo diccionario. {e}'
            return make_log

    # Carga y lee los objetos listados en un archivo.
    def list_reader(self, file_path):
        try:
            with open(file_path, 'r') as file:
                bibs = [lines.strip() for lines in file]
                return bibs
        except FileNotFoundError as e:
            make_log = f'No se ha localizado el archivo lista. {e}'
            return make_log

    # Crea un nuevo directorio si no existe en el contexto actual.
    def make_new_directory(self, directory_name):
        try:
            if not self.is_valid_directory(directory_name):
                os.mkdir(directory_name)
                return 'Se ha creado correctamente el directorio.'
        except OSError as e:
            make_log = f'No se pudo crear el directorio {directory_name}. {e}'
            return make_log
        
        return f'El directorio {directory_name} ya existe.'
    
    # Valida y mueve archivos de un directorio a otro.
    def move_input_file(self, file_name, input_path, output_path):
        input_file = self.new_path(input_path, file_name)
        output_file = self.new_path(output_path, file_name)
        if os.path.exists(output_file):
            if not self.is_valid_file(input_file):
                try:
                    shutil.move(input_file, output_path)
                    return f'El archivo {input_file} se ha movido con exito.'
                except shutil.Error as e:
                    make_log = f'Ya existe este archivo en el directorio, se ha omitido su procesamiento. {e}'
                    return make_log
                
            return 'No se ha encontrado el archivo especificado.'
        
        return 'Ya existe el archivo en el directorio de salida.'