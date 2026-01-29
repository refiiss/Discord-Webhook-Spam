#props an KI
#Grüße an BIG A


import requests
from concurrent.futures import ThreadPoolExecutor

url = input("Webhook URL: ")
msg = input("Nachricht: ")
anzahl = int(input("Anzahl: "))

print("\nBild senden?")
print("1 - Kein Bild")
print("2 - Bild von URL")
print("3 - Lokales Bild")
bild_option = input("Wähle : ")

def send(i):
    try:
        if bild_option == "1":

            requests.post(url, json={"content": msg})
        
        elif bild_option == "2":

            data = {
                "content": msg,
                "embeds": [{"image": {"url": bild_url}}]
            }
            requests.post(url, json=data)
        
        elif bild_option == "3":

            with open(bild_pfad, 'rb') as f:
                files = {'file': f}
                data = {'content': msg}
                requests.post(url, data=data, files=files)
        
        print(f"{i+1}/{anzahl}")
    except Exception as e:
        print(f"Fehler bei {i+1}: {e}")


if bild_option == "2":
    bild_url = input("Bild URL: ")
elif bild_option == "3":
    bild_pfad = input("Bild Pfad (z.B. C:/bild.png): ")

print(f"\n🚀 Sende {anzahl} Nachrichten...")


with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(send, range(anzahl))

print("\nFertig!")