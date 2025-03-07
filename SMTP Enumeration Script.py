import smtplib

def smtp_enum(target, wordlist):
        for uname in f:
            uname = uname.strip()  
            server = smtplib.SMTP(target, 25)  
            server.ehlo()  
            code, response = server.docmd("VRFY", uname) 
            print("Response for %s: %s" % (uname, response.decode()))  
            server.quit()

if __name__ == "__main__":
    target = input("Target IP or hostname: ")
    wordlist = input("Format: wordlist.txt (assuming wordlist is in the same directory as the script): ")
    smtp_enum(target, wordlist)
