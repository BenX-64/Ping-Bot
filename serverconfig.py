import serveruser

class serverconfig:
    global mode
    global hostility
    global maxwarnings
    mode = 0
    hostility = 0
    maxwarnings = 0
    channel_whitelist = {} #set
    user_id_whitelist = {} #set
    user_list = {} #dict

    def __init__(self, mode, hostility, maxwarnings):
        self.mode = mode
        self.hostility = hostility
        self.maxwarnings = maxwarnings  

    def setMode(self,mode):
        self.mode = mode
    def setHostility(self, hostility):
        self.hostility = hostility
    def setMaxwarnings(self, maxwarnings):
        self.maxwarnings = maxwarnings

