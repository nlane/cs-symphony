from textblob import TextBlob
from nlp import wordTree

class NLPMain():
    def __init__(self, content):
        self.content = content

    def extractMeaning(self):
        blob = TextBlob(self.content)
        print(blob.tags)
        tags = blob.tags
        tree = wordTree.wordTree(tags[0])
        for i in range(1, len(tags)):
            tree.addNode(tags[i])
        return tree.traverse(len(tags))