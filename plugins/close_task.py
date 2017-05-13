from slackbot.bot import respond_to, listen_to
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='gurutaminn1009',
    db='todo',
    charset='utf8'
)


@respond_to(r'^close\s([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)$')
@listen_to(r'^close\s([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)$')
def close_task(message, title):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Task WHERE username = 'yudai' AND title ='" + title + "'")
        data = cursor.fetchone()
        if data is None:
            message.reply("そんなタスクないよ!!")
        else:
            cursor.execute("UPDATE Task SET status ='off' WHERE username ='yudai' AND title ='" + title + "'")
            connection.commit()
            message.reply("タスクを閉じたよ!!")
