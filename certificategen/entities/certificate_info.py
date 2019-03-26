import uuid


class CertificateInfo(object):
    def __init__(self, event_name: str, event_type: str, action: str, description: str, date: str, organizer: str, signature: str, background: str):
        self.event_name = event_name
        self.event_type = event_type
        self.action = action
        self.description = description
        self.date = date
        self.organizer = organizer
        self.signature = signature
        self.background = background

    @classmethod
    def random(cls):
        event_name = str(uuid.uuid4())
        event_type = str(uuid.uuid4())
        action = str(uuid.uuid4())
        description = str(uuid.uuid4())
        date = str(uuid.uuid4())
        organizer = str(uuid.uuid4())
        signature = str(uuid.uuid4())
        background = str(uuid.uuid4())

        return cls(event_name=event_name, event_type=event_type, action=action, description=description, date=date, organizer=organizer, signature=signature, background=background)
