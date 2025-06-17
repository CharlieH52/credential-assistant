import re

class ServerManager:
    def __init__(self, file_credentials: dict[str, str], command_processor):
        self.f_creds = file_credentials
        self.command_executor = command_processor

    # ADD SERVER CREDENTIALS
    def add_creds(self):
        SERV_CREDS = ["cmdkey", f"/add:{self.f_creds['SERVER']}", f"/user:{self.f_creds['USER']}", f"/pass:{self.f_creds['PASSWORD']}"]
        self.command_executor.command_execution(command_args=SERV_CREDS)

    # DELETE CURRENT CREDENTIALS
    def release_creds(self):
        SERV_NAME = ["cmdkey", f"/delete:{self.f_creds['SERVER']}"]
        self.command_executor.command_execution(command_args=SERV_NAME)

    # GETS THE SPECIFIC CREDENTIAL TO CHECK IT
    def get_credentials_in_system(self) -> dict[str, str]:
        SERV_TARGET = ["cmdkey", f"/list:{self.f_creds['SERVER']}"]
        output = self.command_executor.command_execution(command_args=SERV_TARGET)
        if self.__check_current_credentials(output):
            credentials = self.__credential_to_dict(output=output)
            return credentials
        else:
            return {}
    
    # This method compare the credentials in file with the credentials in the system.
    def has_credentials(self) -> bool:
        c_creds = self.get_credentials_in_system()
        try:
            if self.f_creds["SERVER"] == c_creds["DESTINO"]:
                return True
            else:
                return False
        except KeyError:
            return False

    def __check_current_credentials(self, output) -> bool:
        status = re.search(r"(\W\s[A-Z]+\s\W)", output.stdout)
        if status:
            return False
        return True

    # CONVERT THE STDOUT TO DICT 
    def __credential_to_dict(self, output) -> dict[str, str]:
        lines = output.stdout.split('\n')
        cleaned = [line.strip() for line in lines if line.strip() != ''][1:]
        current_credentials = {}
        for item in cleaned:
            key, value = item.strip().split(':', 1)
            key = str(key).upper()
            value = value.strip()
            current_credentials[key] = value
        return current_credentials
    
    # Change the MAIN_PATH in the JSON file created by FileManager.__create_credential_file method.
    def open_server_path(self):
        TARGET_PATH = ["START", f"{self.f_creds['MAIN_PATH']}"]
        self.command_executor.command_execution(command_args=TARGET_PATH)

