from prompt import CLI
from credential_manager import CredentialManager

cr = CredentialManager()
cli = CLI()

if __name__ == '__main__':
    while True:
        cli.cred_status()

        cli.main()

        option = input()\
        
        if option == '1':
            cli.add_credentials()

        elif option == '2':
            cli.delete_credentials()
        
        elif option == '3':
            cli.server_path()

        elif option == '4':
            print('No se ha implementado ninguin modulo.')

        elif option == '5':
            cli.instalation_checker()

        elif option == '6':
            break