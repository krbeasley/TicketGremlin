
from Printables.Message import Message


class Task(Message):
    def __init__(self, body, due_date, subject=None, max_len=42):
        super().__init__(subject=subject, body=body, max_len=max_len)
        self.due_date = due_date

    def render(self):
        ret = []

        if self.subject is not None:
            for line in self.subject:
                ret.append(line)

        ret.append(f"Due: {self.due_date}")
        ret.append("")

        for line in self.body:
            ret.append(line)

        return ret

