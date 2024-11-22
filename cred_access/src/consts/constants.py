from os import system
from time import sleep
from cred_access.src.mainFunctions import CredentialManager

cr = CredentialManager()

STATUS = cr.credential_checker()

CLEAR = system('cls')

WAIT = sleep(2)

SOFTWARE = [ 'EMPRESS', 'MapObjects', 'WebView']

# ACGE_ChatGPT.exe
# DS_EnlaceSE.exe
# DS_SistemasEmpress.exe
# Instalador Sistema EMPRESS SRV-CUAUHTEMOC3 v4.0.exe
# Instalador Sistema EMPRESS SRV-CUAUHTEMOC3 v5.0.exe   <<< Evaluar versionado
# MapObjects-v2.4.EXE                                   <<< Importante
# MicrosoftEdgeWebView2-x86.exe                         <<< Con la actualización 11-2024 se requiere para el uso de chatgpt
# Utiler¡as_SRV-CUAUHTEMOC3_SDAC-DS_v1.0.exe
# Utiler¡as_SRV-CUAUHTEMOC3_SDAC-DS_v3.0.exe