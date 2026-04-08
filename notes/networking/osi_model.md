# OSI Model (Layers 1–4)

## Overview

The OSI model divides networking into layers, each with a specific role:

| Layer | Data Unit | Role |
|------|----------|------|
| Physical | Bits | Transmit raw signals |
| Data Link | Frames | Local communication |
| Network | Packets | Routing |
| Transport | Segments | Reliability |

---

## 1. Physical Layer

### Role
Sends raw bits (1s and 0s) across a medium.

### Defines
- Voltage levels
- Light signals (fiber)
- Radio waves (Wi-Fi)
- Bit rate
- Cables and connectors

### Limitations
- No understanding of frames, packets, or addresses

### Failures
- Cable unplugged
- Signal interference
- Broken connectors

---

## 2. Data Link Layer

### Role
Organises bits into frames and handles local delivery.

### Responsibilities

#### Framing
- Converts bit stream into frames

#### MAC Addressing
- Identifies devices on a local network

#### Error Detection
- Detects corrupted frames
- Drops invalid data

#### Switching
- Uses MAC address to forward frames

---

## Switch Behaviour

- Reads destination MAC
- Forwards frame to correct port

### MAC Table
- Stores MAC → Port mappings
- Learns dynamically

### Unknown MAC
- Floods frame to all ports

---

## Collisions

Occurs when two devices transmit at the same time.

### Recovery
- Stop transmission
- Send jam signal
- Wait random time
- Retransmit

---

## 3. Network Layer

### Role
Moves packets between networks using IP addresses.

### Responsibilities
- Logical addressing (IP)
- Routing
- Packet forwarding

---

## 4. Transport Layer

### Role
Ensures reliable, ordered delivery.

### Problems Solved
- Packet loss
- Out-of-order delivery
- Duplication

### Solutions
- Sequence numbers
- ACKs
- Retransmission
