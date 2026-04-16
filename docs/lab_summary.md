# GPIO Control Systems Summary

This project demonstrates basic embedded control systems using Raspberry Pi GPIO.

## Hardware Setup

- Raspberry Pi
- Push buttons (digital inputs)
- LEDs (digital outputs)
- Pull-up resistors (internal)

## Key Concepts

### GPIO Input Handling
Buttons are configured using internal pull-up resistors.  
A pressed button reads LOW (0), while an unpressed button reads HIGH (1).

### Output Control
LEDs are controlled by setting GPIO pins HIGH (ON) or LOW (OFF).

### Control Logic
- Single input → output mapping
- Multi-input (AND condition)
- Time-based control using delays

### Real-Time Behavior

The system uses a polling loop:
- continuously reads inputs
- updates outputs accordingly

This simulates simple real-time embedded system behavior.
