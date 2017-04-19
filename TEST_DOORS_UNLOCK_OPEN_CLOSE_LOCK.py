

from RC_DOORS_MODULE import *
import time

class TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK:

    def __init__(self, name):
        self.name = name
        self.checkPoints = {}
        self.numberOfCheckPoints = 0
        self.checkPointsFailed = []

    def defineCheckPoints(self, label, log):
        self.checkPoints[label] = log
        self.numberOfCheckPoints += 1

    def checkInLogs(self):
        print "CHECKPOINTS to check: ", self.numberOfCheckPoints
        f = open("D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\Logs\SYSLOG_0.log", "r")
        content = f.readlines()
        f.close()
        #print content
        for label in self.checkPoints:
            print "CHECK IS " + label + " EXIST"
            for line in content:
                if line.find(self.checkPoints[label]) != -1:
                    print "PASS"
                    break


    def startTest(self):
        rc_doors_module = RC_DOORS_MODULE()
        rc_doors_module.unlockDoors(90)
        rc_doors_module.waitForReceiveAndDelete()
        time.sleep(2)
        rc_doors_module.openDoor("FRONT_LEFT")
        rc_doors_module.waitForReceiveAndDelete()
        time.sleep(2)
        rc_doors_module.closeDoor("FRONT_LEFT")
        rc_doors_module.waitForReceiveAndDelete()
        time.sleep(2)
        rc_doors_module.openDoor("BOOT")
        rc_doors_module.waitForReceiveAndDelete()
        time.sleep(2)
        rc_doors_module.closeDoor("BOOT")
        rc_doors_module.waitForReceiveAndDelete()
        time.sleep(2)
        rc_doors_module.lockDoors(90)
