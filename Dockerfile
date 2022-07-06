FROM python:3.7-slim
WORKDIR /home/telegram
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt
ENTRYPOINT python bot.py
