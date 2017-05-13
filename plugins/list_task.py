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

connection.close()
