'''
This Script is for gate way of the IoT authentication project
#--------------------
-Jubayer Mahmod
-Hardware security lab
-Auburn Unievrsity
-2018
#--------------------
'''







def authentication(port_number,K,ID_orig):
    import datetime
    import serial
    import hashlib
    import time
    import secrets
    import sys
    
    now=datetime.datetime.now()
    time_='****************'+str(now)+'***************\n'
    write_to_file="record.log"
    log=open(write_to_file,'a+')
    log.write(time_)
    log.write("Device ID: "+str(port_number)+'\n')
    ser = serial.Serial()
    ser.port = "/dev/ttyACM"+str(port_number)
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS     
    ser.parity = serial.PARITY_NONE    
    ser.stopbits = serial.STOPBITS_ONE  
    ser.timeout = None                  
    ser.xonxoff = False                 
    ser.rtscts = False                  
    ser.dsrdtr = False                  
    ser.writeTimeout = None
    noneBits=256;
    def xor_(a,b):
        d=''
        d=hex(int(a,16)^int(b,16))[2:]
        return d
    print("Running Authentication for Edge Device:"+str(port_number))
    
    def authenticate(K):
        n=secrets.randbits(noneBits)
        n=hex(n)[2:].zfill(64)
        t=xor_(K,n);
        try:
            ser.open()
            
        except Exception:
            print("Fatal Error: Failed to open ED's serial Port")
            msg="Fatal Error: Failed to open ED's serial Port\n"
            log.write(msg)
        if ser.isOpen():
            time.sleep(1)# very crucial , do not reduce
            print("Info: ED's serial port opened")
            msg="Info: ED's serial port opened\n"
            log.write(msg)
            
            ser.write(str("g").encode())
            time.sleep(1)# very crucial , do not reduce
            ser.write(t.encode())
            r = ser.readline()
            r = r.decode("ascii").rstrip("\n\r")
            print("Encrypted ID: "+r)
            msg="Encrypted ID: "+r+'\n'
            log.write(msg)
            ser.close()
        else:
            print("Fatal Error: DUT Serial port is not open")
            msg="Fatal Error: DUT Serial port is not open\n"
            log.write(msg)
        h=hashlib.sha256(n.encode('utf-8')).hexdigest()
        ID=xor_(h,r)
        print('Device ID: '+ID)
        return ID


    def RobustID(ID,ID_orig,HD):
        p=0;
        d=hex(int(ID_orig,16)^int(ID,16))
        d=bin(int(d, 16))[2:].zfill(256)
        ID=bin(int(ID, 16))[2:].zfill(256)
        ID_orig=bin(int(ID_orig, 16))[2:].zfill(256)
        misIndex=[];
        RID=""
        j=0;
        for i in range (len(ID)):
            if ID_orig[i] != ID[i]:
                misIndex.append(i);
                j=j+1
            else:
                RID+=ID[i]
        #print(misIndex)
        if j<=HD:
            print("Info: Authetication successfull.")
            msg="Info: Authetication successfull.\n"
            log.write(msg)
            p=1;# inidicated first one is success
            
            
        else:
            print("Error: ED failed authentication.")
            msg='Error: ED failed authentication.\n'
            log.write(msg)
        return RID,p


    ID=authenticate(K)
    #print(ID)
    RID,p=RobustID(ID,ID_orig,16)
    #print(RID)
    HD_=4


    if p==1:
        print("Info: Initiating second authentication")
        msg= "Info: Initiating second authentication"
        log.write(msg)
        time.sleep(1)
        ID=authenticate(K)
        RID_,p=RobustID(ID,ID_orig,16)
        j=0;
        for i in range (len(RID)):
            if RID_[i] != RID[i]:
                j=j+1
        if(j>HD_):
            print("Error: ED failed authentication.")
            msg="Error: ED failed authentication."
            log.write(msg)
    log.close()       


def GetID(port):
    with open('database.txt', 'r') as file:
        for line in file:
            line = line.rstrip("\n\r")  
            if line[0]==str(port):
                ID=line[2:66]
                K=line[67:131]
    return ID,K

#----
i=2
#for i in range(7):   
[ID_orig, K]=GetID(i)
authentication(i,K,ID_orig)







