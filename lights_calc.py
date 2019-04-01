#!/usr/bin/python
import math
import sys
import getopt



global Fu
global num_of_fixtures
global k
global lx_result_roundDown
global lx_result_roundUp
global lux
global room_size
global lum
global const



k=0.7
Fu=50
const=100

def usage():
	print("usage {} --lux --area --lum [-k,--Fu]\n ".format(sys.argv[0]))
	print("--lux  => is the necessary lux for given area.")
	print("--area => is the size of the area given in square meters.")
	print("--lum  => is the lumen's given off by a given light fixture.")
	print("-k     => is the dust acumalation coefficient (that acumalates on the fixture)\n\tThis value is hard coded to an average value but could optionaly be changed using the -k argument")
	print("--Fu   => is the coefficient of reflection that is reflected off by the walls")
	exit()

def light_calc(lux,area,Fu,k,lum):
	print(" lux => {}\n area => {}\n lum => {}\n k => {}\n Fu => {}".format(lux,area,lum,k,Fu))
	equation=(lux*area*const)/(k*Fu*lum)
	result=equation
	num_of_fixtures_down=math.floor(result)
	num_of_fixtures_up=math.ceil(result)
	lx_result_roundDown=(num_of_fixtures_down*k*Fu*lum)/(area*const)
	lx_result_roundUp=(num_of_fixtures_up*k*Fu*lum)/(area*const)
	print("\nresult {}\n \n\tactual number of fixtures:\n  \t\tRounded down {},\n  \t\tRounded up   {}\n \tactual lux level:\n  \t\tRounded down {}\n  \t\tRounded up   {}".format(result,num_of_fixtures_down,num_of_fixtures_up,lx_result_roundDown,lx_result_roundUp))

try:
    opts, args = getopt.getopt(sys.argv[1:],"k:",["help","lux=","lum=","Fu=","area="])
except getopt.GetoptError as err:
    print(str(err))
    usage()
if not sys.argv[1:]:
	usage()

for o,a in opts:
    if o in ('--help'):
        usage()
    elif o in ('-k'):
       k=int(a)
    elif o in ('--lux'):
        lux=int(a)
    elif o in ('--lum'):
	lum=int(a)
    elif o in ('--area'):
	area=int(a)
    elif o in ('--Fu'):
	Fu=int(a)






	#power_up  = 
	#amp_up    =
	#power_down=
	#amp_down  =	

light_calc(lux,area,lum,Fu,k)

