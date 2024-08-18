import math
import random
from collections import Counter

# Function to simulate sending data packets
def send_packets(num_packets, num_ips, attack=False):
    ip_addresses = [f"192.168.0.{i}" for i in range(1, num_ips + 1)]
    
    if attack:
        # During an attack, most traffic comes from a few IPs
        attack_ips = random.sample(ip_addresses, k=max(1, num_ips // 10))
        traffic = random.choices(attack_ips, k=num_packets)
    else:
        # Normal traffic has a more even distribution
        traffic = random.choices(ip_addresses, k=num_packets)
    
    return traffic

# Function to compute entropy
def compute_entropy(traffic):
    total_packets = len(traffic)
    ip_count = Counter(traffic)
    
    entropy = -sum((count / total_packets) * math.log2(count / total_packets) for count in ip_count.values())
    
    return entropy

# Function to classify traffic based on entropy
def detect_ddos(traffic, threshold_entropy):
    entropy = compute_entropy(traffic)
    return "DDoS Attack Detected" if entropy < threshold_entropy else "Normal Traffic"

# Function to find detection accuracy
def find_accuracy(num_tests, num_packets, num_ips, threshold_entropy):
    correct_detections = sum(
        detect_ddos(send_packets(num_packets, num_ips, attack), threshold_entropy) == ("DDoS Attack Detected" if attack else "Normal Traffic")
        for attack in [False, True] for _ in range(num_tests)
    )
    
    return correct_detections / (2 * num_tests)

# Parameters
num_packets = 10000  # Number of packets sent
num_ips = 100        # Number of different IP addresses
num_tests = 100      # Number of tests to calculate accuracy

# Simulate normal and attack traffic
normal_traffic = send_packets(num_packets, num_ips, attack=False)
attack_traffic = send_packets(num_packets, num_ips, attack=True)

# Compute entropy for normal and attack scenarios
normal_entropy = compute_entropy(normal_traffic)
attack_entropy = compute_entropy(attack_traffic)

# Set a threshold for detecting attacks
threshold_entropy = (normal_entropy + attack_entropy) / 2

# Display results
print(f"Normal Entropy: {normal_entropy:.4f}")
print(f"Attack Entropy: {attack_entropy:.4f}")
print(f"Threshold Entropy: {threshold_entropy:.4f}")
print(f"Detection Accuracy: {find_accuracy(num_tests, num_packets, num_ips, threshold_entropy) * 100:.2f}%")
