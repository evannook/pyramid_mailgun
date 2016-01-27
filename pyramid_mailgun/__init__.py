class Mailer:

    def __init__(self, settings):
        self.domain_name = settings['mailgun.domain_name']
        self.api_key = settings['mailgun.api_key']

    def send(self, email):
        import requests
        requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(self.domain_name),
            auth=("api", self.api_key),
            data={
                "from": email['from'],
                "to": email['to'],
                "subject": email['subject'],
                "text": email['text']
            }
        )

def mailer(request):
    return Mailer(request.registry.settings)

def includeme(config):
    config.add_request_method(mailer, 'mailer', reify=True)
