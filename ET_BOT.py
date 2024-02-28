import telegram.ext

Token = "6768721066:AAFosnVbl04ecLtkWG0ugM37VpzmLhg0AQ0"

updater = telegram.ext.Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to Ethio Programming")

def help(update, context):
    update.message.reply_text(
        """"
        /Start -> Welcome to the channel
        /Help -> This particular message
        /Content -> About various playlists of Ethio programming
        /Basic Computer Skill -> The first video from basic computer skill playlist
        /HTML -> The first video from HTML playlist
        /CSS -> The first video from CSS playlist
        /Java Script -> The first video from Java Script playlist
        /Python -> The first video from Python playlist
        /Java -> The first video from Java playlist
        /PHP -> The first video from PHP playlist
        /Contact -> Contact information
        """
    )

def content(update, context):
    update.message.reply_text("We have various playlists and articles available")

def Basic_computer_skill(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/j9cSNAK91rE?si=ZpA_xp2L3jyLc_nr")

def HTML(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/de2FrT6HepM?si=p78Z7PbTRYndGan7")

def CSS(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/WIpllLuu8wo?si=2BEUTZ87MacxTKzR")

def JS(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/59MigPDH3Ow?si=bWCAqmPZC5LWjWN_")

def Python(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/tx_OM83qo84?si=PX_hBGp4O_Q1ggwn")

def Java(update, context):
    update.message.reply_text("Tutorial link: https://youtu.be/Iq5iDyH65aI?si=1MJ5zblO7A9TZS_g")

def PHP(update, context):
    update.message.reply_text("Tutorial link: https://youtube.com/playlist?list=PLj0msIsUsJ07mwVMVHkqVSU977ckFBs55&si=TxAm4QXGClgQpOaj")

def contact(update, context):
    update.message.reply_text("You can contact us on this Group: t.me/trialblazers")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('Basic_computer_skill', Basic_computer_skill))
dispatcher.add_handler(telegram.ext.CommandHandler('HTML', HTML))
dispatcher.add_handler(telegram.ext.CommandHandler('CSS', CSS))
dispatcher.add_handler(telegram.ext.CommandHandler('JavaScript', JS))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('Java', Java))
dispatcher.add_handler(telegram.ext.CommandHandler('PHP', PHP))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))

updater.start_polling()
updater.idle()
