#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

BUTTON_PIN = 5
LED_PIN = 18


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)


def main():
    setup()
    print("Button LED control started. Press Ctrl+C to exit.")

    try:
        while True:
            button_pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW

            if button_pressed:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("Button pressed -> LED ON")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()