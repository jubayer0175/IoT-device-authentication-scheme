''''
Project title:(HOST demo 2019) Remote Authentication of Low-Cost Devices using Unclonable IDs
Instruction directory in notebook: IoT authentication journal

Jubayer Mahmod
Auburn university
Date: 4/17/2019
Note: delete all text file before running.
'''''


import serial
import time


DUT_serial="COM12"
power_serial="COM6"

bytes_=42 ## number of bytes in the arduino code

write_to_file_path="FullRam.txt"
ser = serial.Serial()
ser.port = DUT_serial
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS     
ser.parity = serial.PARITY_NONE    
ser.stopbits = serial.STOPBITS_ONE  
ser.timeout = None                  
ser.xonxoff = False                 
ser.rtscts = False                  
ser.dsrdtr = False                  
ser.writeTimeout = None             
try:
    ser.open()
except Exception:
    print("Fatal Error: Failed to open DUT`s serial Port")
if ser.isOpen():
    print("Info: DUT`s serial port is opened")
    print("............Collecting data..........")
    #write_to_file_path = file+str(i)+type_
    output_file = open(write_to_file_path, "w")
    line = ser.readline()
    line = line.decode("ascii")
    line=line.rstrip("\n\r")
    output_file.write(line)
    ser.flush()
    ser.close()
    output_file.close()
else:
    print("Fatal Error: DUT Serial port is not open")
print("Load the full program: StableIDExtraction.ino")

cl= input("Once completed press y:")
if(cl=='Y' or cl=='y'):
    print('Info: Initiating extraction')
    try:
        ser.open()
    except Exception:
        print("Fatal Error: Failed to open ED's serial Port")
    if ser.isOpen():
        time.sleep(1)# very crucial , do not reduce
        print("Info: ED's serial port is opened")
        ser.write(str("g").encode())
        time.sleep(1)# very crucial , do not reduce
        print("............Collecting data..........")
        ser.write("DF3431F3B8A3C3D0156C7F9B2E3FA8893B47429ACA193F0FABCFA7BF9A7B49C0".encode())
        r = ser.readline()
        r = r.decode("ascii").rstrip("\n\r")
        write_to_file_path1="ID_1.txt"
        output_file = open(write_to_file_path1, "w")
        output_file.write(r)
        ser.flush()
        ser.close()
        output_file.close()
        print("ID extraction complete")
    else:
        print("Fatal Error: DUT Serial port is not open")

else:
    print("Error: Pressed wrong Key. Press Y or Ctrl+C to abort")

##
with open("FullRam.txt") as infile:
    for line in infile:
        emptyRam=line
        print("Number of bits in RAM: "+str(len(emptyRam)))
#print(emptyRam)
with open("ID_1.txt") as infile:
    for line2 in infile:
        notEmptyRam=line2
        print("Number of bits in RAM: "+str(len(notEmptyRam)))

strlen1=len(notEmptyRam)
midIndex=  int(round(strlen1/2))
SrcStringlen=2
l1=1 # dummy value
inc=1
while l1 !=-1:
    seedstr=emptyRam[(midIndex-SrcStringlen):(midIndex+SrcStringlen)] 
    SrcStringlen= SrcStringlen+inc
    #print("working")
    l1= notEmptyRam.find(seedstr)
    newSrcStringlen=SrcStringlen-2*inc
neWseedStr=emptyRam[(midIndex-newSrcStringlen):(midIndex+newSrcStringlen)] 
l2= notEmptyRam.find(neWseedStr)
#print (l2) 
#go for lower limit
flag=1# dummy
i=1
while flag !=-1 and l2>=0:
    flag=emptyRam.find(notEmptyRam[l2:l2+2*newSrcStringlen])
    l2=l2-1
