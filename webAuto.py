import webbrowser
import os 

def main():
	os.system("clear")
	flag=1
	while (flag==1):
		
		os.system("tput setaf 1")
		print("\n\t\t!! This menu is all about the webserver !!")
		os.system("tput setaf 3")
		print("\t--------------------------------------------------------------")
		os.system("tput setaf 6")

		print("""
		Press 1 : To install the web server software(httpd)
		Press 2 : To start the web server 
		Press 3 : To check the status of the web server
		Press 4 : To know the list of Files you have in webserver folder
		Press 5 : To make a html file and edit it 
		Press 6 : To edit any html file which is already created
		Press 7 : To launch this file on web server
		Press 8 : To Exit from this menu
		""")
		os.system("tput setaf 1")
		print("\t\n-----------------------------------------------------------------")

		os.system("tput setaf 3")
		chac = input("\nEnter Your Choice Here :")

		if int(chac) == 1:
			os.system("tput setaf 5")
			os.system("yum install httpd")
			
		elif int(chac) == 2:
			os.system("tput setaf 6")		
			os.system("systemctl start httpd")
			os.system("systemctl enable httpd")
			print("Done..!!")

		elif int(chac) == 3:
			os.system("tput setaf 3")
			print("Type Ctrl + c to exit from here..")
			os.system("systemctl status httpd")
			
		elif int(chac) == 4:
			os.system("tput setaf 5")
			os.chdir("/var/www/html/")
			os.system("ls")

		elif int(chac) == 5:
			os.system("tput setaf 2")
			os.chdir("/var/www/html/")
			name = input("Enter any name to create the html file :\n")
			os.system("vim {}.html".format(name))

		elif int(chac) == 6:
			os.system("tput setaf 2")
			os.chdir("/var/www/html/")
			name = input("Enter alredy existed file which you want to edit :\n")
			os.system("vim {}.html".format(name))

		elif int(chac) == 7:
			os.system("tput setaf 4")
			os.system("ifconfig")
			ip = input("Enter your system's IP Address :\n")
			name = input("Enter the html file name :\n")
			webbrowser.open("http://{}/{}.html".format(ip,name))

		elif int(chac) == 8:
			os.system("tput setaf 6")
			print("Closing This Automation")
			os.system("tput setaf 7")
			flag=0
				

		else :
			os.system("tput setaf 1")
			print("""
			Option Not Found
			You Enterd a wrong Choice
			""")

		os.system("tput setaf 6")
		x = input("\nPress Enter To Continue:\n ")
		os.system("tput setaf 7")
		if (x==""):
			os.system("clear")
		else:
			flag=0


if __name__=='__main__':
	main()

