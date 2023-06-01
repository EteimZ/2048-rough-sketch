# 2048 Rough Sketch

A rough implementation of [2048](https://play2048.co/) in python.

## Folder structure

```bash
src
├── main.py
└── utils.py
```

The `src` folder contains two files:

- `main.py`: This is the main entry file to start the game.
- `utils.py`: This contains functions used in the game of 2028.

## Usage 

```bash
git clone https://github.com/EteimZ/2048-rough-sketch
cd 2048-rough-sketch
python src/main.py
   0|   0|   0|   4
   0|   0|   0|   0
   2|   0|   0|   0
   0|   0|   0|   0
Please press key(w⬆|s⬇|a⬅|d➡|e to exit): 
```

## Gameplay 
Four keys are used to play the game `w`, `s` , `a` and `d`.

`w` moves the grid up.

```code
   2|   0|   0|   4
   0|   0|   0|   0
   0|   0|   0|   0
   0|   0|   2|   0
Please press key(w⬆|s⬇|a⬅|d➡|e to exit): w
```

`s` moves the grid down.

```code
   0|   2|   0|   0
   0|   0|   0|   0
   0|   0|   0|   0
   2|   0|   2|   4                                                                                                             
Please press key(w⬆|s⬇|a⬅|d➡|e to exit): s
```

`a` moves the grid left.

```code
   2|   0|   0|   0                                                                                                               
   0|   0|   0|   0                                                                                                               
   0|   0|   0|   0                                                                                                               
   8|   0|   4|   0                                                                                                           
Please press key(w⬆|s⬇|a⬅|d➡|e to exit): a
```

`d` moves the grid right.

```code
   0|   0|   0|   2                                                                                                               
   0|   0|   0|   0                                                                                                               
   0|   0|   2|   0                                                                                                               
   0|   0|   8|   4                                                                                                           
Please press key(w⬆|s⬇|a⬅|d➡|e to exit): d
```

## Test

Tests have been implemented using [doctest](https://docs.python.org/3/library/doctest.html). Use the command below to run them.

```bash
python src/utils.py # Non verbose test
python src/utils.py -v # verbose test
```
