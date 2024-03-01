import telegram.ext
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

Token = "7153716707:AAGtBbQucgTK70FrmR1Ct4SmWskBS-p3lQQ"

updater = telegram.ext.Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to Trailblazer bot")
    buttons = [
        [KeyboardButton("/start"), KeyboardButton("/Course")],
        [KeyboardButton("/help"), KeyboardButton("/join_Us")],
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text("Select from the options", reply_markup=reply_markup)

def help(update, context):
      update.message.reply_text(
        """"
        /start -> To start the bot 
        /course -> To get link of course
        /help -> To get help
        /join_Us -> To Join us
        """
    )
    


def contact(update, context):
    update.message.reply_text("""
    To ask question 🙋‍♂️: 
              👇👇👇
         t.me/trialblazers
         
To get Tech information 💻 
             👇👇👇
         t.me/trialblazers_tech
    """)

def course(update, context):
    keyboard = [
        [InlineKeyboardButton("Basic Computer Skill", callback_data='basic_computer_skill')],
        [InlineKeyboardButton("HTML", callback_data='html')],
        [InlineKeyboardButton("CSS", callback_data='css')],
        [InlineKeyboardButton("JavaScript", callback_data='javascript')],
        [InlineKeyboardButton("Python", callback_data='python')],
        [InlineKeyboardButton("Java", callback_data='java')],
        [InlineKeyboardButton("PHP", callback_data='php')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a course:", reply_markup=reply_markup)


def button_click(update, context):
    query = update.callback_query
    course = query.data

    
    context_dict = {'chat_id': query.message.chat_id, 'context': context}

   
    if course == 'basic_computer_skill':
        Basic_computer_skill(update, **context_dict)
    elif course == 'html':
        HTML(update, **context_dict)
    elif course == 'css':
        CSS(update, **context_dict)
    elif course == 'javascript':
        JavaScript(update, **context_dict)
    elif course == 'python':
        Python(update, **context_dict)
    elif course == 'java':
        Java(update, **context_dict)
    elif course == 'php':
        PHP(update, **context_dict)


def Basic_computer_skill(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtu.be/j9cSNAK91rE?si=ZpA_xp2L3jyLc_nr")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/j9cSNAK91rE?si=ZpA_xp2L3jyLc_nr")

def HTML(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ07cz9NCfuXPcz1YNw7GqAPt&si=ZCqq__aoc0XwlnmV")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/de2FrT6HepM?si=p78Z7PbTRYndGan7")

def CSS(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ04J7QARcAk6jqK8EI4RfQfw&si=Bd-vM3G7c1Ue6XaQ")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/WIpllLuu8wo?si=2BEUTZ87MacxTKzR")

def JavaScript(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ076kcj7UmOEy8g4ttzkdM21&si=LSXCv9pa6youoIk8")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/59MigPDH3Ow?si=bWCAqmPZC5LWjWN_")

def Python(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ04GcomPKDdxG3Dmy-wQW_b2&si=GSWJqaryvQ8OBRKz")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/tx_OM83qo84?si=PX_hBGp4O_Q1ggwn")

def Java(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ05843kMya0mjHnwLR-hLml2&si=upCWGWGf2tgpAjAh")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/Iq5iDyH65aI?si=1MJ5zblO7A9TZS_g")

def PHP(update, context, chat_id=None):
    context.bot.send_message(chat_id=chat_id, text="Full Course: https://youtube.com/playlist?list=PLj0msIsUsJ07mwVMVHkqVSU977ckFBs55&si=TxAm4QXGClgQpOaj ")
    context.bot.send_message(chat_id=chat_id, text="First Vedio: https://youtu.be/43GELsMWGBc?si=0jHVStkX8yA-TqYB")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('join_Us', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('course', course))
dispatcher.add_handler(telegram.ext.CallbackQueryHandler(button_click))
dispatcher.add_handler(telegram.ext.CommandHandler('basic_computer_skill', Basic_computer_skill))
dispatcher.add_handler(telegram.ext.CommandHandler('html', HTML))
dispatcher.add_handler(telegram.ext.CommandHandler('css', CSS))
dispatcher.add_handler(telegram.ext.CommandHandler('javascript', JavaScript))
dispatcher.add_handler(telegram.ext.CommandHandler('python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('java', Java))
dispatcher.add_handler(telegram.ext.CommandHandler('php', PHP))


updater.start_polling()
updater.idle()
