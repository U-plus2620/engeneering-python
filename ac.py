#!/usr/bin/python
import math
global power

#global BTU_per_hr
#BTU = raw_input("ENTER Q1 IN BTU/h:     ")

global AREA
AREA = raw_input("ENTER ROOM SIZE IN SQUARE METERS:     ")

global Q2
Q2 = raw_input("ENTER Q2 FACTOR:  (for jerusalem enter 1.35\r\nfor lower areas [like eilat] enter 2.7)    ")

global room_type
room_type = raw_input("For room with working people: 1\r\nFor a non-working room: 2    ")

global COP 
COP = raw_input("ENTER MACHINE C.O.P:  ")

global phase
phase = raw_input("PHASE(enter phases)   ")

global PF
PF=raw_input("ENTER POWER FACTOR   ")


def BTU_per_hr (AREA):
	btu=int(AREA)*700
	return btu
BTU=BTU_per_hr(AREA)
def TR (BTU):            #Tons of Refridgeration
	tr=float(BTU)/12000
	return tr

print("BTU/h -> {} \r\nTR  -> {}".format(BTU,TR(BTU)))

def V (AREA,room_type):
	if int(room_type) == 1:
		factor = 12.8
	elif int(room_type) == 2:
		factor = 1.15
	
	v = float(AREA)*factor
	return v
v=V(AREA,room_type)	
print("air exchange  -> {}".format(v))


def q2 (Q2,v):
	result = v/1000.0 * float(Q2)
	return result

result = q2(Q2,v)

print("Q2 -> {}".format(result))

QT = float(TR(BTU)) + float(result)
power = 3*1.163*QT/float(COP)
print("P={}(KW)".format(power))

def amps(phase, PF):
	if int(phase) == 1:
		ampere = power*1000/(230 * PF)
	elif int(phase) == 3:
		ampere = power*1000/(math.sqrt(3)*float(400)*float(PF))
	print("Ib = {}(A)".format(ampere))
amps(phase, PF)
