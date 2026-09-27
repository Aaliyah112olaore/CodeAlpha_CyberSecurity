"""
Basic Network Sniffer
----------------------
Captures live network traffic and displays source/destination IPs,
the protocol used, and a preview of the payload for each packet.

Requirements:
    pip install scapy
    (Windows also needs Npcap installed: https://npcap.com)

Must be run with administrator/root privileges.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# How many packets to capture before stopping (set to 0 for unlimited)
PACKET_COUNT = 20


def get_protocol_name(packet):
    """Work out a human-readable protocol name from the packet layers."""
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def process_packet(packet):
    """Called automatically by sniff() for every captured packet."""
    # Only handle packets that have an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = get_protocol_name(packet)

        print(f"[+] {protocol}  {src_ip}  ->  {dst_ip}")

        # Show source/destination ports for TCP/UDP
        if packet.haslayer(TCP):
            print(f"    Port: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    Port: {packet[UDP].sport} -> {packet[UDP].dport}")

        # Show a short preview of the payload, if any
        if packet.haslayer(Raw):
             payload = packet[Raw].load
             preview = payload[:50]  # first 50 bytes only
            # Note: on port 443 (HTTPS) this will look like random bytes —
            # that's expected, since TLS encrypts the payload. Only
            # unencrypted traffic (e.g. plain HTTP on port 80) would
            # show readable text here.
             print(f"    Payload preview: {preview}")
        print("-" * 60)


if __name__ == "__main__":
    print(f"Starting capture of {PACKET_COUNT} packets... (Ctrl+C to stop early)\n")
    try:
        # sniff() calls process_packet() for every packet it captures
        # timeout=30 means it will stop after 30 seconds even if it
        # hasn't reached PACKET_COUNT yet, so you're not left guessing
        sniff(prn=process_packet, count=PACKET_COUNT, store=False, timeout=30)
    except PermissionError:
        print("Error: run this script as Administrator to capture packets.")
    print("\nCapture finished.")
