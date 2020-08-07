import requests

# rurl = "http://www.hlj.gov.cn/n200/2020/0805/c35-11005974.html"

class Harbin_news():
    def __init__(self, month, start_date, end_date, index):
        self.month = month
        self.start_date = start_date
        self.end_date = end_date
        self.dates = self.get_dates()
        self.start_ind = index

    def get_dates(self):
        acc = []
        for d in range(self.start_date, self.end_date + 1):
            if d < 10:
                d = f"0{d}"
            acc.append(f"0{self.month}{d}")
        return acc

    def sent_req(self):
        for data in self.dates:
            print("*" * 20)
            print(data, end=" ")
            for i in range(self.start_ind, 6246):
                print(i, end=" " if i % 10 != 0 else "\n")
                url = f"http://www.hlj.gov.cn/n200/2020/{data}/c35-1100{i}.html"
                try:
                    req = requests.get(url)
                    if req.status_code == 200:
                        print(url)
                        self.start_ind = i + 1
                except ConnectionError:
                    print("Ауч")
                except:
                    print("Ауч")


harbin = Harbin_news(8, 7, 8, 6145)
harbin.sent_req()