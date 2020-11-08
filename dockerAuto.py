import os 

def main():
	os.system("clear")
	flag=1

	while (flag==1) :
		os.system("tput setaf 2")  
		print("\n\t\tThis menu is all about the Docker...")
		os.system("tput setaf 1")
		print("\t---------------------------------------------------")

		os.system("tput setaf 3")
		print(""" 
		Enter 1 : To start the docker service
		Enter 2 : To check the status of the docker service
		Enter 3 : To know how many Images you have
		Enter 4 : To Download the Image you want
		Enter 5 : To Create the OS of any Image
		Enter 6 : To Know how many Running OS  
		Enter 7 : To Know the List of OS you have
		Enter 8 : To Start the Already Installed OS (Stopped/Run)
		Enter 9 : If you want the stop any os 
		Enter 10 : To Exit from this menu..!! 
		""")
		os.system("tput setaf 1")
		print("\t---------------------------------------------------")
		
		os.system("tput setaf 7")
		ch = int(input("\nEnter Your Choice : "))
		
		if (ch == 1):
			os.system("systemctl start docker")
			os.system("systemctl enable docker")	
			
		elif (ch == 2):
			os.system("tput setaf 2")
			print("Type Ctrl + c to exit from here..")
			os.system("systemctl status docker")
						
		
		elif (ch == 3):
			os.system("tput setaf 6")
			os.system("docker images")

		elif (ch == 4):
			os.system("tput setaf 2")
			img = input("Enter Your image name which you want : ")
			print("\nDownloading {} Image ...\n".format(img))
			os.system("docker pull {}".format(img))

		elif (ch == 5):
			os.system("tput setaf 6")
			name = input("Enter the name for os : \n ")
			img = input("Enter Your image name for installation : \n")
			version = input("Enter the Version of image : \n")
			os.system("docker run -it --name {} {}:{}".format(name,img,version))
			os.system("tput setaf 3")

		elif (ch == 6):
			os.system("tput setaf 2")
			os.system("docker ps")

		elif (ch == 7):
			os.system("tput setaf 5")
			os.system("docker ps -a ")

		elif (ch == 8):
			os.system("tput setaf 2")
			name = input("Enter the name of os which you want to start :\n")
			os.system("docker start {}".format(name))
			os.system("docker attach {}".format(name))
			os.system("tput setaf 6")

		elif (ch == 9):
			os.system("tput setaf 6")
			name = input("Enter the name of os which you want to stop.. ")
			os.system("docker stop {}".format(name))

		elif (ch == 10):
			os.system("tput setaf 2")
			print("Closing This Automation!!")
			os.system("tput setaf 7")
			flag=0
		
		else :
			os.system("tput setaf 1")
			print("Option Not Supported")

		os.system("tput setaf 6")
		x = input("\nPress Enter To Continue:\n ")
		os.system("tput setaf 7")
		if (x==""):
			os.system("clear")
		else:
			flag=0


if __name__=='__main__':
	main()

