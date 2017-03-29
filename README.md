# microbit-acc
## A graph from result data.
![Alt text](/plots/plot_throw1.png)

## What is this?
  This is a small project, the aim of which was to calculate the distance traveled or the maximum velocity of the microbit board. The only hardware I used was the onboard accelerometer to get the acceleration data.

## Did it work?
  Unfortunately, it's impossible to calculate the distance traveled or the velocity of the chip without making extra assumptions (like the acceleration is always downwards). This is because the change in acceleration is impossible to distinguish from the rotation of the chip. Consider this - the microbit is accelerating 9.8 m/s in x direction (z,y=0), a second later acceleration in x and z is 0 but acceleration in y is now 9.8 m/s. Did the microbit rotate or did it stop accelerating in x and started to accelerate in y?
  
## What do I need to replicate this on my microbit?
 To get the values you need to flash the microbit-code.py on the microbit, which records acceleration values when you press button A, and stops when button B is pressed. To get the values off the microbit I have used [UFS](http://microbit-micropython.readthedocs.io/en/latest/tutorials/storage.html#file-transfer) on my linux machine. Don't forget that to flash the code on the microbit you will need to install micropython (i have used [mu](https://codewith.mu/)), otherwise the microbit won't have access to some libraries. File acc-analysis.py analises the data and give a plot of the values.
