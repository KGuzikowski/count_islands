## By Karol Guzikowski

### Description

I use scipy and numpy for the speed as we know python and its loops can be really slow and scipy and numpy are made with Cython and C.

To be sure that I don't run out of memory and program crashes I use numpy's memmap. I was thinking about using scipy's sparse matrices which would work for huge arrays (meaning it would save memory) it doesn't always guarantee that we will not run out of memory. There are alternatives like Zarr, HDF5, or PyTables but I was asked to use a few libraries as possible so I'm gonna use memmap (even though it's slower in some places).

I assume that the world map is a rectangle.

#### Proof of correctness:
I treat the matrix as a graph and apply modified BFS. I use a priority queue so that when the algorithm stumbles upon an island it will visit each of its vertexes and then move to the sea. So it's obvious that it will always find the correct number of islands.
