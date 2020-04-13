import schedule, time,http.client, urllib
def job():
    print('hello')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": "aui4bqowxvocsg5kkzwc3be2kp4fat",
            "user": "u7sws1jeeb8zmrejawjemmpt8j74bt",
            "message": "hello",
            "title": "temperatur",
            "sound": "bike"
            }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()
    time.sleep(10)
schedule.every(1).minutes.do(job)
def loop():
    while(True):
        schedule.run_pending()
        time.sleep(1)
if __name__ == '__main__':
    loop()
