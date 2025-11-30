import requests
import time
i = 0
while True:
    time.sleep(1)
    i += 1
    url = f"https://api.telegram.org/bot7851429639:AAHDiwtYb6_nXC6hGMibpYck2avcEF0EF7s/sendMessage?chat_id=6861956601&text={i}"  # Мұнда өзіңізге қажетті URL енгізіңіз
    response = requests.get(url)