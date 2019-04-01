# engineering-python
A suite of electrical engineering tools, written in Python.

## Installation
Just clone the git repo

## Usage
ac.py is a tool for making approximate calculations for air condition size
for a given room
The arguments for this program are:

light_calc.py is a program to calculate the amount of light fixtures necessary for a given area,
given the necessary lux and the given lumens that each light gives off.
The arguments for the program are given via the command line.
The program calculates formula given by dime budensky in his book on power and lighting.
Please note that all lengths are given in meters.
the calculation is:
    (lux\*room_size\*constant)/(k\*Fu\*lumens)
The command line arguments a and b are the two sides of the area resulting in the room_size(in meters!)
Lux is the necessary lux needed for the given area.
Lumens are the lumens given off by each fixture.
Constant is a mathematical constant.
k is the dust accumulation coefficient
k has been given an average value hard coded in the script which you can change if you know the coefficient value.
Fu is the light reflection coefficient (in percentage).
Fu has been given an average value hard coded in the script which you can change if you know the reflection value.

## Contributing
How to get started with local development of this project.

## License
Pick an open-source license and put it here
  