#print ('lower limit:'+str(l2+1))
flagHigh=1 # dummy
j=1
while flagHigh !=-1 and l2+1+2*newSrcStringlen+j<= strlen1:
    flagHigh=emptyRam.find(notEmptyRam[(l2+1):l2+1+2*newSrcStringlen+j])
    j=j+1
#print ('higher limit:',l2+1+2*newSrcStringlen+j-1)    
HL=strlen1-(l2+1)
LL=strlen1-(l2+1+2*newSrcStringlen+j-1)
print('lower limit:'+str(LL))
print('higher limit:'+str(HL))
g=int((LL+HL)/16)

print('ID extarction starts from:'+ str(g-(bytes_/2)))
##replace &num with a corrected one.
with open('./StableIDExtraction/StableIDExtraction.ino', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('&num', '&num-'+str(int(g-(bytes_/2))))
filedata = filedata.replace('int available_memory = freeMemory();',' ')
filedata = filedata.replace('available_memory',str(bytes_))

with open('./StableIDExtraction_ready/StableIDExtraction_ready.ino', 'w') as file:
    file.write(filedata)
##data collection unit.
  
print("1. Load the file:StableIDExtraction_ready.ino in to DUT ")
print("2. Connect the power down system")
input("3. Press y: ")
if(cl=='Y' or cl=='y'):
    print('Info: Initiating stable ID generation')
    file= "Data_";
    type_=".txt"
    i='1'
    dataset=200; # How many samples
    def collectData():
        ser = serial.Serial()
        ser.port = DUT_serial
        ser.baudrate = 9600
        ser.bytesize = serial.EIGHTBITS     
        ser.parity = serial.PARITY_NONE    
        ser.stopbits = serial.STOPBITS_ONE  
        ser.timeout = None                  
        ser.xonxoff = False                 
        ser.rtscts = False                  
        ser.dsrdtr = False                  
        ser.writeTimeout = None             
        try:
            ser.open()
        except Exception:
            print("Fatal Error: Failed to open DUT`s serial Port")
        if ser.isOpen():
            print("Info: DUT`s serial port is opened")
            print("............Collecting data..........")
            write_to_file_path = file+str(i)+type_
            output_file = open(write_to_file_path, "w")
            time.sleep(1)# very crucial , do not reduce
            print("Info: ED's serial port is opened")
            ser.write(str("g").encode())
            time.sleep(1)# very crucial , do not reduce
            print("............Collecting data..........")
            ser.write("DF3431F3B8A3C3D0156C7F9B2E3FA8893B47429ACA193F0FABCFA7BF9A7B49C0".encode())
            r = ser.readline()
            r = r.decode("ascii").rstrip("\n\r")
            output_file.write(r)
            ser.flush()
            ser.close()
            output_file.close()
        else:
            print("Fatal Error: DUT Serial port is not open")         
    def powerCtrl():
        ser1 = serial.Serial()
        ser1.port =power_serial
        ser1.baudrate = 9600
        ser1.bytesize = serial.EIGHTBITS     
        ser1.parity = serial.PARITY_NONE    
        ser1.stopbits = serial.STOPBITS_ONE  
        ser1.timeout = None                  
        ser1.xonxoff = False                 
        ser1.rtscts = False                  
        ser1.dsrdtr = False                  
        ser1.writeTimeout = None
        try:
            ser1.open()
        except:
            print("Fatal Error: Faliled to open->Power Control Port")
        if ser1.isOpen():
            a = "s"
            ser1.write(str(a.strip()).encode())
            print("Info: DUT power is ON!");
            time.sleep(2) 
            collectData()
            a = "a" 
            ser1.write(str(a.strip()).encode())
            print("Info: DUT power is OFF!")
            time.sleep(5);
            print("Info: This session is complete")
            ser1.flush()
            ser1.close()
    print("Note: Make sure all the devices are powered on")
    print ("Initiating data collection in ")
    
    for i in range(5,0,-1):
        time.sleep(1)
        print (str(i)+" seconds" )
    print("started.......")
    for i in range(dataset):
        print("Info: Starting New session")
        print("Info: Estimated required:"+str((dataset-i)*2.12)+ "min")
        powerCtrl()
        print("Info: Session compeleted: "+ str(i+1))
    print("info: Complete!") 
#-------------------------------------------------------------
else: 
    print("Error")
#----
import numpy as np
dataSmpl=2# starting from  0
#prepare the Raw_data_set_for proceessing
output=open("data_stack.txt", 'w')
for i in range(dataSmpl):
    with open('Data_'+str(i)+'.txt') as f:
        lines = f.readlines()
        linString=list(''.join(lines).strip("*-"))#strip markers
        for item in linString:
            output.write("{}\t".format(item))
        output.write("\n")
output.close()  
count = 0
a=0;
print("Info: Done with text processing")
for line in open("data_stack.txt").readlines( ):
    count += 1 #counts the number of lines
## mathematical operation
with open('data_stack.txt','r') as f1:
    for i in range(count) :
        line=f1.readline().strip()# delete /n
        b=line.split("\t") #/ delete \t in a list
        b = list(map(int, b))# make an array
        a=np.add(a, b)
#stability
stbl=0;
usCells=[]
ID=""
print("Info: Running Stability calculation...")
for i in range (len(a)):
    if (a[i]==max(a)) or (a[i]==0):
        stbl+=1
        ID+=str(int(a[i]/max(a)))# device signature
    else:
        usCells.append(i)
print("Stbale bits:"+str(stbl/len(a))+"%")
print("Unstable Bit locations:")
replace='int usCells[66]='+'{'+str(usCells).strip('[]')+'};'
print(replace)
with open('./StableIDExtraction/StableIDExtraction.ino', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('&num', '&num-'+str(int(g-(bytes_/2))))
#filedata = filedata.replace('&num', '&num-'+str(int(20)))
filedata = filedata.replace('int usCells[66]={};', replace)
filedata = filedata.replace('Serial.println(ID);', '//Serial.println(ID);')
filedata = filedata.replace('//Serial.println(r);', 'Serial.println(r);')
filedata = filedata.replace('int available_memory = freeMemory();',' ')
filedata = filedata.replace('available_memory',str(bytes_))
with open('./ED/ED.ino', 'w') as file:
    file.write(filedata)

import hashlib
import secrets
cl=input("Load Edge device program and press y:")
if(cl=='Y' or cl=='y'):
    ser = serial.Serial()
    ser.port = DUT_serial
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
        d=hex(int(a,16)^int(b,16))[2:]## could lead to pading problem. keep an eye
        return d
    
    K="DF3431F3B8A3C3D0156C7F9B2E3FA8893B47429ACA193F0FABCFA7BF9A7B49C0"
    #ID_orig='faf93db73bff7f7fbd77beffffafcefadce7fcdd7dfff3eff6be737fa77ef31d' #D1
    #ID_orig='f9b39ed76eb737ddf9e5b5bbebaf7f51ef7ef5bfa3bfeffee7f7dd5bfdcdb4aa' #D3
    
    n=secrets.randbits(noneBits)
    n=hex(n)[2:].zfill(64)
    t=xor_(K,n);
    try:
        ser.open()
        
    except Exception:
        print("Fatal Error: Failed to open ED's serial Port")
    if ser.isOpen():
        time.sleep(1)# very crucial , do not reduce
        print("Info: ED's serial port is opened")
        ser.write(str("g").encode())
        print("Info: Sending nonce")
        time.sleep(1)# very crucial , do not reduce
        ser.write(t.encode())
        r = ser.readline()
        r = r.decode("ascii").rstrip("\n\r")
        ser.close()
    else:
        print("Fatal Error: DUT Serial port is not open")
    
    h=hashlib.sha256(n.encode('utf-8')).hexdigest()
    ID=xor_(h,r)
    print('Device ID: '+ID)



## hamming stuff:




    


