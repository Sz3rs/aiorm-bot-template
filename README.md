<h1>Шаблон бота на Aiogram</h1>

Укажите в файле .env токен от бота и список ID администраторов:

`botToken=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ`<br>
`admins=123456789,987654321,111111111`

Чтобы перевести бота на mysql, укажите в .env:

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
