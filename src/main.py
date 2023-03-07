from src.Config.Config import Config
from src.Parser.Parser import Parser
from src.DTO.JobDTO import JobDTO
from src.Database.Manager.JobsManager import JobsManager
from src.Telegram.Bot import Bot
from src.Format.Bcolors import bcolors
from datetime import datetime
import time


def get_time() -> str:
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


def parse(parser: Parser, bot: Bot, manager: JobsManager):
    jobs = parser.get_jobs()
    print(get_time(), ' Parsed: ', len(jobs))
    new_count = 0

    job: JobDTO
    for job in jobs:
        if manager.add_new_job(job.title, job.link):
            bot.send_job(job)
            new_count += 1
    print(get_time(), ' New: ', new_count, '\n')


def run():
    config = Config()
    parser = Parser(config=config)
    manager = JobsManager(config=config)
    bot = Bot(config=config)

    while True:
        try:
            parse(parser, bot, manager)
        except Exception as e:
            print(bcolors.format_warning(f"{get_time()} BOT NOT WORKING! IT HAS SOME PROBLEMS!"))
            print(e)
        finally:
            time.sleep(config.get_time_to_sleep())


if __name__ == '__main__':
    run()
