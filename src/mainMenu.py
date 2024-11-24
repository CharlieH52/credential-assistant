from src.consts.constants import *
from src.mainFunctions import CredentialManager

cr = CredentialManager()

def cred_status():
    CLEAR
    print("Estado actual del acceso al servidor...\n")
    if STATUS == True:
        print(f"Credenciales: {SERVER} [ASIGNADAS]\n")
    else:
        print('Credenciales: SIN ASIGNAR\n') 

def main():   
    print('Selecciona la opcion a ejecutar:\n'
        '1. Asignar credenciales.\n'
        '2. Borrar credenciales.\n'
        '3. Ir a carpeta.\n'
        '4. Instalacion.\n'
        '5. Estatus.\n'
        '6. Salir.\n'
    )

    
    
    
    
    

    