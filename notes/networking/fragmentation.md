# IP Fragmentation

## Overview
Packets larger than MTU must be split.

---

## Key Terms

- MTU: Maximum packet size
- MSS: TCP data size

---

## Fragmentation

- Packet split into smaller pieces
- Each fragment has its own header

---

## Important Fields
- Identification
- MF (More Fragments)
- Offset

---

## Reassembly
- Done at destination

---

## Downsides
- Overhead
- Slower
- Loss of one fragment = loss of entire packet
