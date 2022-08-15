import getpass
USER_NAME = getpass.getuser()



bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
print(bat_path)