from datetime import datetime

class Note:
    def __init__(self, Id, header, body, date):
        self.Id = Id
        self.header = header
        self.body = body
        self.date = date


    def get_id(self):
        return self.Id

    def get_header(self):
        return self.header

    def set_header(self, newHeader):
        self.header = newHeader
    def get_body(self):
        return self.body
    def set_body(self, newBody):
        self.body = newBody
    def get_date(self):
        return self.date

    def set_date(self):
        self.date = datetime.now()


