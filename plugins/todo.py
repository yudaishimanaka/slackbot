from slackbot.bot import respond_to, listen_to
import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='gurutaminn1009',
    db='todo',
    charset='utf8'
)


@respond_to(r'^task\s*$')
@listen_to(r'^task\s*$')
def task_list(message):
    with connection.cursor() as cursor:
        msg = "タスク一覧だよっ!!\n"
        sql = "select * from Task where username='yudai' and status='on'"
        cursor.execute(sql)
        results = cursor.fetchall()
        for value in results:
            msg += (">*" + str(value[1]) + "* (" + str(value[4]) + "まで)\n")

        message.reply(str(msg))


@respond_to(r'^open\s([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)\/([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)'
            r'\/(low|norml|high)\/(\d{2}:\d{2}:\d{4}-\d{2}:\d{2}:\d{4})$')
@listen_to(r'^open\s([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)\/([亜-熙ぁ-んァ-ヶa-zA-Z._?\/^\S].*?)'
           r'\/(low|norml|high)\/(\d{2}:\d{2}:\d{4}-\d{2}:\d{2}:\d{4})$')
def reply_test(message, title, overview, level, date):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Task WHERE username = 'yudai' AND title ='" + title + "'")
        data = cursor.fetchone()
        if data is None:
            if level == "low":
                level = "普通"
            elif level == "normal":
                level = "重要"
            else:
                level = "最重要"
            date = date.split("-")
            start = date[0].replace(':', '/')
            end = date[1].replace(':', '/')
            cursor.execute('INSERT INTO Task (username,title,contents,startp,endp,level,status) '
                           'VALUES(%s,%s,%s,%s,%s,%s,%s)', ["yudai", title, overview, start, end, level, "on"])
            connection.commit()
            cursor.execute("SELECT * FROM Task WHERE username = 'yudai' AND title ='" + title + "'")
            value = cursor.fetchone()
            msg = ">タスクタイトル:" + value[1] + "\n" \
                  ">優先度:" + value[5] + "\n" \
                  ">締め切り:" + value[4] + ""
            default_message = 'タスクを登録したよっ!!頑張れ!!リトルデーモン!! :muscle: \n'
            message.reply(default_message + msg)
        else:
            default_message = 'タスク一覧か完了済みタスク一覧に「 *' + data[1] + '* 」って言う同じタイトル' \
                              'のタスクが存在するよ？おっちょこちょいのリトルデーモンだね :grin: \n'
            message.reply(default_message)


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
