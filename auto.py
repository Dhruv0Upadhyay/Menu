import os
import time
import hadoopAuto
import basic
import dockerAuto
import partition
import webAuto

def main():
	os.system("clear")
	flag=1
	while(flag==1):
		print("  \n ==============================================================================================")
		print("\t\t\t\t\tWelcome!")
		print("\t\t\tMENU FOR AUTOMATION OF FOLLOWING TECHNOLOGIES\n\n")
		print("\t\t\tPress 1 : REMOTE OR LOCAL LOGIN")
		print("\t\t\tPress 2 : HADOOP")
		print("\t\t\tPress 3 : LVM - LOGICAL VOLUME MANAGEMENT")
		print("\t\t\tPress 4 : DOCKER")
		print("\t\t\tPress 5 : CONFIGURING WEB SERVER")
		print("\t\t\tPress 6 : EXIT AUTOMATION")
		print("\n  ==============================================================================================")
		print("\n")
		os.system("tput setaf 3")	
		ch =int(input("Enter Your Choice:: "))
		os.system("tput setaf 7")
		print("\n")
		
		if (ch==1):
			os.system("tput setaf 3")
			print("\n\tOpening Automation For Remote/Local Login... \n")
			os.system("tput setaf 7")
			time.sleep(2)
			basic.main()

		elif (ch==2):
			os.system("tput setaf 3")
			print("\n\tOpening Automation Hadoop Setup... \n")
			os.system("tput setaf 7")
			time.sleep(2)
			hadoopAuto.main()

		elif (ch==3):
			os.system("tput setaf 3")
			print("\n\tOpening Automation For LVM Partitions... \n")
			os.system("tput setaf 7")
			time.sleep(2)
			partition.main()
		
		elif (ch==4):
			os.system("tput setaf 3")
			print("\n\tOpening Automation For Docker... \n")
			os.system("tput setaf 7")
			time.sleep(2)
			dockerAuto.main()
			
		elif (ch==5):
			os.system("tput setaf 3")
			print("\n\tOpening Automation For Configuring Web Server... \n")
			os.system("tput setaf 7")
			time.sleep(2)
			webAuto.main()
			
		
		elif (ch==6):
			os.system("tput setaf 3")
			print("\n<< CLOSING AUTOMATION >>> \n")
			os.system("tput setaf 7")
			flag=0
			
		else:
			os.system("tput setaf 3")
			print("No such option!!!")
			os.system("tput setaf 7")

		os.system("tput setaf 6")
		x = input("\nPress Enter To Continue:\n ")
		os.system("tput setaf 7")
		if (x==""):
			os.system("clear")
		else:
			flag=0

		
if __name__=='__main__':
	main()


