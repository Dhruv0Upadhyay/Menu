import subprocess
import os
import time

def main():
	os.system("clear")
	w="Welcome"
	t="This Menu-Based Program will help you to Setup Hadoop"

	flag=1
	status=""
	check = subprocess.check_output("jps")
	status = check.decode("utf-8")
	
	while(flag==1):
		os.system("tput setaf 6")
		print("  \n ==============================================================================================")
		print("\t\t\t\t\t{}!".format(w))
		print("\t\t\t{}\n\n".format(t))
		print("\t\t\tPress 1 : To Check Hadoop Version")
		print("\t\t\tPress 2 : To Check Which Hadoop Service is Running")
		print("\t\t\tPress 3 : To Start Hadoop Service")
		print("\t\t\tPress 4 : To Stop Hadoop Service")
		print("\t\t\tPress 5 : To Check Hadoop Cluster Report")
		print("\t\t\tPress 6 : To List All Existing Files on Hadoop Cluster")
		print("\t\t\tPress 7 : To Exit The Program")
		print("  ==============================================================================================")
		os.system("tput setaf 7")
		print("\n")
		os.system("tput setaf 3")	
		ch =int(input("Enter Your Choice:: "))
		os.system("tput setaf 7")
		print("\n")
		
		#To display Hadoop Version
		if (ch==1):
			os.system("tput setaf 3")
			print("<<< Hadoop Version >>>\n")
			os.system("tput setaf 7")
			os.system("rpm -q hadoop")

		#To display Hadoop Service
		elif (ch==2):
			os.system("tput setaf 3")
			print("<<< Hadoop Service Report>>>\n")
			check = subprocess.check_output("jps")
			status = check.decode("utf-8")
			os.system("tput setaf 7")
			print(status)
			os.system("tput setaf 3")
			if ("NameNode" in status):
				print("STATUS: NameNode is Running!")
			elif ("DataNode" in status):
				print("STATUS: DataNode is Running!")
			else:
				print("STATUS: No Service is Running!")

			os.system("tput setaf 7")
		
		#To Start Hadoop Service-NameNode, DataNode, Client
		elif(ch==3):
			os.system("clear")
			serviceHadoop()	

		#To Stop Hadoop Service
		elif (ch==4):
			os.system("tput setaf 3")
			if ("NameNode" in status):
				print("STATUS: NameNode is Running!")
				ans=input("\nDo you want to stop it?(y/n): ")
				if (ans=="y"):
					os.system("hadoop-daemon.sh stop namenode")
					print("\nNameNode is Stopped!")
			elif ("DataNode" in status):
				print("STATUS: DataNode is Running!")
				ans=input("\nDo you want to stop it?(y/n): ")
				if (ans=="y"):
					os.system("hadoop-daemon.sh stop datanode")
					print("\nDataNode is Stopped!")
			else:
				print("STATUS: No Service is Running!")

			os.system("tput setaf 7")
		
		#To Display Hadoop Report	
		elif (ch==5):
			os.system("tput setaf 3")
			print("<<< Hadoop Report >>>\n")
			os.system("tput setaf 7")
			if ("NameNode" in status) or ("DataNode" in status):
				os.system("hadoop dfsadmin -report")
			else:
				print("\tNo Report To Display!!!")

		#To Display Files On Hadoop Cluster
		elif (ch==6):
			os.system("tput setaf 3")
			print("\n  Gathering Data From Hadoop Cluster...\n")
			print("\n\n<<< List Of files on Hadoop Cluster >>>\n\n")
			os.system("tput setaf 7")
			os.system("hadoop fs -ls /")

		#To close program
		elif(ch==7):
			os.system("tput setaf 3")
			print("<<< Closing This Automation  >>> \n")
			os.system("tput setaf 7")
			flag=0
			exit()

		else:
			os.system("tput setaf 3")
			print("No such option!!!")
			os.system("tput setaf 7")
			
		os.system("tput setaf 6")
		c = input("\nPress Enter To Continue:\n ")
		os.system("tput setaf 7")
		if (c==""):
			os.system("clear")
		else:
			flag=0

