# Game of Life Computes Pi

## Live on Shadertoy
https://www.shadertoy.com/view/NdtyW4

## Description
Demonstrates Conway’s Game of Life with a pattern that geometrically 
computes a value related to Pi.

"An arrangement of four breeders that produce Gosper glider guns that 
fire at each other so as to invert each others’ streams"

Looks best in fullscreen (press space to reset) on high-resolution 
displays (> 1080p)

## Controls:
* [W, A, S, D, mouse drag] - camera move
* [UP, DOWN, top-right screen corner] - camera zoom
* [SPACE, botom-right screen corner] - reset

## Features
* Initialized with an interesting Game Of Life pattern
* Mobile-friendly: 60FPS on 2016's Android phone (Mali-G71 MP8)
* Implements data compression to overcome constant values limit 
  (it is especially low on mobiles)
* Relatively efficient branchless code
* SDF rendering of the cells

## The pattern source
"FIGURE 6.43: LIFE COMPUTES PI" "A pattern with population in 
generation t equal to approximately (pi-2)t^2/720"

from "Nathaniel Johnston and Dave Greene - "Conway’s Game of Life: 
Mathematics and Construction"

https://conwaylife.com/book/periodic_circuitry
