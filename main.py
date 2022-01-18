from pyrogram import Client, filters
 
bot = Client(
   " This_is_the_first_program",
   api_id = 50519096, #Not Valid Id
   api_hash = "AAGTZ-M5lhNoBXgAZcciOzkuJ6qM2Q3Mfoc", #Not Valid Hash Key
   bot_token = "ENTER YOUR TOKEN Here"
)
#Section 1 - Simple Bot with Menu
@bot.on_message(filters.command('start'))  #creating a command
 
def command1(bot, message):  #calling a function
   bot.send_message(message.chat.id, "Hey, I am there \n Start me with /help")  #calling a method which is prebuilt in .send_messagg
 
#Section 2 - Help command
@bot.on_message(filters.command('help'))  #creating a command
 
def command1(bot, message):  #calling a function
   message.reply_text("You at help command  \n Possible Commands \n /start - start the bot \n  /help - help about the bot  \n /about - About the Bot \n /sticker \n /video \n /audio \n /document \n /photof \n /videof \n /voice \n /animation" )  #calling a method which is prebuilt in .send_message
 
#Section 3 - About
@bot.on_message(filters.command('about'))  #creating a command
 
def command1(bot, message):  #calling a function
   message.reply_text("Developed by @DevShreyas ")  #calling a method which is prebuilt in .send_message
 
#Section 4- #EchoBot
# @bot.on_message(filters.text & filters.private)
# #filter.text is for any text, calling filter function and text object &
# # filters.private means only reply to private messages
# def echobot(client, message):
#     message.reply_text(message.text)
 
#Section 5 - #WelcomeBot Greets Everyone that Joins a group chat
Group = "your grp id or Username if public"
Welcome_Message = "Hello, to the group chat!"
 
@bot.on_message(filters.chat(Group) & filters.new_chat_members) #Filter in only groups
def welcomebot(client, message):
   message.reply_text(Welcome_Message) #Sending welcome message
 
#Section 6 - Send Photo
@bot.on_message(filters.command('photo'))
def command3(bot, message):
   bot.send_photo(message.chat.id, "https://upload.wikimedia.org/wikipedia/commons/8/88/Start_%28%D0%BA%D0%B8%D0%BD%D0%BE%D1%82%D0%B5%D0%B0%D1%82%D1%80%29.jpg")
 
#Section 7 - Send Video
@bot.on_message(filters.command('video'))
def command4(bot, message):
   bot.send_video(message.chat.id, "https://media.istockphoto.com/videos/running-shoes-and-runner-sports-smartwatch-video-id1170296713")
 
#Section 8 - Get Audio
 
   #Part 1 Get File ID
@bot.on_message(filters.audio)
def audio(bot, message):
   message.reply(message.audio.file_id) #Sending file id
#Part 2 Send Using ID
@bot.on_message(filters.command('audio')) 
def command4(bot, message):
    bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBP2HP1ZeFWpwO3FvXDttbbDMYxnRyAALEAwADEoBWS-tsA3VGzjweBA")
 
#Section 9 - Send Documnet
 
#Part 1 Get File ID
@bot.on_message(filters.document & filters.private)
def document(bot, message):
   message.reply(message.document.file_id) #Sending file id
#Part 2 Send Using ID
@bot.on_message(filters.command('document')) 
def command5(bot, message):
  bot.send_document(message.chat.id, "BQACAgUAAxkBAAIBPWHP1RjilZ37qKI4JyACb6O_JlowAAKUBgAChHJ5VlobW0qCJwJoHgQ")
 
#Section 10 - Send Sticker
   #Part 1 Get File ID
@bot.on_message(filters.sticker & filters.private)
def sticker(bot, message):
   message.reply(message.sticker.file_id) #Sending file id
   #Part 2 Send Using ID
@bot.on_message(filters.command('sticker')) 
def command6(bot, message):
  bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAIBdGHP2fAzxhUHNMqKQZdi_43oAAGpMgACBwIAAi6UeBDwTGWRFVkjIR4E") #Need to Update Each time #to send the diffferent message
 
#Section 11 - Send Video
   #Part 1 Get File ID
@bot.on_message(filters.video & filters.private)
def video(bot, message):
   message.reply(message.video.file_id) #Sending file id
   #Part 2 Send Using ID
@bot.on_message(filters.command('videof')) 
def command8(bot, message):
  bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBiWHP3AlYGw7EtAzC16qSUNj7tLVjAALFAwADEoBW2PL3uYrnryAeBA") #Need to Update Each time #to send the diffferent message
 
#Section 12 - Send Photo
   #Part 1 Get File ID
@bot.on_message(filters.photo & filters.private)
def photo(bot, message):
   message.reply(message.photo.file_id) #Sending file id
   #Part 2 Send Using ID
@bot.on_message(filters.command('photof')) 
def command7(bot, message):
  bot.send_photo(message.chat.id, "AgACAgUAAxkBAAIBi2HP3CylwMO6BbbCz4nKv_sNA88hAAImrjEbAAESgFb8DxGusAmHawAIAQADAgADeQAHHgQ") #Need to Update Each time #to send the diffferent message
 
#Section 13 - Send animation
   #Part 1 Get File ID
@bot.on_message(filters.animation & filters.private)
def animation(bot, message):
   message.reply(message.animation.file_id) #Sending file id
   #Part 2 Send Using ID
@bot.on_message(filters.command('animation')) 
def command7(bot, message):
  bot.send_animation(message.chat.id, "CgACAgQAAxkBAAIBo2HP3lzaA5vChsCRPORIKl2VGVClAAIEAwACBeFUUr7WH_Dsnk8mHgQ") #Need to Update Each time #to send the diffferent message
 
#Section 14 - Send voice
   #Part 1 Get File ID
@bot.on_message(filters.voice & filters.private)
def voice(bot, message):
   message.reply(message.voice.file_id) #Sending file id
   #Part 2 Send Using ID
@bot.on_message(filters.command('voice')) 
def command7(bot, message):
  bot.send_voice(message.chat.id, "AwACAgUAAxkBAAIBm2HP3hru5VGS3HWTSq2ViFYW9pgiAALIAwADEoBWMwi4GnBUht8eBA") #Need to Update Each time #to send the diffferent message
 
bot.run()

