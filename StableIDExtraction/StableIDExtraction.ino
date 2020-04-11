/*This module sends binary ID to the computer for ID generatio
Jubayer
Auburn University
2018
*/

#include <stdio.h>
#include <stdlib.h>
#include <Dump.h>// probably I do not need this
#include <MemoryFree.h>
#include<string.h>
#include <sha256.h>
#include <sha256_config.h>
extern void * __brkval;
extern void * __bss_end;

//--rest function;



//--functions
String PUF();
void authenticate(void);
byte CtoI (char A);
//------
void setup() {
  Serial.begin(9600); 
}
//----------
  int i=0;
  String n="";// nonce
  char trig='k';
//----------
void loop(){
  if(Serial.available()>0 && trig !='g' ){
        trig=Serial.read();
         i=0;
      // if(trig=='g') Serial.println("autneticating....");
         }
         if(trig=='g') authenticate();
          
/*This is user code part*/
//---------------------------

         

//----------------------------
}

String PUF()
{
  int byte_count = 0;
  
  //Serial.println(available_memory);
  uint8_t num = 0;
  int available_memory = freeMemory(); 
  //uint8_t* ramptr = &num1-273; // make this number carefully
  uint8_t* ramptr = &num;
   String ID;
  while (byte_count < available_memory)
          {
            String binary=String(*ramptr,BIN);
            int b=binary.length();
            if (b != 8)
            {
              String temp="00000000";
              temp=temp.substring(0,8-b);
              ID +=(temp+binary);
            }
            else
            {
              ID +=binary;
            }
             ramptr = ramptr - 1; 
             ++byte_count; 
 
            } 
   Serial.println(ID);// remove one ID extraction is done         
// String sorting subroutine
int usCells[66]={};// Array length is used in the later thnig
String R_ID;
//String R_I;
int flag;
int t=3;
byte q=0;
           for(int i=0; i<ID.length()-1; i++) 
           {  flag=0;
             for( int j=0;j<66;j++) {
               if (usCells[j]==i) flag=1;// detect the indecies to discard
             }
              if(flag==0 && (R_ID.length()<64)) {// real dumb mistakes. you converted it to hex remeber
                //R_I+=ID[i];
                //Serial.println(R_ID.length());
                                        //binary integert to hex integer conversion
                byte p=byte(ID[i])-48;// make it 1 or 0
                q=q+(p<<t);//integer concatenation like make the 4 bytes to 1 int
                t=t-1;
                if(t==-1) {//-1 is beause I need total 4 cycle and 5th cycle is breaking
                  t=3;
                  R_ID+=String(q,HEX);// hex ID gerenation. 
                  q=0;
                }                
              }
          }
//Serial.println(R_ID); 
//Serial.println(R_I);
return R_ID;
}
// Ascii to hex character conversion
byte CtoI (char A)
{
  byte c; 
 if (A<='9' &&  A>='0')       c=A-'0';
 else if(A<= 'F' && A>='A')   c=A-55;  // subtract 55 to make it hex
 else if(A<= 'f' && A>='a')   c=A-87; // subratct 87 to make it hex
 else                         return -1;// means the character is not Hex
  return c;
}

void authenticate(){
String K="DF3431F3B8A3C3D0156C7F9B2E3FA8893B47429ACA193F0FABCFA7BF9A7B49C0";// shared key
if(Serial.available()>0){
  
         char A=Serial.read();
          byte a= CtoI (A);
          byte b= CtoI(K.charAt(i));
          i=i+1;
          byte xored=a^b;//might need padding
          n+=String(xored,HEX);// this is your nonce
          if(i==K.length()){
            // nonce is ready to be hashed
            uint8_t *hash;
            char preHash[50] = {0};
            Sha256.init(); 
            Sha256.print(n);
            hash = Sha256.result();
            String p;
            for(byte l=0;l<32;l++) 
            {
              sprintf(preHash,"%02X",hash[l]);
              p+=preHash;
            };
             String ID=PUF();
             String r;
             for(byte index=0;index<64;index++){
               byte b= CtoI(ID[index]);
               byte a= CtoI(p[index]);
               byte xored=a^b;
               r+=String(xored,HEX);
               }
             //Serial.println(r);           
              n="";
              trig='k';
              i=0;
              } // reset i; 
        }
}

