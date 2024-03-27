# დაწერე ფუნქცია რომელიც არგუმენტად მიიღებს ვებგვერდის მისამართს და გააგზავნის GET request_ს ყოველ 10 წამში და დაბეჭდოს
# ვებგვერდის სახელი და პასუხად მიღებული სტატუსის კოდი. გამოიყენე time მოდულის sleep ფუნქცია.
# Threading_ის გამოყენებით ერთდროულად გაუშვი ზემოხსენებული ფუნქცია სამი განსხვავებული ვებგვერდის შესამოწმებლად.

import time
import threading
import requests

def threading_urls(url):
    while True:
        time.sleep(10)
        response = requests.get(url)
        if response.status_code == 200:
            website_name = url.split("/")[2]
            print(f"Website Name: {website_name}\nRequest Status Code: {response.status_code}\n")
        else:
            print("Something went wrong!")
            break


website_1 = threading.Thread(target=threading_urls, args=("https://webflow.com/?r=0",))
website_2 = threading.Thread(target=threading_urls, args=("https://ghost.org/",))
website_3 = threading.Thread(target=threading_urls, args=("https://felixcolgrave.myportfolio.com/",))

website_1.start()
website_2.start()
website_3.start()
