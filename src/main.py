from src.Config.Config import Config
from src.Parser.Parser import Parser
from src.DTO.JobDTO import JobDTO
from src.Database.Manager.JobsManager import JobsManager
from src.Telegram.Bot import Bot
from src.Format.Bcolors import bcolors
import time


def parse(parser: Parser, bot: Bot, manager: JobsManager):
    jobs = parser.get_jobs()
    print('Parsed: ', len(jobs))

    job: JobDTO
    for job in jobs:
        if manager.add_new_job(job.title, job.link):
            bot.send_job(job)


def run():
    config = Config()
    parser = Parser(config=config)
    manager = JobsManager(config=config)
    bot = Bot(config=config)

    while True:
        try:
            parse(parser, bot, manager)
        except:
            print(bcolors.format_warning("BOT NOT WORKING! IT HAS SOME PROBLEMS!"))
        finally:
            time.sleep(config.get_time_to_sleep())


if __name__ == '__main__':
    run()
