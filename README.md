<h1>Aiorm - лучший шаблон бота на AioGram с удобной ORM системой</h1>

Укажите в файле .env токен от бота и список ID администраторов:

`botToken=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ`<br>
`admins=123456789,987654321,111111111`

Чтобы перевести бота на mysql, укажите в .env:

`DBtype=mysql`<br>
`mysqlDatabase=name`<br>
`mysqlUser=admin`<br>
`mysqlPassword=12345678`

<h2>Запуск бота</h2>
Через терминал линукс:<br>

`pip3 install -r requirements.txt` (установка необходимых модулей) <br>
`python3 bot.py`

Через Docker:<br>
`chmod +x runbot.sh` (команда вводится один раз, в последующие запуски ее можно не вводить)<br>
`./runbot.sh` (подготовка и запуск контейнера с ботом)

<h2>Добавление новых колонок</h2>
Если вам понадобится добавить в таблицу Peewee новую колонку, то используйте migrator.py. Его нужно запустить отдельно
`python3 migrator.py`
