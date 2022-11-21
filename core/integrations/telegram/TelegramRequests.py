class Requests():
  
  BASE_URL = "https://api.telegram.org/bot5921437499:AAFDLifLWEhaU62k1okTM7VA3f8b4cYCpfo"
  
  def send_message(self, chat_id, text):
    url = self.BASE_URL + "/sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)