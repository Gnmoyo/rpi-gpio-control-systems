#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

BUTTON_1_PIN = 5
BUTTON_2_PIN = 18
LED_PIN = 23


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)


def main():
    setup()
    print("Dual button LED control started. Press Ctrl+C to exit.")

    try:
        while True:
            button_1_pressed = GPIO.input(BUTTON_1_PIN) == GPIO.LOW
            button_2_pressed = GPIO.input(BUTTON_2_PIN) == GPIO.LOW

            if button_1_pressed and button_2_pressed:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("Both buttons pressed -> LED ON")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()