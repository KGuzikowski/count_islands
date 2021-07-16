## By Karol Guzikowski

### Description

I use scipy and numpy for the speed as we know python and its loops can be really slow and scipy and numpy are made with Cython and C.

To be sure that I don't run out of memory and program crashes I use numpy's memmap. I was thinking about using scipy's sparse matrices which would work for huge arrays (meaning it would save memory) it doesn't always guarantee that we will not run out of memory. There are alternatives like Zarr, HDF5, or PyTables but I was asked to use as few libraries as possible so I'm gonna use memmap (even though it's slower in some places).

I assume that the world map is a rectangle and is correct.

#### Proof of correctness:
I treat the matrix as a graph and apply modified BFS. I use a priority queue so that when the algorithm stumbles upon an island it will visit each of its vertexes and then move to the sea. So it's obvious that it will always find the correct number of islands.

#### Testing
I only tested functions from `utils.py` file. I don't test the BFS part because I provided the proof of correctness above.

#### Running program and tests
To run program do:
```shell script=
chmod +x run.sh
./run.sh
```

Here script will create virtual env and install packages there.

To run tests do:
```shell script=
chmod +x run_tests.sh
./run_tests.sh
```
