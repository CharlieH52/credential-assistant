from time import sleep
from BaseFunctions import CredentialReadder
acc = CredentialReadder()

if __name__ == '__main__':
    while True:
        cred_checker = acc.credential_checker()
        print('Estado actual del acceso al servidor...\n')
        if cred_checker == True:
            print(f'Credenciales: {acc.serv}\n')
        else:
            print('Credenciales: SIN ASIGNAR\n')    

        print('Selecciona la opcion a ejecutar:\n'
              '1. Asignar credenciales.\n'
              '2. Borrar credenciales.\n'
              '3. Instalar EMPRESS.\n'
              '4. Estatus.\n'
              '5. Salir.\n'
        )

        option = input()

        # Llama a la funcion que establece las credenciales.
        if option == '1':
                while True:
                    if cred_checker == True:
                        print('Ya se encuentran asignadas las credenciales en este equipo.\n')
                        print('Deseas renovarlas?\n')

                        cred_rep = input()

                        if cred_rep == 'Y' or cred_rep == 'y':
                            acc.release_creds()
                            sleep(1)
                            print('Credenciales removidas...\n')
                            acc.renew_creds()
                            sleep(1)
                            print('Credenciales renovadas...\n')
                            sleep(2)
                            break
                        elif cred_rep == 'N' or cred_rep == 'n':
                            break
                    if cred_checker == False:
                        acc.renew_creds()
                        sleep(2)
                        print('Se han generado las credenciales...\n')
                        break

        # Si las credenciales no han sido establecidas omite la decisión, sino, llama la funcion que elimina las credenciales.
        if option == '2':
            if cred_checker == False:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')
            else:
                acc.release_creds()
                sleep(1)
                print('Se han eliminado las credenciales...\n')

        # Instala EMPRESS unicamente si las credenciales estan instaladas.
        if option == '3':
            if cred_checker == True:
                print('Comenzando instalacion...')
                sleep(1)
                acc.empress_instalation()
            else:
                sleep(1)
                print('No hay credenciales para la instalacion.')

        # Devuelve un mensaje del estado actual de las credenciales al servidor.  
        if option == '4':
            if cred_checker == True:
                sleep(1)
                print('Credenciales asignadas.\n')
            else:
                sleep(1)
                print('Aun no se han asignado credenciales a este equipo.\n')

        # Sale del programa.
        if option == '5':
            break