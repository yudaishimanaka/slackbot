from slackbot.bot import respond_to, listen_to


@respond_to(r'^usage\s*$')
@listen_to(r'^usage\s*$')
def usage(message):
    msg = "使用法だよっ!!\n" \
          "*コマンド一覧*\n" \
          ">タスク一覧:*task*\n" \
          ">タスクを開く:*open [task_title]/[overview]/[task_level]/[date]*\n" \
          ">タスクを閉じる:*close [task_title]*\n" \
          "*オプションの説明*\n" \
          ">[task_title] - タスクタイトルを指定\n" \
          ">[overview] - タスク内容を指定\n" \
          ">[task_level] - low(低い):normal(普通):high(高い)の中から指定\n" \
          ">[date] - mm:dd:yyyy-mm:dd:yyyy\n" \
          "*コマンド例* (タスクを開く)\n" \
          ">open test/これはテストタスクです/high/04:01:2017-04:10:2017"
    message.reply(msg)
