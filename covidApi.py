import requests
from bs4 import BeautifulSoup
import datetime
import json


import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


message_list = [
    "gubun",
    "defCnt",
    "incDec",
    "qurRate",
    "isolClearCnt",
    "deathCnt",
]
class covidApi(QAxWidget):
    def __init__(self):
        super().__init__()
        self.now = int(datetime.datetime.now().strftime("%Y%m%d")) - 1
        self.API_Key = "k%2BPIRwDWhR8mM7w%2BswcgX7YpCgiaN4pPVuzwOpD5NVKxXb23Zc45moqww27QKKSB8kYQFVTp85Ye%2Ffs5bRvXgw%3D%3D"
        self.URL = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?" \
                  "serviceKey={API}" \
                  "&pageNo=1" \
                  "&numOfRows=10" \
                  "&startCreateDt={date}" \
                  "&endCreateDt={date}".format(API=self.API_Key, date=self.now)
        self.data_list = []
        self.api_connect(requests.get(self.URL))

    def api_connect(self, response):
        if response.status_code == 200:
            html = response.text
            self.soup = BeautifulSoup(html, "html.parser")
            self.set_data()

        else:
            print("response code Error!! error code : {}".format(response.status_code))

    def set_data(self):
        self.data = []
        for i in range(0, 6):
            self.data.append(self.soup.select("item {}".format(message_list[i])))
            #for x in data:
             #   tmp = json.dumps(xmltodict.parse(str(x))['item'])
              #  self.data_list.append(tmp)

    def show(self):
        for x in self.data:
            print(x[0].text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    covidApi = covidApi()
    covidApi.show()








