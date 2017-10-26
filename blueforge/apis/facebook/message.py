import json


class Message(object):
    def __init__(self, text=None, attachment=None, quick_repilies=None):
        if not text and not attachment:
            raise ValueError('The text or attachment value are required.')

        self.text = text
        self.attachment = attachment
        self.quick_replies = quick_repilies

    def get_data(self):
        data = {}

        if self.text:
            data['text'] = self.text

        if self.attachment:
            data['attachment'] = self.attachment.get_data()

        if self.quick_replies:
            data['quick_replies'] = self.quick_replies.get_data()
        return data


class Recipient(object):
    def __init__(self, recipient_id=None, phone_number=None):
        if not recipient_id and not phone_number:
            raise ValueError('The recipient id or phone number are required.')
        self.recipient_id = recipient_id
        self.phone_number = phone_number

    def get_data(self):
        if self.recipient_id:
            return {'id': self.recipient_id}
        return {'phone_number': self.phone_number}


class RequestDataFormat(object):
    def __init__(self, recipient=None, message=None, sender_action=None):
        if not recipient:
            raise ValueError('The recipient is required.')

        if not message and not sender_action:
            raise ValueError('The message or sender action value are required.')

        self.recipient = recipient
        self.message = message
        self.sender_action = sender_action

    def get_data(self):
        data = {}

        if self.recipient:
            data['recipient'] = self.recipient.get_data()

        if self.message:
            data['message'] = self.message.get_data()

        if self.sender_action:
            data['sender_action'] = self.sender_action

        return data

    def serialise(self):
        return json.dumps(self.get_data())