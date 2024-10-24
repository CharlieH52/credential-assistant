import subprocess
import os
import re
from credential_manager import CredentialManager
from constants import *

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
        print(self.programs)
        installation_files = [item for item in SOFTWARE if item in self.programs]
        print(installation_files)
        for i in installation_files:
            print(i)
            self.installers.append(i)



sa = SoftwareAsistant()
for i in sa.installers:
    print(f'<<{i}>>')