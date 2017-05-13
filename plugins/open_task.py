from slackbot.bot import respond_to, listen_to
import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='gurutaminn1009',
    db='todo',
    charset='utf8'
)


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
            connection.close()
        else:
            default_message = 'タスク一覧か完了済みタスク一覧に「 *' + data[1] + '* 」って言う同じタイトル' \
                              'のタスクが存在するよ？おっちょこちょいのリトルデーモンだね :grin: \n'
            message.reply(default_message)
            connection.close()
