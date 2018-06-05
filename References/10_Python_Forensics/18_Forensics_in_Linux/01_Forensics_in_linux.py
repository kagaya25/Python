


"""

Python Forensics in Linux

The major concern of digital investigations is to secure important evidences or data with encryption or any other format. The basic example is storing the passwords. It is therefore necessary to understand the usage of Linux operating system for digital forensic implementation to secure these valuable data.

Information for all the local users are mostly stored in the following two files −

/etc/passwd
etc/shadow
The first one is mandatory, which stores all the passwords. The second file is optional and it stores information about the local users including the hashed passwords.

Issues arise regarding the security issue of storing the password information in a file, which is readable by every user. Therefore, hashed passwords are stored in /etc/passwd, where the content is replaced by a special value "x".

The corresponding hashes have to be looked up in /etc/shadow. The settings in /etc/passwd may override the details in /etc/shadow.

Both the text files in Linux include one entry per line and the entry consists of multiple fields, separated by colons.

The format of /etc/passwd is as follows −

Sr.No.	Field Name & Description
1	
Username

This field consists of the attributes of human-readable format

2	
Password hash

It consists of the password in an encoded form according to the Posix crypt function

If the hash password is saved as empty, then the corresponding user will not require any password to log into the system. If this field contains a value that cannot be generated by the hash algorithm, such as an exclamation mark, then the user cannot log on using a password.

A user with a locked password can still log on using other authentication mechanisms, for example, SSH keys. As mentioned earlier, the special value "x" means that the password hash has to be found in the shadow file.

The password hash includes the following −

Encrypted salt − The encrypted salt helps maintain the screen locks, pins, and passwords.

Numerical user ID − This field denotes the ID of the user. The Linux kernel assigns this user ID to the system.

Numerical group ID − This field refers to the primary group of the user.

Home directory − The new processes are started with a reference of this directory.

Command shell − This optional field denotes the default shell that is to be started after a successful login to the system.

Digital forensics include collecting the information which is relevant to tracking an evidence. Hence, the user ids are useful in maintaining the records.

Using Python, all of this information can be automatically analyzed for the Indicators of Analysis, reconstructing the recent system activity. Tracking is simple and easy with the implementation of Linux Shell.

Python Programming with Linux
Example


"""

import sys
import hashlib
import getpass

def main(argv):
   print '\nUser & Password Storage Program in Linux for forensic detection v.01\n' 
  
   if raw_input('The file ' + sys.argv[1] + ' will be erased or overwrite if 
         it exists .\nDo you wish to continue (Y/n): ') not in ('Y','y') : 
   sys.exit('\nChanges were not recorded\n') 
  
   user_name = raw_input('Please Enter a User Name: ')
   password = hashlib.sha224(getpass.getpass('Please Enter a Password:')).hexdigest()
   
   # Passwords which are hashed  
   try: 
      file_conn = open(sys.argv[1],'w') 
      file_conn.write(user_name + '\n') 
      file_conn.write(password + '\n') 
      file_conn.close() 
   except: 
      sys.exit('There was a problem writing the passwords to file!')
      
if __name__ == "__main__": 
   main(sys.argv[1:])
   
