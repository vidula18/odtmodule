from machine import Pin, PWM
import time

# Define motor control pins
IN1 = Pin(14, Pin.OUT)  # Motor direction pin 1
IN2 = Pin(27, Pin.OUT)  # Motor direction pin 2
EN = PWM(Pin(18))       # Enable pin (PWM for speed control)

# Set PWM frequency and duty cycle
EN.freq(1000)

def motor_forward(speed=10):
    """Spin motor forward extremely slowly"""
    IN1.on()
    IN2.off()
    EN.duty(speed)

def motor_backward(speed=10):
    """Spin motor backward extremely slowly"""
    IN1.off()
    IN2.on()
    EN.duty(speed)

def motor_stop():
    """Stop the motor"""
    IN1.off()
    IN2.off()
    EN.duty(0)


while True:
    motor_forward(10)
    time.sleep(3)
    motor_stop()
    time.sleep(1)

    motor_backward(10)
    time.sleep(3)
    motor_stop()
    time.sleep(1)
