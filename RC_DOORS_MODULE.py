import os


DOOR_LABELS = {"FRONT_LEFT":"0", "FRONT_RIGHT":"1", "BACK_LEFT":"2", "BACK_RIGHT":"3", "MASK":"4", "BOOT":"5"}

class RC_DOORS_MODULE:

    def __init__(self):
        self.sn = "9999"
        self.can_recv_file = "D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\System\CAN_recv.txt"
        self.can_send_file = "D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\System\CAN_send.txt"
        self.ar_file = "D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\System\AR.txt"
        self.ar_content = "ACCESS REQUEST"
        self.rc_domain = "0x00"
        self.doors_domain = "0x01"

    def sendMessage(self, message):
        if not os.path.isfile(self.can_recv_file):
            f = open(self.can_recv_file, "w")
            f.write(message)
            f.close()

    def waitForReceiveAndDelete(self):
        while not os.path.isfile("D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\System\CAN_recv.txt"):
            return True

    def unlockDoors(self, batery_level):
        msg = self.rc_domain + self.sn + str(batery_level) + "00"
        self.sendMessage(msg)

    def lockDoors(self, batery_level):
        msg = self.rc_domain + self.sn  + str(batery_level) + "01"
        self.sendMessage(msg)

    def openDoor(self, label):
        msg = self.doors_domain + "0" + DOOR_LABELS[label] + "1"
        self.sendMessage(msg)

    def closeDoor(self, label):
        msg = self.doors_domain + "0" + DOOR_LABELS[label] + "0"
        self.sendMessage(msg)