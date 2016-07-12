# physics-simulations

2d_Heat_Model.py - Part of project at McGill Physics Hackathon 2016

Models the heat equation as seen here: https://en.wikipedia.org/wiki/Heat_equation , given an initial 2d - gaussian distribution centered at 0 with variance of 0.1. Parameter alpha describes how fast heat is lost. The Laplacian is calculated with a finite difference of nearby units, overwrapping the edges is done to prevent the boundary conditions, which are arbitrary and do not change, from overpowering the simulation. 
