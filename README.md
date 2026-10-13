# Prodigy Infotech Cybersecurity Internship — Packet Sniffer

## Objective
Build a Python tool that captures and analyzes packets on an authorized network interface and displays source/destination IP addresses, protocol, ports, packet length, and optionally a short payload prefix.

## Requirements
- Python 3
- Scapy
- Linux (recommended for this lab)

## Install on Arch Linux
```bash
sudo pacman -S python python-pip
python -m venv .venv
source .venv/bin/activate
pip install scapy
```

If your environment blocks system package installation, use a virtual environment as shown above.

## Run
List interfaces:
```bash
sudo .venv/bin/python packet_sniffer.py --list-interfaces
```

Capture 25 packets on a selected interface:
```bash
sudo .venv/bin/python packet_sniffer.py --interface wlan0 --count 25
```

Replace `wlan0` with an interface listed on your own machine. To stop an unlimited capture, press `Ctrl+C`.

Show a short payload prefix in hexadecimal (may contain sensitive data):
```bash
sudo .venv/bin/python packet_sniffer.py --interface wlan0 --count 10 --show-payload
```

Payload display is off by default. The program shows only up to 32 bytes of a payload and does not save captured packets to disk.

## Fields displayed
- Time: local time when the packet is processed
- Protocol: TCP, UDP, ICMP, or an IP protocol identifier
- Source IP and destination IP
- Source and destination ports for TCP/UDP
- Packet length in bytes
- Optional short payload prefix, in hexadecimal

## Ethical and safety notes
- Capture only traffic on systems/networks you own or have explicit permission to test.
- Do not use this tool to intercept other people's traffic or collect credentials.
- Payloads can contain private information. Keep payload previews disabled unless necessary for a controlled lab.
- Use a packet count limit during demonstrations and stop the capture when finished.
- HTTPS/TLS application data is generally encrypted; this tool does not decrypt it.
- Some interfaces or networks expose only traffic visible to the host. Promiscuous-mode behavior depends on the interface and network.

## Troubleshooting
- `No module named scapy`: activate the virtual environment and install Scapy.
- Permission errors: packet capture generally requires elevated privileges or suitable capture capabilities.
- No packets appear: choose the correct interface and generate ordinary traffic on your own device.
- Interface names vary. Use `--list-interfaces`.

## Suggested demonstration
1. List interfaces.
2. Capture a small number of packets on your own active interface.
3. Visit a benign website or run a simple network command during capture.
4. Screenshot the terminal output.
5. Keep payload preview disabled for the standard demonstration.
