class JobDTO:
    def __init__(self, title=None, amount=None, description=None, link=None, work_type=None):
        self.amount = amount
        self.description = description
        self.title = title
        self.link = link
        self.work_type = work_type

    def __str__(self):
        return f'------\n{self.title}\n{self.work_type}\n{self.link}, {self.amount}\n{self.description}\n------\n\n'
