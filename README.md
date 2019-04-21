# engineering-python
A suite of electrical engineering tools, written in Python.

## Installation
Just clone the git repo

## Included Tools

### `ac.py`
`ac.py` is a tool for making approximate calculations for air condition size
for a given room
The arguments for this program are:

### `light_calc.py`

`light_calc.py` is a program to calculate the amount of light fixtures necessary for a given area,
given the necessary lux and the given lumens that each light gives off.

The arguments for the program are given via the command line.
> Note that all lengths are given in meters.

The command line arguments a and b are the two sides of the area resulting in the room_size(in meters!)

```bash
light_calc.py --lux --area --lum [-k,--Fu] 
```

* `--lux` lux amount 
* `--area` Room area in square meters> 
* `--lum` The lumens given off by each fixture
* `-k` (Optional) - See below
* `--Fu` (Optional) - See below


#### Formula

The formula used is by Dimah Budensky in his book on power and lighting:

```
(lux * room_size * constant) / (k * Fu * lumens)
```

Where:

- `Lux` is the necessary lux needed for the given area.
- `Lumens` are the lumens given off by each fixture.
- `Constant` is a mathematical constant, whose value is always `100`
- `k` is the Light Loss Factor which is calculated by dust accumalation and  Wear-and-Tear of the fixture, and is close to 0.8 in a less dusty place and 0.6 in a very dusty place.
> `k` has been given an average value hard coded in the script which you can change if you know the coefficient value.
- `Fu` is the Utilization Factor which is calculated by the reflection of light from the walls, floor and ceiling.
> `Fu` has been given an average value hard coded in the script. This value may be found in the lights' spec sheets and then could be changed on the command line.


## Contributing
How to get started with local development of this project.

## License
Pick an open-source license and put it here
  
