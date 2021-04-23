# Robot-Likelihood-Simulation
A solution code for Assignment 3 of Probabilistic Robotics Book.

### Dependencies
- python
- numpy
- matplotlib

### Running Assignment 3.1)
Run the file 1.py using any python IDE or simply run the following command:
```python
python 1.py
```

### Running Assignment 3.2)
Run the file 2.py using any python IDE or simply run the following command:
```python
python 2.py
```

### Running Assignment 3.3)
Run the file 3.py using any python IDE or simply run the following command:
```python
python 3.py
```

### Running Assignment 3.4)
Run the file 4.py using any python IDE or simply run the following command:
```python
python 4.py
```

#### Assignment 3.1)
Let a robot be equipped with wheel eencoders and on-board software that transforms the physical measuring data into time-discrete odometry measurements <rot1, trans, rot2>.

Let the robot start at pose <x, y, θ> = <0m, 0m, 0°> and obtain the following subsequent odometry measurements: 
- Motion 1: <-20°, 3m, -30°>
- Motion 2: <20°, 10m, 10°> 

Calculate the resulting pose of the robot, assuming exact measurements.

#### Assignment 3.2)
How would your pose estimate for the first movement look like under the following simple error model? 
1. rot1_hat = rot1 (+ or -) epsilon_rot1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; epsilon_rot1 = 10°
2. trans_hat = trans (+ or -) epsilon_trans &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; epsilon_trans = 0.5m
3. rot2_hat = rot2 (+ or -) epsilon_rot2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; epsilon_rot2 = 5°

Please draw the movements and pose estimates into one diagram!

#### Assignment 3.3)
Visualize the likelihood of positions (x, y) after one, two, and three successive applications of the motion model from 3.2) for Motion 1 by computing the likelihoods on the grid (x, y, θ) and marginalizing out the heading direction θ.

#### Assignment 3.4)
 Initialize 100 samples at <x, y, θ> = <0m, 0m, 0°> 
 
 Show the (x, y)-positions of the samples after one, two, and three successive applications of the motion model from 3.2) for Motion 1.
