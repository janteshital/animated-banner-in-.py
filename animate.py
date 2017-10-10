
import os
import time
#the width of the display the windows console is 79 characters wide.
WIDTH = 79
print("ENTER THE WORD U WANT TO DISPLAY")
message = raw_input().upper()
printedMessage = [ "","","","","","","" ]

#maps to 7 strings, one for each line of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],
                       
                "A" :[ " *** ",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],
					  
				"B" :[ "*****",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*****" ],
						
				"C" :[ "*****",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],
				
				"D" :[ "******",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],
						
					   
               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "F" : [ "******",
					   "*     ",
					   "*     ",
					   "***   ",
					   "*     ",
					   "*     ",
					   "*     "],
					   
				"G" : ["******",
                       "*     ",
                       "*     ",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],
	
						
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 
                       
               "I" : [ " *** ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *   ",
                       " ***  " ],
                       
               "J" : [  "*****",
                        "  *  ",
                        "  *  ",
                        "  *  ",
                        "  *  ",
                        "* *  ",
                        "***  " ],
                       
                
               "K" : [ "*     *",
                       "*   *  ",
                       "* *    ",
                       "*      ",
                       "* *    ",
                       "*   *  ",
                       "*     *" ],
                 
                 
               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],


               "M" : [ "*         *",
                       "* *     * *",
                       "*  *   *  *",
                       "*    *    *",
                       "*         *",
                       "*         *", 
                       "*         *"],
                       
                
               "N" : [ "*       *",
                       "* *     *",
                       "*  *    *",
                       "*   *   *",
                       "*    *  *",
                       "*     * *" ,
                       "*       *"],



               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],
                       
                
               "P" : [ "******",
                       "*    *",
                       "*    *",
                       "******",
                       "*     ",
                       "*     ",
                       "*     " ],
                       
               "Q" : [ "*****  ",
                       "*   *  ",
                       "*   *  ",
                       "*   *  ",
                       "* * *  ",
                       "*   *  ",
                       "***** *" ],
                       
               "R" : [ "****** ",
                       "*    * ",
                       "*    * ",
                       "****** ",
                       "* *    ",
                       "*   *  ",
                       "*     *" ],
                       
                 	   
               "S" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "    *",
                       "    *",
                       "*****" ],
               
               "T" : [ "*******",
                       "   *   ",
                       "   *   ",
                       "   *   ",
                       "   *   ",
                       "   *   ",
                       "   *   " ],
                
               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],
               
                              
               
                
               "V" : [ "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       " *  * ",
                       "   *  " ],
                       
                        
               "W" : [ "*      *",
                       "*      *",
                       "*      *",
                       "*      *",
                       "*   *  *",
                       "* *  * *",
                       "*      *" ],
                       
                        
               "X" : [ "*     *",
                       " *   * ",
                       "  * *  ",
                       "   *   ",
                       "  * *  ",
                       " *   * ",
                       "*     *" ],
                       
                                
               "Y" : [ "*     *",
                       " *   * ",
                       "  * *  ",
                       "   *   ",
                       "   *   ",
                       "   *   ",
                       "   *   " ],
                       
                       
                           
               "Z" : [ "*******",
                       "     * ",
                       "    *  ",
                       "   *   ",
                       "  *    ",
                       " *     ",
                       "*******" ],
                       
                       

                
                            
                       
                       
                       
               
                       


               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               
               }

#build up the printed banner. to do this, the 1st row of thedisplay is created for each character in the message, followed bythe second line, etc..
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

offset = WIDTH
timeout=time.time()+60*0.5
while True:
	if time.time()>timeout:
		break
	else:
		os.system("cls")
		for row in range(7):
			print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
		offset -=1
		
		#start again from the right hand side.
		if offset <= ((len(message)+2)*6) * -1:
			offset = WIDTH
		
		time.sleep(0.05)
    

























