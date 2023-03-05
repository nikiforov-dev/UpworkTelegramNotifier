import telebot
from src.Config.Config import Config
from src.DTO.JobDTO import JobDTO


class Bot:
    def __init__(self, config: Config):
        self.__token = config.get_telegram_bot_token()
        self.__chat_id = config.get_telegram_chat_id()
        self.__bot = telebot.TeleBot(self.__token)

    def send_job(self, job: JobDTO):
        self.__bot.send_message(self.__chat_id, job.__str__())
