from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN', "7237448561:AAG0upxhbub0Rfqrpx6gDfEOc9zU-tpUknQ")
MONGO_URI = getenv('MONGO_URI', "mongodb+srv://agautevdragitevsvh:pJSptT6jE0pcw9a4@cluster0.de4uc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', "6634423600").split()))
