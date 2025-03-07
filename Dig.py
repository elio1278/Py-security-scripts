import dns.resolver

class DigInfo:
    def print_dig_info(self, host, record_type):
        try:
            answers = dns.resolver.resolve(host, record_type)
            for rdata in answers:
                print(rdata) 
        except dns.resolver.NoAnswer:
            print(f"No records found for {host} with type {record_type}")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {host} does not exist")
        except dns.exception.Timeout:
            print(f"Query timed out for {host}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    diginfo = DigInfo()
    diginfo.print_dig_info("google.com", "A")
