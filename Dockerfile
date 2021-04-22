FROM python:3

WORKDIR /usr/src/app

ENV discord-api=empty

EXPOSE 25/tcp

COPY main.py mail.py ./
COPY docker-config.py ./config.py
RUN pip install discord.py aiosmtpd

CMD ["python3", "main.py"]