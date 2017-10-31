class Element(object):
    def __init__(self, title, item_url=None,
                 image_url=None, subtitle=None, buttons=None):
        self.title = title
        self.item_url = item_url
        self.image_url = image_url
        self.subtitle = subtitle
        self.buttons = buttons

    def get_data(self):
        data = {
            'title': self.title,
            'item_url': self.item_url,
            'image_url': self.image_url,
            'subtitle': self.subtitle
        }
        if self.buttons:
            data['buttons'] = [
                button.get_data() for button in self.buttons
            ]
        return data
