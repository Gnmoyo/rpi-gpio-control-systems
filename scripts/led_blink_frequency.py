#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

BUTTON_1_PIN = 18
BUTTON_2_PIN = 5
LED_PIN = 23

blink_delay = None


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)


def main():
    global blink_delay

    setup()
    print("LED frequency control started.")
    print("Button 1 -> 1 Hz blinking")
    print("Button 2 -> 2 Hz blinking")
    print("Press Ctrl+C to exit.")

    led_state = False

    try:
        while True:
            button_1_pressed = GPIO.input(BUTTON_1_PIN) == GPIO.LOW
            button_2_pressed = GPIO.input(BUTTON_2_PIN) == GPIO.LOW

            if button_1_pressed:
                blink_delay = 0.5
                print("1 Hz blinking selected")
                time.sleep(0.2)

            elif button_2_pressed:
                blink_delay = 0.25
                print("2 Hz blinking selected")
                time.sleep(0.2)

            if blink_delay is not None:
                led_state = not led_state
                GPIO.output(LED_PIN, led_state)
                time.sleep(blink_delay)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()