from time import sleep
from BaseFunctions import CredentialReader, OperativeSystem
cr = CredentialReader()
op = OperativeSystem()

if __name__ == '__main__':
    while True:
        cred_checker = cr.credential_checker()
        print("Estado actual del acceso al servidor...\n")
        if cred_checker == True:
            print(f"Credenciales: {cr.srv_creds['SERVER']}\n")
        else:
            print('Credenciales: SIN ASIGNAR\n')    

        print('Selecciona la opcion a ejecutar:\n'
              '1. Asignar credenciales.\n'
              '2. Borrar credenciales.\n'
              '3. Instalar EMPRESS.\n'
              '4. Instalar MapObjects.\n'
              '5. Instalar WebView.\n'
              '6. Ir a carpeta.\n'
              '7. Estatus.\n'
              '8. Salir.\n'
        )

        option = input()

        # Llama a la funcion que establece las credenciales.
        if option == '1':
                while True:
                    if cred_checker == True:
                        print('Ya se encuentran asignadas las credenciales en este equipo.\n')
                        print('Deseas renovarlas?(Y/N)\n')

                        cred_rep = input().upper()

                        if cred_rep == 'Y':
                            op.release_creds()
                            sleep(1)
                            print('Credenciales removidas...\n')
                            op.renew_creds()
                            sleep(1)
                            print('Credenciales renovadas...\n')
                            sleep(2)
                            break
                        elif cred_rep == 'N':
                            break
                    if cred_checker == False:
                        op.renew_creds()
                        sleep(2)
                        print('Se han generado las credenciales...\n')
                        break

        # Si las credenciales no han sido establecidas omite la decisión, sino, llama la funcion que elimina las credenciales.
        if option == '2':
            if cred_checker == False:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')
            else:
                op.release_creds()
                sleep(1)
                print('Se han eliminado las credenciales...\n')

        # Instala EMPRESS unicamente si las credenciales estan instaladas.
        if option == '3':
            if cred_checker == True:
                print('Comenzando instalacion...')
                sleep(1)
                cr.empress_instalation()
            else:
                sleep(1)
                print('No hay credenciales para la instalacion.')

        # Devuelve un mensaje del estado actual de las credenciales al servidor.  
        if option == '7':
            if cred_checker == True:
                sleep(1)
                print('Credenciales asignadas.\n')
            else:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')

        # Sale del programa.
        if option == '8':
            break