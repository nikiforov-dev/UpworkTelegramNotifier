class JobDTO:
    def __init__(self, title=None, amount=None, description=None, link=None, work_type=None):
        self.amount = amount
        self.description = description
        self.title = title
        self.link = link
        self.work_type = work_type

    def __str__(self):
        return f'<b>{self.title}</b>\n\n' \
               f'<u>{self.work_type} | {self.amount}</u>\n\n' \
               f'<em>« {self.description} »</em>\n\n' \
               f'<a href=\'{self.link}\'><b>Open</b></a>'
