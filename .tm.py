import os,sys,requests,time



def Emad():
	if Emadman in requests.get("https://raw.githubusercontent.com/Emad00Emad/Test1/main/.m.txt").text:
		Zz()
	else:
		os.system("clear")
		print(" Hello dear user, sorry, this code has been updated. Wait five minutes. The old code will be automatically deleted and the updated code will be installed from the programmer. [ Emad alkhashen ] Thank you.")
		time.sleep(50)
		os.system("clear")
		os.system("rm -rf Test1")
		os.system("clear")
		os.system("git clone https://github.com/Emad00Emad/Test1")
		os.system("clear")
		os.system("python .tm.py")


def Zz():
	print(" Hi prooo ")


if __name__=='__main__':
	try:Emadman = requests.get("https://raw.githubusercontent.com/Emad00Emad/Test1/main/.f.txt").text
	except:pass
	Emad()
