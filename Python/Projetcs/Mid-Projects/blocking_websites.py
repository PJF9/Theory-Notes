
def get_blocked_websites(host_file_loc=r"C:\Windows\System32\drivers\etc\hosts"):
    with open(host_file_loc, 'r') as host_file:
        return [line.split('\t')[-1][:-1] for line in host_file.readlines() if not line.startswith("#") and line != '\n']


class Web_Site_blocker:

    def __init__(self, host_file_loc=r"C:\Windows\System32\drivers\etc\hosts"):
        self.loc = host_file_loc
        self.redirect = "127.0.0.1"
        self.blocked_website = get_blocked_websites()

    def block_website(self, website):
        if website not in self.blocked_website:
            self.blocked_website.append(website)

            with open(self.loc, 'a') as host_file:
                host_file.write(self.redirect + '\t' + website + '\n')
    
    def allow_website(self, website):
        if website in self.blocked_website:
            with open(self.loc, 'r') as host_file:
                host_content = [line for line in host_file.readlines() if line != (self.redirect + '\t' + website + '\n')]
            with open(self.loc, 'w') as host_file:
                host_file.writelines(host_content)
            self.blocked_website.remove(website)

    def reset_host(self, reset_host_loc):
        with open(reset_host_loc, 'r') as reset_host_file:
            reset_host_content = reset_host_file.read()
        with open(self.loc, 'w') as host_file:
            host_file.write(reset_host_content)
        self.blocked_website = []
