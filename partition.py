import os
import time


def main():
	os.system("clear")
	w="Welcome"
	t="This Menu-Based Program will help you to Automate LVM Partition"
	os.system("tput setaf 7")

	flag=1
	pv=[]
	vg=""
	lv=""
	direc=""

	while(flag==1):
		os.system("tput setaf 6")
		print("\n")
		print("  ==============================================================================================")
		print("\t\t\t\t\t{}!".format(w))
		print("\t\t{}\n".format(t))
		print("\t\t\tPress  1 : To Display Hard Disk Information")
		print("\t\t\tPress  2 : To Display Information About Total and Available Space")
		print("\n\n\t\t\t------------Creating---------------")
		print("\t\t\tPress  3 : To Create Physical Volume(PV)")
		print("\t\t\tPress  4 : To Create Volume Group(VG)")
		print("\t\t\tPress  5 : To Create Logical Volume(LV)")
		print("\t\t\tPress  6 : To Format and Mount LV")
		
		print("\n\n\t\t\t------------Displaying---------------")
		print("\t\t\tPress  7 : To Display Physical Volume(PV)")
		print("\t\t\tPress  8 : To Display Volume Group(VG)")
		print("\t\t\tPress  9 : To Display Logical Volume(LV)")

		print("\n\n\t\t\t------------Extending---------------")
		print("\t\t\tPress 10 : To Extend Logical Volume(LV)")

		print("\n\n\t\t\t------------Deleting---------------")
		print("\t\t\tPress 11 : To Delete Physical Volume(PV)")
		print("\t\t\tPress 12 : To Delete Volume Group(VG)")
		print("\t\t\tPress 13 : To Delete Logical Volume(LV)")
		
		print("\n\t\t\tPress 14 : To Exit The Program")
		print("  ==============================================================================================")
		os.system("tput setaf 7")
		print("\n")

		os.system("tput setaf 3")	
		ch =int(input("Enter Your Choice:: "))
		os.system("tput setaf 7")
		print("\n")

		#Display Hard Disks	
		if (ch==1):
			os.system("tput setaf 3")
			print("<<< Hard Disk Information >>>")
			os.system("tput setaf 7")
			os.system("fdisk -l")

		#Display Total Space
		elif (ch==2):
			os.system("tput setaf 3")
			print("<<< Information About Total Space and Available Space>>>")
			os.system("tput setaf 7")
			os.system("df -h")

		#Create Physical Volume
		elif(ch==3):
			l=input("First Want to know Which Hard Disks are Available?(y/n):")
			if (l=="y") or (l=="Y"):
				os.system("lsblk")
				print("\n")
			n=int(input("Enter Number of Physical Volumes you wanna create: "))
			os.system("tput setaf 3")
			for i in range(n):
				print("Enter Physical Volume",(i+1) ,": ",end="")
				h=input()
				os.system("pvcreate {}".format(h))
				pv.append(h)	
			os.system("tput setaf 7")

		#Create Volume Group
		elif(ch==4):
			hd2=[]
			hd=""
			os.system("tput setaf 3")
			print("<<< Creating Volume Group>>>")
			os.system("tput setaf 7")
			n = input("Enter the Name of Volume Group(VG): ")
			vg=n
			print("\nChoose Physical Volume From Below:: ")
			os.system("pvscan")
			s=int(input("\nEnter number of Physical Volumes To create VG: "))
			for i in range(s):
				print("Enter Physical Volume",(i+1) ,": ",end="")
				h=input()
				hd2.append(h)
			for h in hd2:
				hd = hd + " " + h	
			os.system("vgcreate {} {}".format(n,hd))

		#Create Logical Volume
		elif(ch==5):
			os.system("tput setaf 3")
			print("<<< Available Size of Volume Group  >>>\n ")
			os.system("vgdisplay {}".format(vg))
			os.system("tput setaf 7")
			n = input("Enter the Name of Logical Volume(LV): ")
			size = input("Enter the Size (in GB) of Logical Volume(LV): ")
			lv = n
			os.system("lvcreate --size {}G --name {} {}".format(size, lv, vg))
		
		#Formatting and Mounting LV
		elif(ch==6):
			os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
			os.system("tput setaf 3")
			print("<<< Logical Volume Formatted >>>\n")
			os.system("tput setaf 7")
			d = input("Enter directory name to mount the LV: ")
			direc=d
			os.system("mkdir /{}".format(d))
			os.system("mount /dev/{}/{} /{}".format(vg, lv, d))
			os.system("tput setaf 3")
			print("\n<<< Logical Volume Mounted >>>\n")
			os.system("tput setaf 7")

		#Display Physical Volume
		elif(ch==7):
			l = len(pv)
			if(l==0):
				print("\tDisplaying Existing Physical Volume ...\n")
				time.sleep(1)
				os.system("pvscan")
			else:
				os.system("pvscan")
				for i in range(len(pv)):
					os.system("tput setaf 3")
					print("\n<<< Displaying Physical Volume",(i+1)," >>>")
					os.system("tput setaf 7")
					os.system("pvdisplay {}".format(pv[i]))  
					print("\n")             
		
		#Display Volume Group
		elif(ch==8):
			if (vg==""):
				print("\tDisplaying Existing Volume Group...\n")
				time.sleep(1)
				os.system("vgscan")
			else:
				os.system("vgscan")
				os.system("tput setaf 3")
				print("\n<<< Displaying Volume Group >>>\n")
				os.system("tput setaf 7")
				print("\n")
				os.system("vgdisplay {}".format(vg))

		#Display Logical Volume
		elif(ch==9):
			if (lv==""):
				print("\tDisplaying Existing Logical Volume ...\n")
				time.sleep(1)
				os.system("lvscan")
			else:
				os.system("lvscan")
				os.system("tput setaf 3")
				print("\n<<< Displaying Logical Volume >>>")
				os.system("tput setaf 7")
				print("\n")
				os.system("lvdisplay {}/{}".format(vg,lv))

		#Extend Volume Group
		elif(ch==10):
			os.system("tput setaf 3")
			print("<<< Available Size of Volume Group  >>> \n")
			os.system("vgdisplay {}".format(vg))
			os.system("tput setaf 7")
			size = input("Enter Size (in GB) of Logical Volume(LV) you wanna Extend: ")
			os.system("lvextend --size +{}G /dev/{}/{}".format(size,vg,lv))
			os.system("resize2fs /dev/{}/{}".format(vg,lv))
			os.system("tput setaf 3")
			print("<<< Logical Volume Extended >>>")
		
		#Delete Physical Volume	
		elif(ch==11):	
			#if (len(pv)==0):
			print("\tChecking Existing Physical Volume ...\n")
			time.sleep(1)
			os.system("pvscan")
			os.system("tput setaf 3")
			n=input("\nEnter name of Physical Volume you wanna delete: ")
			os.system("pvremove {}".format(n))
			os.system("tput setaf 7")

			
			"""else:
				os.system("tput setaf 3")
				print("\n Available Physical Volume : \n")
				for h in pv:
					print("\t",h)
				os.system("tput setaf 7")
				n=input("\nEnter name of Physical Volume you wanna delete: ")
				os.system("pvremove {}".format(n))
				for h in pv:
					if (n == h):
						pv.remove(h) """		

		#Delete Volume Group	
		elif(ch==12):
			#if (vg==""):
			print("\tChecking Existing Volume Group...\n")
			time.sleep(1)
			os.system("vgscan")
			os.system("tput setaf 3")
			l=input("\nEnter name of Volume Group you wanna delete: ")
			os.system("vgremove {}".format(l))
			os.system("tput setaf 7")
			"""else:
				os.system("tput setaf 3")
				print("\n  Available Volume Group:  ",vg,"\n")
				os.system("tput setaf 7")
				l=input("\nEnter name of Volume Group you wanna delete: ")
				os.system("vgremove {}".format(l))
				vg="" """
			
		#Delete Logical Volume
		elif(ch==13):
			#if (lv==""):
			print("\tChecking Existing Logical Volume ...\n")
			time.sleep(1)
			os.system("lvscan")
			os.system("tput setaf 7")
			os.system("umount /{}".format(direc))
			os.system("lvremove /dev/{}/{}".format(vg,lv))
			lv=""
			"""else:
				os.system("tput setaf 3")
				print("\n Available Logical Volume:  ",lv,"\n")
				os.system("tput setaf 7")
				os.system("umount /{}".format(direc))
				os.system("lvremove /dev/{}/{}".format(vg,lv))
				lv=""  """

		
		elif(ch==14):
			os.system("tput setaf 3")
			print("<<< Closing Program  >>> \n")
			os.system("tput setaf 7")
			flag=0

		else:
			os.system("tput setaf 3")
			print("No such option!!!")
			os.system("tput setaf 7")
			
		os.system("tput setaf 1")
		c = input("\nPress Enter To Continue:\n ")
		os.system("tput setaf 7")
		if (c==""):
			os.system("clear")
		else:
			flag=0


if __name__=='__main__':
	main()



	
