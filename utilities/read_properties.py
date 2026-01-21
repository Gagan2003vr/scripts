import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_username():
        username=config.get("admin login page",'username')
        return username

    @staticmethod
    def get_password():
        password = config.get("admin login page", 'password')
        return password
