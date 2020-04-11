

/*This is written for Arduino signature 
extration
Jubayer
Auburn Unievrsity
*/
#include <stdio.h>
#include <stdlib.h>
#include <Dump.h>
#include <MemoryFree.h>
#include<string.h>


extern void * __brkval;
extern void * __bss_end;

void PUF(void);

void setup() {
  Serial.begin(9600); 
   PUF();
}

void loop(){}
// PUF ID extraction
void PUF()
{
  int byte_count = 0;
  int available_memory = freeMemory(); 
  uint8_t num = 0;
  uint8_t* ramptr = &num; 
   String ID;
   
  while (byte_count < available_memory) 
          {
              String binary=String(*ramptr,BIN);
              int b=binary.length();
            if (b != 8)
            {   String temp="00000000";
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
            
      Serial.println(ID);
}         
