import requests

class callDB():
    def __init__(self, nlpobj):
        self.nlpobj = nlpobj

    def call(self):
        res = "Sorry, this returned no results"
        # if self.nlpobj["action"] == "count":
        #     #call here
        # else:
        #     #call here

        # response = requests.get("http://10.123.27.108:8080/greeting")
        # print(response.content)
        return res