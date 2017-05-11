from slackbot.bot import respond_to, listen_to, default_reply


@respond_to('task')
@listen_to('task')
def reply_task_list(message):
    message.reply("タスクリストを表示しますね！！！")


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
