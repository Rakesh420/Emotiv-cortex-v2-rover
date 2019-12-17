# Importing the packages and the libraries
from flask import Flask
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

app = Flask(__name__)
tf=0.8
# Function to initialise the gpio channels
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(26,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(21,gpio.OUT)

# Pivot rover to the forward
@app.route('/forward')
def forward():
 init()
 gpio.output(17, True)
 gpio.output(26, False)
 gpio.output(22, False) 
 gpio.output(21, True)
 return 'moved forward'
 
# Pivot rover to the right
@app.route('/pivot_right')
def pivot_right():
    init()
    gpio.output(17,True)
    gpio.output(26,False)
    gpio.output(22,False)
    gpio.output(21,True)
    time.sleep(tf)
    gpio.cleanup()
    
    return 'pivoted right'

# Pivot rover to the left
@app.route('/pivot_left')
def pivot_left():
    init()
    gpio.output(17,True)
    gpio.output(26,True)
    gpio.output(22,False)
    gpio.output(21,True)
    return 'pivoted left'

# Stop rover
@app.route('/stop_rover')
def stop_rover():    
    init()
    gpio.output(17, False)
    gpio.output(26, False)
    gpio.output(22, False) 
    gpio.output(21, False)
    return 'Rover stopped'

    
@app.route('/')
def index():
    return 'Control Rover'

if __name__ == '__main__':   
    app.run(debug=True,host='0.0.0.0')
