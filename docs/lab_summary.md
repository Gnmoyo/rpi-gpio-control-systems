# GPIO Control Systems – Lab Summary

## Overview

This project demonstrates **basic embedded control system design** using a Raspberry Pi and GPIO programming in Python.

The system explores how digital inputs (buttons) and outputs (LEDs) interact in real time, forming the foundation of embedded and robotics applications.

---

## Hardware Setup

* Raspberry Pi
* Push buttons (digital inputs)
* LEDs (digital outputs)
* Internal pull-up resistors

---

## Core Concepts

### GPIO Input Handling

Buttons are configured using internal pull-up resistors:

* Pressed → LOW (0)
* Released → HIGH (1)

This allows reliable detection of user input without external resistors.

---

### Output Control

LEDs are controlled using GPIO output signals:

* HIGH → LED ON
* LOW → LED OFF

This demonstrates direct control of hardware actuators.

---

### Control Logic

Different input-output relationships were implemented:

* Single input → output mapping
* Multi-input logic (AND condition)
* Time-based control using delays

---

### Real-Time Behavior

The system uses a **polling loop**:

* continuously reads input states
* processes control logic
* updates outputs accordingly

This simulates a simple real-time embedded control system.

---

## Implemented Experiments

### 1. Button-Controlled LED

* Pressing a button turns an LED ON
* Demonstrates basic input → output mapping

---

### 2. Dual Button Logic Control

* LED activates only when **both buttons are pressed**
* Demonstrates logical AND condition

---

### 3. Frequency-Based LED Control

* Button 1 → 1 Hz blinking
* Button 2 → 2 Hz blinking
* Demonstrates timing and frequency control

---

### 4. LED Sequence Control

* LEDs operate in a timed sequence
* Demonstrates state-based and sequential control logic

---

## Embedded Systems Concepts Demonstrated

* GPIO configuration (input/output modes)
* Internal pull-up resistor usage
* Polling-based real-time control
* Timing and delay handling
* State-based system behavior

---

## Conclusion

These experiments provide a foundation in embedded system design by demonstrating how software interacts with hardware in real time.

The system continuously:

* monitors inputs
* applies control logic
* updates outputs

This workflow is fundamental to more advanced embedded and robotics systems.
