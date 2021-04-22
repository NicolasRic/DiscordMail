import logging
import config

class mailServer:
    async def handel_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        config.emails.append(Email(envelope.mail_from, envelope.rcpt_tos, envelope.content.decode('utf8', errors='replace')))
        logging.info("Email recieved from %s", envelope.mail_from)
        return '250 Message accepted for delivery'

class Email:
    def __init__(self, client, id, data):
        self.client = client
        self.id = id
        self.data = data