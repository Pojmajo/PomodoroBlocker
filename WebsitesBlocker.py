class WebsitesBlocker:
    def __init__(self, websites_list):
        self.__hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        self.__redirect = "127.0.0.1"
        self.__websitesList = websites_list

    def block(self):
        with open(self.__hostsPath, 'r+') as file:
            content = file.read()
            for site in self.__websitesList:
                if site in content:
                    pass
                else:
                    file.write(self.__redirect+" "+site+"\n")

    def unlock(self):
        with open(self.__hostsPath, 'r+') as file:
            content = file.readlines()
            file.seek(8)
            for line in content:
                if not any(site in line for site in self.__websitesList):
                    file.write(line)
                file.truncate()


