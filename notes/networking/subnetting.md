# Subnetting

## Overview
Subnetting splits a network into smaller networks.

---

## IP Structure
- Network ID
- Host ID

---

## CIDR Notation
- /24 = 255.255.255.0

---

## Key Formula
Hosts = 2^(host bits) - 2

---

## Example

192.168.1.10/24

- Network: 192.168.1.0
- Broadcast: 192.168.1.255
- Range: .1 – .254

---

## Splitting Networks

/24 → /25

- Subnet 1: 192.168.1.0 – 127
- Subnet 2: 192.168.1.128 – 255

---

## Shortcut

Block size = 256 - subnet mask

---

## Same Network Check
- AND IP with subnet mask
- If equal → same network
