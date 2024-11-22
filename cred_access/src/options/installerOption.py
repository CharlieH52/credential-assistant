import subprocess
from cred_access.src.mainFunctions import CredentialManager
from cred_access.src.consts.constants import *

cr = CredentialManager()


class SoftwareAsistant:
    def __init__(self):
        self.programs = []
        self.installers = []
        
        self._exe_list()
        self._software_list()

    def _exe_list(self):
        output = subprocess.run(r'dir \\SRV-CUAUHTEMOC3\sis_cuauh\PRINCIPAL /B', capture_output=True, text=True, shell=True)
        software_list = output.stdout.strip().split('\n')
        for program in software_list:
            if '.exe' in program or '.EXE' in program:
                 self.programs.append(program)
    
    def _software_list(self):
        for i in SOFTWARE:
            for l in self.programs:
                if i in l:
                    self.installers.append(l)

    def install_option(program):
        subprocess.run(program)

    def instalation_checker(self):
            CLEAR
            print('Modulo no implementado.')
            input()
            pass
    
sa = SoftwareAsistant()
    
def software_list(self):
        CLEAR
        while True:
            print('Selecciona el programa a instalar')
            for i in sa.installers:
                print(i)
            input()
            break