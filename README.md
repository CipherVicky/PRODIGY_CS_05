# Prodigy Infotech CS Internship — Task 05
# 📡 Educational Packet Sniffer

A lightweight, Python-based network packet sniffer built with **Scapy**. It captures and analyzes network traffic in real time, displaying source & destination IP addresses, transport protocols, port numbers, packet lengths, and optional payload previews.

Designed for network analysis, cybersecurity students, and educational lab environments.

---

## ✨ Features

- **Automatic Interface Detection**: Automatically binds to your active default network interface without requiring manual configuration.
- **Auto-Elevation (`sudo`)**: Prompts for root permissions on Linux if not already elevated.
- **Protocol Analysis**: Detects and parses IPv4, IPv6, TCP, UDP, ICMP, and other protocols.
- **Clean Tabular Output**: Displays packet metadata in an easy-to-read, structured table.
- **Payload Inspection**: Optional hex preview (first 32 bytes) for inspecting application-layer payloads.
- **Interface Explorer**: Easily list all available local network interfaces with `--list-interfaces`.

---

## 📋 Prerequisites

- **Operating System**: Linux (Arch, Ubuntu, Debian, Fedora, etc.) or macOS
- **Python**: Python 3.8 or higher
- **Root / Sudo Privileges**: Required on Linux to access raw network sockets (`CAP_NET_RAW`)

---

## 🚀 Installation

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com/your-username/packet-sniffer.git
   cd packet-sniffer
   ```

2. **Install dependencies**:
   ```bash
   pip install scapy
   ```
   *On Arch Linux, you can also install via pacman:*
   ```bash
   sudo pacman -S python-scapy
   ```
   *On Debian/Ubuntu:*
   ```bash
   sudo apt install python3-scapy
   ```

3. **Make the script executable**:
   ```bash
   chmod +x packet_sniffer.py
   ```

---

## 💻 How to Run

### 1. Quick Start (Default Interface)
Run the script directly. It will automatically detect your active network connection and start capturing:

```bash
./packet_sniffer.py
```
*(or `python3 packet_sniffer.py`)*

> **Note**: Packet capturing requires root privileges. The script will automatically prompt for your `sudo` password if needed.

---

### 2. Common Usage Examples

- **Capture on a specific interface** (e.g., Wi-Fi `wlo1` or Ethernet `eth0`):
  ```bash
  ./packet_sniffer.py -i wlo1
  ```

- **Capture on Localhost / Loopback** (`lo`):
  ```bash
  ./packet_sniffer.py -i lo
  ```

- **Stop automatically after $N$ packets** (e.g., 20 packets):
  ```bash
  ./packet_sniffer.py -c 20
  ```

- **Show hex payload preview**:
  ```bash
  ./packet_sniffer.py --show-payload
  ```

- **List all network interfaces**:
  ```bash
  ./packet_sniffer.py --list-interfaces
  ```

- **Stop capture**: Press <kbd>Ctrl</kbd> + <kbd>C</kbd> at any time.

---

## 📊 Command-Line Options

| Option | Description |
| :--- | :--- |
| `-i`, `--interface` | Specify network interface (e.g., `eth0`, `wlan0`, `lo`). Defaults to active interface. |
| `-c`, `--count` | Number of packets to capture before stopping (default: `0` = continuous). |
| `--show-payload` | Display first 32 bytes of packet payload in hex format. |
| `--list-interfaces` | List all detected local network interfaces and exit. |
| `-h`, `--help` | Show help and usage instructions. |

---

## 🖥️ Example Output

```text
=================================================================================================================================================
                                                    EDUCATIONAL PACKET SNIFFER
=================================================================================================================================================
[*] Target Interface : wlo1 (use -i <name> to change)
[*] Packet Limit     : Unlimited (Ctrl+C to stop)
[*] Payload Previews : OFF
[*] Press Ctrl+C at any time to finish.

TIME     | PROTO    | SOURCE IP                               | DESTINATION IP                          | PORTS         |      LENGTH
-------------------------------------------------------------------------------------------------------------------------------------------------
21:40:02 | TCP      | 192.168.1.15                            | 142.250.190.46                          | 44320 -> 443  |    74 bytes
21:40:02 | TCP      | 142.250.190.46                          | 192.168.1.15                            | 443 -> 44320  |    66 bytes
21:40:03 | UDP      | 192.168.1.15                            | 192.168.1.1                             | 5353 -> 5353  |   128 bytes
-------------------------------------------------------------------------------------------------------------------------------------------------
[✓] Capture completed. Total packets analyzed: 3
```

---

## ⚖️ Ethical Disclaimer

This software is provided for educational and authorized network diagnostics purposes only.
- Sniffing network packets without explicit authorization on networks you do not own or administer is illegal and violates privacy laws.
- Only run this tool on localhost, lab environments, or networks where you have written permission.

---

## 📜 License

This project is licensed under the MIT License.
