class messageParse():

    def __init__(self, message):
        self.message = message

    def getContent(self):
        content = self.message["message"]
        if "<p>" in content:
            idxStart = content.index("<p>") + 3
            idxEnd = content.index("</p>")
            content = content[idxStart:idxEnd]
            return content
        return None