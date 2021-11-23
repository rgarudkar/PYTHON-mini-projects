from instabot import Bot
bot = Bot() #INITIATES THE INSTABOT

bot.login(username="Your Username", password="Your Password")
bot.send_message("Hi Brother", ["Receiver's Username"])