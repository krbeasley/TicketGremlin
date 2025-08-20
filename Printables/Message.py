def getNChars(text, n):
    """Returns the first n characters from a line of text"""
    return text[:n]


class Message:
    def __init__(self, subject=None, body="", max_len=42):
        self.MAX_LEN = max_len
        self.subject = subject
        self.setBody(body)

    def setSubject(self, new_subject):
        self.subject = self.createTextArray(new_subject)

    def createTextArray(self, text):
        # Split the text string into a tmp array based on new lines
        tmp_arr = self.parseNewLines(text)
        text_arr = []
        # Loop through the lines and push them to the text_arr
        for line in tmp_arr:
            # ignore this if it's an image path
            if not line.startswith("[[image]]"):
                # Continue splitting and adding lines until you're left with
                # something that'll fit on one line.
                while len(line) > self.MAX_LEN:
                    loop = 0
                    nChars = getNChars(line, self.MAX_LEN)
                    # make sure we're not splitting in the middle of a word
                    while nChars[-1] not in [" ", "-", ":", "/"]:
                        # Check we're not stuck in an infinite loop
                        if loop > 100:
                            print("Looped too many times reducing a string.")
                            exit(1)
                        loop = loop + 1
                        nChars = getNChars(line, self.MAX_LEN + loop)
                    # Remove nChars from the line
                    line = line.replace(nChars, "")
                    text_arr.append(nChars.strip())
            # Make sure to add whatever's left
            text_arr.append(line.strip())
        # Strip the last line if it's blank
        if text_arr[-1] == "":
            text_arr.pop(-1)
        # Finally return the text array
        return text_arr

    def setBody(self, body):
        self.body = self.createTextArray(body)

    def parseNewLines(self, text):
        ret = []
        lines = str(text).split("\\n")
        for line in lines:
            ret.append(line)
            ret.append("")

        return ret

    def render(self):
        ret = []

        if self.subject is not None:
            for line in self.subject:
                ret.append(line)
            ret.append("")

        for line in self.body:
            ret.append(line)

        return ret
