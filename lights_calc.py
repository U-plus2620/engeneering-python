#!/usr/bin/python
import math
import sys



print("usage {} lux a b lum".format(sys.argv[0]))


global lx
lx=int(sys.argv[1])
global lx_result_roundDown
global lx_result_roundUp
global num_of_fixtures
global k
k=0.7
global Fu
Fu=50
global a
a=float(sys.argv[2])
global b
b=float(sys.argv[3])
global lum
lum=int(sys.argv[4])
global const
const=100

print(" lx => {}\n a => {}\n b => {}\n lum => {}".format(lx,a,b,lum))
def light_calc(lx,a,b,lum):
	equation=(lx*a*b*const)/(k*Fu*lum)
	result=equation
	num_of_fixtures_down=math.floor(equation)
	num_of_fixtures_up=math.ceil(result)
	lx_result_roundDown=(num_of_fixtures_down*k*Fu*lum)/(a*b*const)
	lx_result_roundUp=(num_of_fixtures_up*k*Fu*lum)/(a*b*const)
	print("result {}\n actual number of fixtures:\n  Rounded down {},\n  Rounded up   {}\n actual lux level:\n  Rounded down {}\n  Rounded up   {}".format(result,num_of_fixtures_down,num_of_fixtures_up,lx_result_roundDown,lx_result_roundUp))
	#power_up  = 
	#amp_up    =
	#power_down=
	#amp_down  =	

light_calc(lx,a,b,lum)
