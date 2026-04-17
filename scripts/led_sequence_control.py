#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

GREEN_LED_PIN = 18
RED_LED_PIN = 12


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.LOW)


def main():
    setup()
    print("LED sequence control started. Press Ctrl+C to exit.")

    try:
        while True:
            # Both ON
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            print("Both LEDs ON")
            time.sleep(2)

            # Red only
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            print("Red LED ON")
            time.sleep(2)

            # Green only
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            print("Green LED ON")
            time.sleep(2)

            # Both OFF
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            print("Both LEDs OFF")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()