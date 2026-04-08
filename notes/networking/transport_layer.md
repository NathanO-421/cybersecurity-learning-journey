# Transport Layer (TCP & UDP)

## TCP Goals
- Reliable delivery
- Ordered delivery
- Complete delivery

---

## Key Mechanisms

### Sequence Numbers
- Identify order of data

### ACKs
- Confirm received data

### Retransmission
- Resend missing data

---

## Packet Loss Example
- Missing packet → duplicate ACKs
- Sender retransmits

---

## Flow Control

- Uses receive window (rwnd)
- Prevents receiver overload

---

## Congestion Control

- Uses congestion window (cwnd)
- Adjusts based on network conditions

---

## TCP Characteristics
- Reliable
- Ordered
- Slower

---

## UDP

### Features
- No reliability
- No ordering
- Faster

### Use Cases
- Streaming
- Gaming
- DNS
