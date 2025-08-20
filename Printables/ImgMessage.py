
from Printables.Message import Message

class ImgMessage(Message):
    def __init__(self, filepath, subject=None, body=None, max_len=42):
        super().__init__(subject=subject, body=body or "", max_len=max_len)
        self.filepath = filepath

    def render(self):
        ret = []
        # Draw the subject first
        if self.subject is not None:
            for line in self.subject:
                ret.append(line)

        # Insert the image
        ret.append(f"[[image]] {self.filepath}")

        # Insert the caption
        for line in self.body:
            ret.append(line)
        # Return the array
        return ret
