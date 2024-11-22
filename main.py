from cred_access.src.mainMenu import *
from cred_access.src.options.addOption import add_credentials
from cred_access.src.options.deleteOption import delete_credentials
from cred_access.src.options.serverPathOption import server_path

from cred_access.src.mainFunctions import CredentialManager

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