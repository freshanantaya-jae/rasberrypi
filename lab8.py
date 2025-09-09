from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

# กำหนด GPIO Pin สำหรับมอเตอร์
motor_left_forward = 17
motor_left_backward = 18
motor_right_forward = 22
motor_right_backward = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_left_forward, GPIO.OUT)
GPIO.setup(motor_left_backward, GPIO.OUT)
GPIO.setup(motor_right_forward, GPIO.OUT)
GPIO.setup(motor_right_backward, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

app = Flask(__name__)

def stop():
    GPIO.output(motor_left_forward, False)
    GPIO.output(motor_left_backward, False)
    GPIO.output(motor_right_forward, False)
    GPIO.output(motor_right_backward, False)

def forward():
    GPIO.output(motor_left_forward, True)
    GPIO.output(motor_left_backward, False)
    GPIO.output(motor_right_forward, True)
    GPIO.output(motor_right_backward, False)

def backward():
    GPIO.output(motor_left_forward, False)
    GPIO.output(motor_left_backward, True)
    GPIO.output(motor_right_forward, False)
    GPIO.output(motor_right_backward, True)

def left():
    GPIO.output(motor_left_forward, False)
    GPIO.output(motor_left_backward, True)
    GPIO.output(motor_right_forward, True)
    GPIO.output(motor_right_backward, False)

def right():
    GPIO.output(motor_left_forward, True)
    GPIO.output(motor_left_backward, False)
    GPIO.output(motor_right_forward, False)
    GPIO.output(motor_right_backward, True)

def distance():
    # วัดระยะด้วย Ultrasonic Sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    dist = pulse_duration * 17150
    return dist

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command/<action>")
def command(action):
    dist = distance()
    if dist < 15:   
        stop()
        return "Obstacle detected!"
    else:
        if action == "forward":
            forward()
        elif action == "backward":
            backward()
        elif action == "left":
            left()
        elif action == "right":
            right()
        elif action == "stop":
            stop()
        return f"Action: {action}"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
