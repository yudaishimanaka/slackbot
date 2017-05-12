from slackbot.bot import respond_to, listen_to, default_reply


@respond_to('愛こそすべて')
@listen_to('愛こそすべて')
def reply_guiltykiss(message):
    message.reply("guilty kiss!!")


@respond_to('可愛い')
@listen_to('可愛い')
@respond_to('かわいい')
@listen_to('かわいい')
def reply_kawaii(message):
    message.reply("ありがとう♡")
    message.react('heart')


@default_reply()
def default_reply(message):
    message.reply("あいきゃんこと小林愛香だよっ!?、よろしくねっ!!")
