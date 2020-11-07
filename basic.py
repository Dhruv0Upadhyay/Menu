import os
import time
import getpass

def main():
	os.system("clear")
	w="Welcome"
	t="Basic Linux Commands Automation"
	flag=1
	status=""
	while(flag==1):
		os.system("tput setaf 6")
		print("  \n ==============================================================================================")
		print("\t\t\t\t\t{}!".format(w))
		print("\n\t\t\t{}\n".format(t))
		os.system("tput setaf 2")
		print("\t\t\tDATE\tCAL\tLS\tifconfig")
		print("\t\t\tmkdir\tcat\tPS\tman")
		os.system("tput setaf 6")
		print("\n\t\t--- Do You Want To Run Commands Locally Or Remotely ---\n")
		l = input("\t\t\tEnter your choice(L/R): ")
		print("\n ==============================================================================================")
		os.system("tput setaf 7")
		print("\n")

		
		#For Local Login		
		if (l=="L") or (l=="l"):
			pas=getpass.getpass("Enter password of Local System: ")
			if (pas==YOUR_PASSWORD):
				print("\n\tChecking Password...")
				time.sleep(2)
				os.system("clear")
				os.system("tput setaf 6")
				print("\n\n\t\t<<< LOCAL LOGIN >>>")
				os.system("tput setaf 7")
				listOption("Local",None)
			else:
				print("\n\tPassword Incorrect")
		
		#For Remote Login
		elif(l=="R") or (l=="r"):
			ip = input("Enter IP of System You Want to Remote Login: ")
			print("\n\tSearching IP...")
			time.sleep(2)
			os.system("clear")
			os.system("tput setaf 6")
			print("\n\n\t\t<<< REMOTE LOGIN >>>")
			os.system("tput setaf 7")
			listOption("Remote",ip)

		else:
			os.system("tput setaf 3")
			print("No such option!!!")
			os.system("tput setaf 7")

		#Switch btw Local And Remote Login		
		os.system("tput setaf 6")
		c = input("\n\n\n\tWant To Change Type Of Login?(Y/N): ")
		os.system("tput setaf 7")
		if (c=="Y") or (c=="y"):
			os.system("clear")
		else:
			print("\n\n\t<<< Closing Program >>>\n\n")
			flag=0


def listOption(login,ip):
	f=1

	while(f==1):

		os.system("tput setaf 2")
		print("  \n  ==============================================================================================")
		print("\n\t\tSelect Any Linux Command --> \n")
		print("\t\t1: Run DATE command")
		print("\t\t2: Run CAL command")
		print("\t\t3: Run LS command")
		print("\t\t4: Show IP Address of system")
		print("\t\t5: Show Running Processes")
		print("\t\t6: Create Folder in Current Directory")
		print("\t\t7: Read File from Current Directory")
		print("\t\t8: Exit {} Login".format(login))
		print("\n  ==============================================================================================\n")
		os.system("tput setaf 3")	
		op =int(input("\tEnter Your Choice:: "))
		os.system("tput setaf 7")		
		print("\n")
		
		#For Local Login
		if (login=="Local"):
			if op==1:
				#For DATE command
				os.system("tput setaf 6")
				print("\n\t<<< Running DATE Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("date")
			elif op==2:
				#For CAL command
				os.system("tput setaf 6")
				print("\n\t<<< Running CAL Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("cal")
			elif op==3:
				#For LS command
				os.system("tput setaf 6")
				print("\n\t<<< Running LS Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ls")
			elif op==4:
				#For ifconfig command
				os.system("tput setaf 6")
				print("\n\t<<< Running ifconfig Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ifconfig enp0s3")
			elif op==5:
				#For PS command
				os.system("tput setaf 6")
				print("\n\t<<< Running PS Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ps")
			elif op==6:
				#For mkdir command
				d=input("Enter Name Of Folder You Want to Create: ")
				os.system("tput setaf 6")
				print("\n\tCreating Folder {}ly...\n".format(login))
				os.system("tput setaf 7")
				os.system("mkdir /root/{}".format(d))
				time.sleep(1)
				os.system("tput setaf 6")
				print("\n\t<<< Folder Created >>>\n")
				os.system("tput setaf 7")

			elif op==7:
				#For cat command
				os.system("tput setaf 6")
				print("\n\t<<< List of Files >>>\n")
				os.system("tput setaf 7")
				os.system("ls *.txt")
				print("\n")
				d=input("Enter Name Of File You Want to Read: ")
				os.system("tput setaf 6")
				print("\n\t Readiing File {}ly...\n".format(login))
				os.system("tput setaf 7")
				os.system("cat /root/{}".format(d))

			elif op==8:
				#Back to main menu
				os.system("tput setaf 6")
				print("\n\t Directing Back To Main Menu...\n")
				os.system("tput setaf 7")
				time.sleep(2)
				f=0
			else:
				print("Not an option!!!")

		#For Remote Login
		else:
			if op==1:
				#For DATE command
				os.system("tput setaf 6")
				print("\n\t<<< Running DATE Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ssh {} date".format(ip))

			elif op==2:
				#For CAL command
				os.system("tput setaf 6")
				print("\n\t<<< Running CAL Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ssh {} cal".format(ip))

			elif op==3:
				#For LS command
				os.system("tput setaf 6")
				print("\n\t<<< Running LS Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ssh {} ls".format(ip))

			elif op==4:
				#For ifconfig command
				os.system("tput setaf 6")
				print("\n\t<<< Running ifconfig Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ssh {} ifconfig enp0s3".format(ip))

			elif op==5:
				#For PS command
				os.system("tput setaf 6")
				print("\n\t<<< Running PS Command {}ly >>>\n".format(login))
				os.system("tput setaf 7")
				os.system("ssh {} ps".format(ip))

			elif op==6:
				#For mkdir command
				d=input("Enter Name Of Folder You Want to Create: ")
				d=print("Enter Name Of Folder You Want to Create: ")
				os.system("ssh {} mkdir /root/{}".format(ip,d))
				os.system("tput setaf 6")
				print("\n\tCreating Folder {}ly...\n".format(login))
				time.sleep(2)
				print("\n\t<<< Folder Created >>>\n")
				os.system("tput setaf 7")

			elif op==7:
				#For cat command
				os.system("ssh {} ls *.txt".format(ip))
				print("\n")
				d=input("Enter Name Of File You Want to Read: ")
				os.system("ssh {} cat /root/{}".format(ip,d))

			elif op==8:
				#For exiting Remote Login
				os.system("tput setaf 6")
				print("\n\tExiting Remote Login...")
				os.system("tput setaf 7")
				time.sleep(2)
				f=0
			else:
				print("Not an option!!!")

		os.system("tput setaf 6")
		if (op==8):
			c = input("\nPress Enter To Continue\n ")
		else:
			c = input("\nPress Enter To Continue With {} Login!\n ".format(login))
		os.system("tput setaf 7")
		if (c==""):
			os.system("clear")
		else:
			f=0
		

if __name__=='__main__':
	main()

