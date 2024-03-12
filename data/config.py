from environs import Env


env = Env()
env.read_env()

TOKEN = env.str('BOT_TOKEN')
SOCIALS = env.str('SOCIALS').split(',')
SOCIAL_NAMES = env.str("SOCIAL_NAMES").split(',')
