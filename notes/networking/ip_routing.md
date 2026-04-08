# IP Routing & Packet Forwarding

## Router Role
A router:
- Reads destination IP
- Decides next hop
- Forwards packet

---

## Packet Forwarding Process

1. Frame arrives
2. Router checks MAC address
3. Removes frame
4. Reads IP packet
5. Checks routing table
6. Selects next hop
7. Uses ARP to find MAC
8. Sends new frame

---

## Routing Table Contains
- Network prefix
- Next hop
- Interface

---

## Longest Prefix Match
- Most specific route is chosen

---

## Key Idea
- IP = destination
- MAC = next hop

---

## Packet Journey Summary

- IP addresses stay the same
- MAC addresses change at each hop
