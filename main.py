from src.mainMenu import *
from src.options.addOption import add_credentials
from src.options.deleteOption import delete_credentials
from src.options.serverPathOption import server_path

from src.mainFunctions import CredentialManager

cr = CredentialManager()

if __name__ == '__main__':
    while True:
        cred_status()

        main()

        option = input()
        
        if option == '1':
            add_credentials()

        elif option == '2':
            delete_credentials()
        
        elif option == '3':
            server_path()

        elif option == '4':
            pass

        elif option == '5':
            pass

        elif option == '6':
            break