from sqlite3 import connect
from subprocess import run


class Mozilla_History_Tracer:
    def __init__(self):
        self.mozilla_history_db = r"C:\Users\jacob\AppData\Roaming\Mozilla\Firefox\Profiles\iie7bh24.default-release\places.sqlite"
        self.bookmarks = ["https://www.skroutz.gr/books/10888642.%CE%A4%CE%BF-%CE%B2%CE%B9%CE%B2%CE%BB%CE%AF%CE%BF-%CF%84%CE%B7%CF%82-%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AE%CF%82.html?from=catspan", "https://www.youtube.com/watch?v=_7HNLVuTAgc", "https://www.youtube.com/watch?v=vmEHCJofslg", "https://gordicaleksa.medium.com/turing-for-dummies-ai-part-2-848cb87e95ab", "https://www.youtube.com/watch?v=tD6v3tsyfOc", "https://www.deviantart.com/rainmeter", "https://www.skroutz.gr/books/335267.Quantum-%CE%91%CF%8A%CE%BD%CF%83%CF%84%CE%AC%CE%B9%CE%BD-%CE%9C%CF%80%CE%BF%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CE%BC%CE%B5%CE%B3%CE%AC%CE%BB%CE%B7-%CE%B4%CE%B9%CE%B1%CE%BC%CE%AC%CF%87%CE%B7-%CE%B3%CE%B9%CE%B1-%CF%84%CE%B7-%CF%86%CF%8D%CF%83%CE%B7-%CF%84%CE%B7%CF%82-%CF%80%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82.html", "https://www.kaggle.com/krishanudb/pytorch-tutorial-for-beginners", "https://www.youtube.com/watch?v=iOWFXqT5MZ4", "https://www.youtube.com/watch?v=5dZ_lvDgevk", "https://ytmp3.cc/en13/", "https://www.skroutz.gr/books/115975.%CE%98%CE%B5%CF%89%CF%81%CE%AF%CE%B1-%CF%87%CE%BF%CF%81%CE%B4%CF%8E%CE%BD.html", "https://www.youtube.com/watch?v=eivDTOlA0TE", "https://jovian.ai/aakashns/01-pytorch-basics", "https://www.youtube.com/watch?v=3Kq1MIfTWCE", "https://www.youtube.com/watch?v=HrqYGTK8-bo", "https://www.youtube.com/watch?v=tRKeLrwfUgU", "https://www.youtube.com/watch?v=6CVjoOtA5eg", "https://gordicaleksa.medium.com/turing-for-dummies-ai-part-1-f0f668bcd83d", "https://www.skroutz.gr/books/410612.%CE%97-%CE%B1%CF%81%CF%87%CE%AE-%CF%84%CE%B7%CF%82-%CE%B1%CE%B2%CE%B5%CE%B2%CE%B1%CE%B9%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82.html", "https://pytorch.org/docs/stable/torch.html", "https://www.youtube.com/watch?v=exaWOE8jvy8&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=2", "https://www.edyoda.com/", "https://www.youtube.com/watch?v=GIsg-ZUy0MY&t=33929s", "https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo", "https://leetcode.com/problemset/all/", "https://www.youtube.com/watch?v=3Xc3CA655Y4", "http://iplocation.pythonclub.org/"]
    
    def __get_safe_history(self):
        c = connect(self.mozilla_history_db).cursor()
        results = c.execute("SELECT * FROM moz_places").fetchall()
        history = []

        for rec in results:
            if (rec[1] not in self.bookmarks) and (rec[1] not in history):
                history.append(rec[1])

        return history

    def __get_private_history(self):
        command_output = run("ipconfig /displaydns", shell=True, capture_output=True, text=True).stdout
        output_splitted = command_output.split('\n')

        private_history = [output_splitted[i].lstrip() for i in range(len(output_splitted) -1) if output_splitted[i+1] == "    ----------------------------------------"]
        
        return private_history

    def get_history(self):
        return {"Safe": self.__get_safe_history(), "Private": self.__get_private_history()}
