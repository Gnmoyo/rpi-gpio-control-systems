# Raspberry Pi GPIO Control Systems

> Embedded control system examples using Raspberry Pi GPIO for real-time input handling and output control in Python.

---

## Overview

This project demonstrates **basic embedded system design principles** using a Raspberry Pi, focusing on digital input/output (GPIO) control.

The system implements multiple control scenarios using buttons and LEDs, simulating real-time interaction between sensors (inputs) and actuators (outputs).

---

## Key Features

* Digital input handling using GPIO buttons
* Digital output control using LEDs
* Real-time polling-based control loops
* Multi-input logic (AND conditions)
* Frequency-based LED control
* Timed output sequencing

---

## Technologies Used

* Python
* Raspberry Pi GPIO (RPi.GPIO)
* Linux (Raspberry Pi OS)

---

## Implemented Systems

### 1. Button-Controlled LED

* Pressing a button turns an LED on
* Demonstrates basic input → output mapping

📁 `scripts/button_led_control.py`

---

### 2. Dual Button Control

* LED activates only when **two buttons are pressed simultaneously**
* Demonstrates logical AND condition in embedded systems

📁 `scripts/dual_button_led_control.py`

---

### 3. Frequency-Based LED Control

* Button 1 → LED blinks at **1 Hz**
* Button 2 → LED blinks at **2 Hz**
* Demonstrates timing and frequency control

📁 `scripts/led_blink_frequency.py`

---

### 4. LED Sequence Control

* LEDs switch states in a timed sequence
* Demonstrates state-based control and timing logic

📁 `scripts/led_sequence_control.py`

---

## Project Structure

```
.
├── scripts/        # Python control programs
├── docs/           # Lab summaries and explanations
├── notes/          # Reconstruction notes
└── README.md
```

---

## Embedded Systems Concepts Demonstrated

* GPIO configuration (input/output modes)
* Pull-up resistor usage
* Polling vs event-driven design
* Real-time control loops
* Timing and delay handling
* State-based system behavior

---

## Notes

This project is based on laboratory work involving Raspberry Pi microcontrollers and has been **cleaned and restructured** to present the core embedded system concepts clearly.

---

## Author

**Gugulethu Moyo**
Mechatronics, Robotics & Automation Engineering

