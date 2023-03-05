import configparser
import os


class Config:
    def __init__(self):
        self.__parser = configparser.RawConfigParser()
        self.__parser.read(os.path.join(os.getcwd(), "config.ini"))

    def get_database_connection_string(self):
        return self.__parser['Database']['DbConnectionString']

    def get_upwork_filters_url(self):
        return self.__parser['Parser']['FilterUrl']

    def get_telegram_bot_token(self):
        return self.__parser['Telegram']['BotToken']

    def get_telegram_chat_id(self):
        return self.__parser['Telegram']['ChatId']

    def get_time_to_sleep(self):
        return int(self.__parser['RepeatTime']['Seconds'])
