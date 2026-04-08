# ARP and DHCP

## ARP (Address Resolution Protocol)

### Purpose
Maps IP address → MAC address

---

## ARP Process

1. Check ARP cache
2. Broadcast request
3. Receive reply
4. Store mapping
5. Send frame

---

## Key Cases

### Same Network
- ARP for destination

### Different Network
- ARP for router (default gateway)

---

## DHCP (Dynamic Host Configuration Protocol)

### Purpose
Automatically assigns network configuration

---

## DORA Process

1. Discover
2. Offer
3. Request
4. ACK

---

## DHCP Provides
- IP address
- Subnet mask
- Default gateway
- DNS server

---

## Key Notes
- Uses MAC address initially
- IP is leased (temporary)