#Function To Start Service- NameNode,DataNode,Client
def serviceHadoop():
	f=1
	while(f==1):
		os.system("tput setaf 6")
		print("  \n\n ==============================================================================================")
		print("\t\t\tChoose Which Service You Want To Start?\n")
		print("\t\t\tPress  1 : To Check Hadoop Service Report")
		print("\t\t\tPress  2 : Configure NameNode")
		print("\t\t\tPress  3 : Configure DataNode")
		print("\t\t\tPress  4 : Configure Client")
		print("\t\t\tPress 5 : To Check Hadoop Cluster Report")
		print("\t\t\tPress  6 : Back")
		print("  \n==============================================================================================\n")	
		os.system("tput setaf 3")	
		op =int(input("Enter Your Choice:: "))
		os.system("tput setaf 7")

		#To display Hadoop Service 
		if (op==1):
			os.system("tput setaf 3")
			print("<<< Hadoop Status Report>>>\n")
			os.system("tput setaf 7")
			check = subprocess.check_output("jps")
			status = check.decode("utf-8")
			os.system("tput setaf 3")
			if ("NameNode" in status):
				print("STATUS: NameNode is Running!")
			elif ("DataNode" in status):
				print("STATUS: DataNode is Running!")
			else:
				print("STATUS: No Service is Running!")

			os.system("tput setaf 7")


		#To configure Namenode
		elif (op==2):
			ip=input("Enter IP of Namenode: ")
			direc = "nn"
			node = "name"
			
			# --- To check current directory ---
			#ls1 = subprocess.check_output("pwd")
			#loc1 = ls1.decode("utf-8")
			#print("LOC1: ",loc1)
			
			#Configuring xmls
			os.system("mkdir /etc/hadoop/{}".format(direc))
			serviceNode(ip,node,direc)
			
			#Changing directory to /etc/hadoop/
			os.chdir("/etc/hadoop/")

			#Formatting NameNode
			os.system("tput setaf 3")
			print("\n<<< Formatting NameNode!!  >>> \n")
			os.system("tput setaf 7")
			os.system("hadoop namenode -format")

			#Starting NameNode
			os.system("systemctl stop firewalld")
			os.system("hadoop-daemon.sh start namenode")
			os.chdir("/root/")	
			os.system("tput setaf 3")
			print("\n<<< NameNode Started!!  >>> \n")
			os.system("tput setaf 7")
			#ls2 = subprocess.check_output("pwd")
			#loc2 = ls2.decode("utf-8")
			#print("LOC2: ",loc2)
			
		#To configure DataNode
		elif (op==3):
			ip=input("Enter IP of Namenode: ")
			direc = input("Enter DataNode Directory: ")
			node = "data"
			
			#Configuring xmls
			os.system("mkdir /etc/hadoop/{}".format(direc))
			serviceNode(ip,node,direc)
			
			#Starting DataNode
			os.system("systemctl stop firewalld")
			os.system("hadoop-daemon.sh start datanode")
			os.chdir("/root/")
			os.system("tput setaf 3")
			print("\n<<< DataNode Started!!  >>> \n")
			os.system("tput setaf 7")
		
		#Configuring Client
		elif (op==4):
			os.system("clear")
			serviceClient()	
			
		#To Display Hadoop Report	
		elif (ch==5):
			os.system("tput setaf 3")
			print("<<< Hadoop Report >>>\n")
			os.system("tput setaf 7")
			if ("NameNode" in status) or ("DataNode" in status):
				os.system("hadoop dfsadmin -report")
			else:
				print("\tNo Report To Display!!!")

		elif (op==6):
			os.system("tput setaf 3")
			print("\n<<< Back To Main Menu  >>> \n")
			os.system("tput setaf 7")
			f=0
			
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
			f=0

