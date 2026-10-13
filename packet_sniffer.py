#!/usr/bin/env python3
"""
Prodigy Infotech Cybersecurity Internship
Packet Sniffer — Educational Lab Edition

Captures packets on an interface you are authorized to inspect.
Payload previews are disabled by default. If enabled, only a short prefix
is displayed; payloads may contain sensitive information.
"""

import os
import sys
from datetime import datetime

# 1. Automatic Python Virtual Environment & Scapy detection
try:
    from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw, get_if_list, conf
except ImportError:
    # If scapy isn't in current python, check for the local virtual environment
    venv_python = os.path.expanduser("~/myvenv/bin/python3")
    if os.path.exists(venv_python) and sys.executable != venv_python:
        os.execv(venv_python, [venv_python] + sys.argv)
    else:
        print("\n[!] Error: 'scapy' is required. Install it using:")
        print("    pip install scapy   OR   sudo pacman -S python-scapy\n")
        sys.exit(1)

import argparse


def get_ip_addresses(packet):
    if IP in packet:
        return packet[IP].src, packet[IP].dst
    if IPv6 in packet:
        return packet[IPv6].src, packet[IPv6].dst
    return "N/A", "N/A"


def get_protocol(packet):
    if TCP in packet:
        return "TCP"
    if UDP in packet:
        return "UDP"
    if ICMP in packet:
        return "ICMP"
    if IP in packet:
        return f"IP({packet[IP].proto})"
    if IPv6 in packet:
        return f"IPv6({packet[IPv6].nh})"
    return "OTHER"


def get_ports(packet):
    if TCP in packet:
        return f"{packet[TCP].sport} -> {packet[TCP].dport}"
    if UDP in packet:
        return f"{packet[UDP].sport} -> {packet[UDP].dport}"
    return "-"


def payload_preview(packet, enabled=False, limit=32):
    if not enabled or Raw not in packet:
        return "(disabled or no payload)"
    raw = bytes(packet[Raw].load[:limit])
    preview = raw.hex(" ")
    suffix = " ..." if len(packet[Raw].load) > limit else ""
    return preview + suffix


packet_counter = 0


def handle_packet(packet, show_payload=False):
    global packet_counter
    packet_counter += 1

    src, dst = get_ip_addresses(packet)
    protocol = get_protocol(packet)
    ports = get_ports(packet)
    timestamp = datetime.now().astimezone().strftime("%H:%M:%S")
    size = len(packet)

    print(
        f"{timestamp} | {protocol:<8} | {src:<39} | {dst:<39} "
        f"| {ports:<13} | {size:>5} bytes"
    )

    if show_payload:
        preview = payload_preview(packet, enabled=True)
        if preview != "(disabled or no payload)":
            print(f"    Payload prefix (hex, max 32 bytes): {preview}")


def main():
    parser = argparse.ArgumentParser(
        description="Educational packet sniffer for authorized lab traffic."
    )
    parser.add_argument(
        "-i", "--interface",
        help="Network interface to capture on (default: auto-detect active interface)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=0,
        help="Stop after this many packets (default: 0 = continuous until Ctrl+C)"
    )
    parser.add_argument(
        "--show-payload", action="store_true",
        help="Show first 32 payload bytes in hex"
    )
    parser.add_argument(
        "--list-interfaces", action="store_true",
        help="List available network interfaces and exit"
    )
    args = parser.parse_args()

    # Listing interfaces does not require root privileges
    if args.list_interfaces:
        print("\nAvailable network interfaces:")
        for iface in get_if_list():
            marker = " (active default)" if iface == str(conf.iface) else ""
            print(f"  - {iface}{marker}")
        print()
        return

    # 2. Automatic Root Privilege Elevation (sudo)
    # Raw packet sniffing requires root permissions on Linux
    if os.geteuid() != 0:
        print("[*] Packet sniffing requires root privileges. Elevating with sudo...")
        try:
            # Re-exec this script with sudo using the current python executable
            os.execvp("sudo", ["sudo", sys.executable, os.path.abspath(__file__)] + sys.argv[1:])
        except Exception as e:
            print(f"[!] Could not elevate with sudo: {e}")
            sys.exit(1)

    # 3. Automatic Interface Detection
    selected_iface = args.interface or str(conf.iface)

    print("=" * 145)
    print("                    EDUCATIONAL PACKET SNIFFER")
    print("=" * 145)
    print(f"[*] Target Interface : {selected_iface} (use -i <name> to change)")
    print(f"[*] Packet Limit     : {'Unlimited (Ctrl+C to stop)' if args.count == 0 else f'{args.count} packets'}")
    print(f"[*] Payload Previews : {'ON (32-byte hex)' if args.show_payload else 'OFF'}")
    print(f"[*] Press Ctrl+C at any time to finish.\n")

    print(
        f"{'TIME':<8} | {'PROTO':<8} | {'SOURCE IP':<39} | "
        f"{'DESTINATION IP':<39} | {'PORTS':<13} | {'LENGTH':>11}"
    )
    print("-" * 145)

    try:
        sniff(
            iface=selected_iface,
            prn=lambda pkt: handle_packet(pkt, args.show_payload),
            store=False,
            count=args.count
        )
    except OSError as exc:
        print(f"\n[!] Capture error on interface '{selected_iface}': {exc}")
    except KeyboardInterrupt:
        pass
    finally:
        print("-" * 145)
        print(f"[✓] Capture completed. Total packets analyzed: {packet_counter}\n")


if __name__ == "__main__":
    main()
