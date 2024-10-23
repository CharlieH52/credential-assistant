import subprocess
import os
import re
from credential import CredentialManager
from constants import *

cr = CredentialManager()

class SoftwareAsistant:
    def __init__(self):
        self.list = []

        self.clean_list()

    def _software_list(self):
        output = subprocess.run(r'dir \\SRV-CUAUHTEMOC3\sis_cuauh\PRINCIPAL /B', capture_output=True, text=True, shell=True)
        software_list = output.stdout.strip().split('\n')
        return software_list
    
    def clean_list(self):
        for i in self._software_list():
            self.list.append(i)


sa = SoftwareAsistant()
for i in sa.list:
    if '.exe' in i or '.EXE' in i:
        print(i)