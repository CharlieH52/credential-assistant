import subprocess
import json
import os

working_path = os.getcwd()
# Change the name of the JSON file if you want.
credential_file = os.path.join(working_path, "credentials.json")

class CommandProcessor:
    def command_execution(self, command_args: list[str]):
        try:
            return subprocess.run(command_args, capture_output=True, text=True, shell=True)
        except subprocess.SubprocessError as e:
            print(e)
            
class FileManager:
    def __init__(self):
        self.__check_credential_file()

    @staticmethod
    def get_credentials_from_file() -> dict[str, str]:
        with open(credential_file, "r") as file:
            credentials = json.load(file)
        return credentials
    
    def __check_credential_file(self):
        if not os.path.exists(credential_file):
            self.__create_credential_file()

    # This is the format for the JSON file that I use... 
    def __create_credential_file(self):
        basic_format = {
            "SERVER": "",
            "USER": "",
            "PASSWORD": "",
            "MAIN_PATH": ""
        }
        with open(credential_file, "w") as file:
            json.dump(basic_format, file, indent=4)