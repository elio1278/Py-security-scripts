import whois as ws
class WhoisInfo:
        def print_whois_info(self,host):

            whoisinfo=ws.whois(host)
            print(whoisinfo)

if __name__=="__main__":
        whoisinfo=WhoisInfo()
        whoisinfo.print_whois_info("google.com")