#Function For Client Service
def serviceClient():
	f=1
	while(f==1):
		os.system("tput setaf 6")
		print("  \n\n ==============================================================================================")
		print("\t\t\t<<< Client Services >>>\n")
		print("\t\t\tPress  1 : Configure Client")
		print("\t\t\tPress  2 : List All Existing Files on Hadoop Cluster")
		print("\t\t\tPress  3 : Upload File to Hadoop Cluster")
		print("\t\t\tPress  4 : Read a File from Hadoop Cluster")
		print("\t\t\tPress  5 : Remove File from Hadoop Cluster")
		print("\t\t\tPress  6 : Upload File with Modified Block Size")
		print("\t\t\tPress  7 : Upload File with Modified Replication Number")
		print("\t\t\tPress  8 : Back")
		print("  \n==============================================================================================\n")	
		os.system("tput setaf 3")	
		op =int(input("Enter Your Choice:: "))
		os.system("tput setaf 7")

		#Configure Client
		if (op==1):
			ip=input("Enter IP of Namenode: ")
			
			#Configuring core-site.xml for Client
			serviceNode(ip,"None","None")
			os.chdir("/root/")
			
		#To display Files On Hadoop Cluster
		elif (op==2):
			os.system("tput setaf 3")
			print("\n  Gathering Data From Hadoop Cluster...\n")
			print("\n\n<<< List Of files on Hadoop Cluster >>>\n\n")
			os.system("tput setaf 7")
			os.system("hadoop fs -ls /")
			
		#To upload file
		elif (op==3):
			f1=input("Enter FileName you wanna upload: ")
			print("\n\nDefault Block Size  : 64MB")
			print("\nDefault Replication : 3\n")
			print("\nEnter data in {} File\n".format(f1))
			time.sleep(2)			
			os.system("vi {}".format(f1))
			os.system("tput setaf 3")
			print("\n  Uploading File....\n")
			os.system("tput setaf 7")
			os.system("hadoop fs -put {} /".format(f1))
			os.system("tput setaf 3")
			print("\n<<< File Uploaded!!! >>>\n")
			os.system("tput setaf 7")
			
		#To Read File
		elif (op==4):
			l=input("First Want to know Which Files Exist on Cluster?(y/n):")
			os.system("tput setaf 3")
			print("\n  Gathering Data From Hadoop Cluster...\n")
			print("\n\n<<< List Of files on Hadoop Cluster >>>\n\n")
			os.system("tput setaf 7")
			if (l=="y"):
				os.system("hadoop fs -ls /")
			f1=input("\nEnter FileName you wanna read: ")
			os.system("tput setaf 3")
			print("\n\n  Reading File....\n\n")
			print("<<< File Data >>>\n")
			os.system("tput setaf 7")			
			os.system("hadoop fs -cat /{}".format(f1))
		
		#To delete file
		elif (op==5):
			l=input("First Want to know Which Files Exist on Cluster?(y/n):")
			os.system("tput setaf 3")
			print("\n\n<<< List Of files on Hadoop Cluster >>>\n\n")
			os.system("tput setaf 7")
			if (l=="y"):
				os.system("hadoop fs -ls /")
			f1=input("\nEnter FileName you wanna delete: ")
			os.system("tput setaf 3")
			print("\n\n  Deleting File....\n\n")
			os.system("tput setaf 7")					
			os.system("hadoop fs -rm /{}".format(f1))
			os.system("tput setaf 3")
			print("\n<<< File Deleted!!! >>>\n")
			os.system("tput setaf 7")
		
		#To upload file with modified block size
		elif (op==6):
			f1=input("Enter FileName you wanna upload: ")
			s=input("Enter Size of Block (in Bytes): ")
			print("\nEnter data in {} File\n".format(f1))
			time.sleep(2)			
			os.system("vi {}".format(f1))
			os.system("tput setaf 3")
			print("\n  Uploading File....\n\n")
			os.system("tput setaf 7")
			os.system("hadoop fs -D dfs.block.size={} -put {} /".format(s,f1))
			os.system("tput setaf 3")
			print("\n<<< File Uploaded!!! >>>\n")
			os.system("tput setaf 7")	
			
		#To upload file with modified replication number
		elif (op==7):
			f1=input("Enter FileName you wanna upload: ")
			s=input("Enter Size of Replicas: ")
			print("\nEnter data in {} File\n".format(f1))
			time.sleep(2)			
			os.system("vi {}".format(f1))
			os.system("tput setaf 3")
			print("\n  Uploading File....\n")
			os.system("tput setaf 7")
			os.system("hadoop fs -D dfs.replication={} -put {} /".format(s,f1))
			os.system("tput setaf 3")
			print("\n<<< File Uploaded!!! >>>\n")
			os.system("tput setaf 7")
		
		elif (op==8):
			os.system("tput setaf 3")
			print("<\n<< Back to Hadoop Service Menu >>> \n")
			os.system("tput setaf 7")
			f=0
			
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
			f=0


def serviceNode(ip,node,direc):
	os.chdir("/etc/hadoop/")

	#Configuring core-site.xml			
	os.system("echo \"\" > core-site.xml")
	file1 = open("core.txt","w")
	file1.write("<?xml version=\"1.0\"?>")
	file1.write("\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>")
	file1.write("\n<!-- Put site-specific property overrides in this file. -->")
	file1.write("\n\n<configuration>")
	file1.write("\n<property>")
	file1.write("\n<name>fs.default.name</name>")
	file1.write("\n<value>hdfs://{}:9001</value>".format(ip))
	file1.write("\n</property>")
	file1.write("\n</configuration>")
	file1=open("core.txt","r")
	os.system("cp core.txt core-site.xml")
	file1.close()
	print("\ncore-site.xml>>")			
	os.system("cat core-site.xml")	

	#Configuring hdfs-site.xml
	os.system("echo \"\" > hdfs-site.xml")
	file2 = open("hdfs.txt","w")
	file2.write("<?xml version=\"1.0\"?>")
	file2.write("\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>")
	file2.write("\n<!-- Put site-specific property overrides in this file. -->")
	file2.write("\n\n<configuration>")
	file2.write("\n<property>")
	file2.write("\n<name>dfs.{}.dir</name>".format(node))
	file2.write("\n<value>/{}</value>".format(direc))
	file2.write("\n</property>")
	file2.write("\n\n</configuration>")
	file2=open("hdfs.txt","r")	
	os.system("cp hdfs.txt hdfs-site.xml")	
	file2.close()
	print("\ncore-site.xml>>")
	os.system("cat hdfs-site.xml")

	os.chdir("/root/")


if __name__=='__main__':
	main()


	
