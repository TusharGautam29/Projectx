import math
import random
from collections import Counter

# Function to simulate sending data packets
def send_packets(num_packets, num_ips, attack=False):
    ip_addresses = [f"192.168.0.{i}" for i in range(1, num_ips + 1)]
    
    if attack:
        # During an attack, most traffic comes from a few IPs
        attack_ips = random.sample(ip_addresses, k=max(1, num_ips // 10))
        traffic = [random.choice(attack_ips) for _ in range(num_packets)]
    else:
        # Normal traffic has a more even distribution
        traffic = [random.choice(ip_addresses) for _ in range(num_packets)]
    
    return traffic

# Function to compute entropy
def compute_entropy(traffic):
    total_packets = len(traffic)
    ip_count = Counter(traffic)
    
    entropy = 0
    for count in ip_count.values():
        probability = count / total_packets
        entropy -= probability * math.log2(probability)
    
    return entropy

# Simulate traffic
num_packets = 10000  # Number of packets sent
num_ips = 100  # Number of different IP addresses

# Normal traffic
normal_traffic = send_packets(num_packets, num_ips, attack=False)
normal_entropy = compute_entropy(normal_traffic)

# Attack traffic
attack_traffic = send_packets(num_packets, num_ips, attack=True)
attack_entropy = compute_entropy(attack_traffic)

# Setting a threshold for detecting attack
threshold_entropy = (normal_entropy + attack_entropy) / 2

# Function to classify traffic
def detect_ddos(traffic):
    entropy = compute_entropy(traffic)
    if entropy < threshold_entropy:
        return "DDoS Attack Detected"
    else:
        return "Normal Traffic"

# Find accuracy
def find_accuracy(num_tests=100):
    correct_detections = 0

    for _ in range(num_tests):
        traffic = send_packets(num_packets, num_ips, attack=False)
        if detect_ddos(traffic) == "Normal Traffic":
            correct_detections += 1
        
        traffic = send_packets(num_packets, num_ips, attack=True)
        if detect_ddos(traffic) == "DDoS Attack Detected":
            correct_detections += 1

    accuracy = correct_detections / (2 * num_tests)
    return accuracy

# Display results
print(f"Normal Entropy: {normal_entropy}")
print(f"Attack Entropy: {attack_entropy}")
print(f"Threshold Entropy: {threshold_entropy}")
print(f"Detection Accuracy: {find_accuracy() * 100:.2f}%")
