import sys
import os
import subprocess
import signal
import time
from TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK import *
from TEST_DOORS_UNLOCK_WITH_LOW_BATTERY import *
from TEST_DOORS_LOCK_WHEN_DOOR_OPENED import *
output = None
test = None

def precondition(test):
    test.defineCheckPoints("UNLOCK_FRONT_LEFT", "DoorModule::lockDoors FRONT_LEFT")
    test.defineCheckPoints("UNLOCK_BOOT", "DoorModule::unlockDoors BOOT")
    test.defineCheckPoints("OPEN_FRONT_LEFT", "DoorModule::changeOpeningState: 1 on FRONT_LEFT")
    test.defineCheckPoints("CLOSE_FRONT_LEFT", "DoorModule::changeOpeningState: 0 on FRONT_LEFT")
    test.defineCheckPoints("OPEN_BOOT", "DoorModule::changeOpeningState: 1 on BOOT")
    test.defineCheckPoints("CLOSE_BOOT", "DoorModule::changeOpeningState: 0 on BOOT")
    test.defineCheckPoints("LOCK_FRONT_LEFT", "DoorModule::lockDoors FRONT_LEFT")
    test.defineCheckPoints("LOCK_BOOT", "DoorModule::lockDoors BOOT")
    output = subprocess.Popen(["D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\Debug\OSCAR.exe"], stdout=subprocess.PIPE)
    print "OAM STARTED"
    return output

def precondition_TEST_UNLOCK_WITH_LOW_BATERY_START(test):
    test.defineCheckPoints("UNLOCK", "DoorModule::unlockDoors")
    test.defineCheckPoints("ALARM_RAISED", "WCM::execute: BATTERY_LOW")
    test.defineCheckPoints("LOCK_UNAVAILABLE", "DoorModule::lockDoors: doors cannot be lock due to battery low")

def precondition_TEST_DOORS_LOCK_WHEN_DOOR_OPENED(test):
    test.defineCheckPoints("UNLOCK", "DoorModule::unlockDoors")
    test.defineCheckPoints("OPEN_FRONT_LEFT", "DoorModule::changeOpeningState: 1 on FRONT_LEFT")
    test.defineCheckPoints("LOCK_UNAVAILABLE", "DoorModule::lockDoors: doors cannot be lock due to opened")

def postcondition(process):
    process.terminate()

def TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK_START():
    print "TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK_START"
    test = TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK("UNBLOCK_LOCK_DOORS")
    process = precondition(test)
    time.sleep(5)
    test.startTest()
    time.sleep(2)
    postcondition(process)
    time.sleep(5)
    print "TEST DONE. CHECKING POINTS"
    test.checkInLogs()

def TEST_UNLOCK_WITH_LOW_BATERY_START():
    print "TEST_UNLOCK_WITH_LOW_BATERY_START"
    test = TEST_DOORS_UNLOCK_WITH_LOW_BATTERY()
    precondition_TEST_UNLOCK_WITH_LOW_BATERY_START(test)
    output = subprocess.Popen(["D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\Debug\OSCAR.exe"], stdout=subprocess.PIPE)
    print "OAM STARTED"
    time.sleep(5)
    test.startTest()
    time.sleep(2)
    postcondition(output)
    time.sleep(5)
    print "TEST DONE. CHECKING POINTS"
    test.checkInLogs()

def TEST_DOORS_LOCK_WHEN_DOOR_OPENED_START():
    print "TEST_DOORS_LOCK_WHEN_DOOR_OPENED_START"
    test = TEST_DOORS_LOCK_WHEN_DOOR_OPENED()
    precondition_TEST_DOORS_LOCK_WHEN_DOOR_OPENED(test)
    output = subprocess.Popen(["D:\private\OSCAR\New_Architecture_OSCAR\OSCAR\Debug\OSCAR.exe"], stdout=subprocess.PIPE)
    print "OAM STARTED"
    time.sleep(5)
    test.startTest()
    time.sleep(2)
    postcondition(output)
    time.sleep(5)
    print "TEST DONE. CHECKING POINTS"
    test.checkInLogs()

def main():
    TEST_DOORS_UNLOCK_OPEN_CLOSE_LOCK_START()
    print "*********************************"
    #TEST_UNLOCK_WITH_LOW_BATERY_START()
    print "*********************************"
    #TEST_DOORS_LOCK_WHEN_DOOR_OPENED_START()
    print "*********************************"
    print "DONE"
    #DODAC funkcje przenoszaca  zapisujaca logi


if __name__ == "__main__":
    main()