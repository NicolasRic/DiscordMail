import smtpd
import logging
import config

class mailServer(smtpd.SMTPServer):
    def __init__(*args, **kwargs):
        smtpd.SMTPServer.__init__(*args, **kwargs)
        logging.info("SMTP server running on port %s", config.smtpport)

    def process_message(self, peer, mailfrom, rcpttos, data):
        config.emails.append(Email(mailfrom, rcpttos, data))
        logging.info("Email recieved from %s", mailfrom)

class Email:
    def __init__(self, client, id, data):
        self.client = client
        self.id = id
        self.data = data