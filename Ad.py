import os
#os.system("pip install Dick.py==1.2.3")
import amino
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\33[93;5;5m\33[93;5;234m ❮ NON-STOP ADVERTISEMENT : Made By Levi ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("TECH", font="cybermedium"))
print(pyfiglet.figlet_format("VISION", font="cybermedium"))
client = amino.Client()
lists=[]
cmlink=[]

xd=open('message.txt','r')
admsg=(xd.read())
email = input("\33[93;5;5m\33[93;5;234m ❮ EMAIL ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
password = input("\33[93;5;5m\33[93;5;234m ❮ PASSWORD ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
client.login(email = email, password = password)
print("\33[93;5;5m\33[93;5;234m ❮ Logged In Account ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")

t = open('cm.txt','r')
for m in t.read().splitlines():
    temp=m

    lists.append(str(temp))
t.close
print("\n\33[93;5;5m\33[93;5;234m ❮ Collecting Community ID... ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
for i in lists:
	try:
		fok=client.get_from_code(i)
		cid=fok.path[1:fok.path.index("/")]
		cmlink.append(cid)
		print("\33[93;5;5m\33[93;5;234m ✓  "+ cid + "\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
	except:
		print("Invalid link")
	
for cid in cmlink:
	try:
		client.join_community(cid)
		subclient =amino.SubClient(comId = cid,profile=client.profile)
		os = subclient.get_all_users(start=0,size=500,type="recent").profile.userId
		usn = subclient.get_all_users(start=0,size=500,type="recent").profile.nickname
		print(f"\n\33[93;5;5m\33[93;5;234m ❮ Advertisement Started in {cid} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
		for userd,nick in zip(os,usn):
			try:
				subclient.start_chat(userId = userd, message = admsg)
				print("\33[93;5;5m\33[93;5;234m ❮ Advertised to ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m" + nick)
			except Exception:
				pass
	except Exception as e:
		print(e)
	print(f"\n\33[93;5;5m\33[93;5;234m ❮ Advertisement Done In {cid} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
	
print("\n\33[48;5;5m\33[38;5;234m ❮Advertisement Done in all Communities ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")