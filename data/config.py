from environs import Env
env = Env()
env.read_env()
TOKEN = env.str("API_TOKEN")
ADMINS = env.list("ADMINS")
