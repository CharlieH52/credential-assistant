# Credential Asisstant
It's important to keep credentials in a confidential file and never copy them to other computers on the network. However, sometimes it's necessary to grant access for specific purposes or servers.

This program provides a safe method to grant such access quickly and easily check whether the computer can reach the server.

## Configuration
**Step 1.** Install the dependencies using the requirements.txt file.<br>
**Step 2.** Compile the program with *Pyinstaller* using the following command.<br>
> pyinstaller --clean --onefile --name="{Choose_a_pretty_name}" main.py
>
**Step 3.** Run the program for the first time and let it create the ***credentials.json*** file.<br>
**Step 4.** Enter your server credentials and test the connection.<br>

> [!IMPORTANT]
> You can modify the program to embed the credentials into the executable, but at this stage, it's entirely up to you.