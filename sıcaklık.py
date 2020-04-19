import requests
from bs4 import BeautifulSoup
import time
import keyboard
print("""
********************
Evin Sıcaklığını gösteren program.
Lütfen çıkmak için 'q' tuşuna bas
Sıcaklığı öğrenmek için 's' tuşuna bas
Nemi öğrenmek için 'n' tuşuna bas
********************
Coded by: TURKMEN
********************
""")
while True:
    if keyboard.is_pressed('q'):
        print("Programdan Çıkılıyor...")
        time.sleep(3)
        break
    elif keyboard.is_pressed('s'):
        url="http://139.59.206.133/uhYCCQ8BfR3LtsBIg-DG9ACzsyB_-BH5/get/V6"
        response=requests.get(url) #urlyi çektik
        html_icerik=response.content #url içeriğini çektik
        soup=BeautifulSoup(html_icerik,"html.parser")
        sonuc=soup.prettify()
        print("Sıcaklık {}°C".format(sonuc[2:8]))
        time.sleep(1)
    elif keyboard.is_pressed('n'):
        url = "http://139.59.206.133/uhYCCQ8BfR3LtsBIg-DG9ACzsyB_-BH5/get/V5"
        response = requests.get(url)  # urlyi çektik
        html_icerik = response.content  # url içeriğini çektik
        soup = BeautifulSoup(html_icerik, "html.parser")
        sonuc = soup.prettify()
        print("Nem %{}RH".format(sonuc[2:4]))
        time.sleep(1)


