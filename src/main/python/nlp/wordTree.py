from nlp import node
import json

f = open("/Users/Natalie/mybotapp/cs-symphony/src/main/python/nlp/synonyms.json")
lookup = json.load(f)
f.close()

f = open("/Users/Natalie/mybotapp/cs-symphony/src/main/python/nlp/valuesToCol.json")
colLookup = json.load(f)
f.close()

class wordTree():
    def __init__(self, pos):
        self.start = node.node(pos)
        self.cols = []
        self.finalOutput = {"action":None, "constraint":[], "format":None}

    def addNode(self, tag):
        curr = self.start
        while curr.next != None:
            curr = curr.next
        newNode = node.node(tag)
        curr.next = newNode
        if tag[0] in lookup:
            self.cols.append(tag[0])
            if tag[0] == "mismatched":
                self.finalOutput["constraint"].append({"match_status" : "mismatched"})
            elif tag[0] == "unmatched":
                self.finalOutput["constraint"].append({"match_status" : "mismatched"})
        if tag[1] == "CD":
            self.finalOutput["constraint"] = {"foid" : tag[0]}

    def traverse(self, size):
        print(self.finalOutput)
        curr = self.start.next
        last = self.start
        while curr != None and size != 0:
            size -= 1
            print(curr.pos)
            if curr.pos[1] == "NN" and last.pos[1] == "JJ" and len(self.cols) > 0:
                self.finalOutput["action"] = {"find" : self.cols[0]}
            elif curr.pos[1] == "JJ" and last.pos[1] == "WRB":
                self.finalOutput["action"] = {"count" : "*"}
            elif last.pos[1] == "IN":
                if curr.pos[0] in self.cols:
                    self.finalOutput["format"] = {"group" : curr.pos[0]}
                else:
                    if curr.pos[0] in colLookup:
                        self.finalOutput["constraint"].append({colLookup[curr.pos[0]]:curr.pos[0]})
            elif curr.pos[1] == "VBP" and last.pos[1] == "WRB":
                self.finalOutput["action"] = "find"
            last = curr
            curr = last.next
        return self.finalOutput

#{{action: count, cols: foid}, {constraint: {trade_status : mismatched}}, {format: group, cols: client}
#{{action: find, cols: mismatch_reason}, {constraint:[match_status:mismatch, client:CITI]},





