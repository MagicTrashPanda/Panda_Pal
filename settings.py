# import os and load_dotenv from dotenv
import os
from dotenv import load_dotenv

# load the discordAPIToken from the .env file
load_dotenv()
discordToken = os.getenv('discordAPIToken')
