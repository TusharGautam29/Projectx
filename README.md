Report: DDoS Attack Detection Using Entropy-Based Analysis
1. Introduction
Distributed Denial of Service (DDoS) attacks represent a significant security threat to online services. These attacks aim to disrupt normal operations by overwhelming a server with a flood of traffic, often making it difficult for legitimate users to access the service. Detecting such attacks in a timely manner is critical for mitigating their impact. This report details a method for detecting DDoS attacks using entropy-based analysis of network traffic, implemented in Python.

2. Methodology
The proposed detection method leverages entropy, a concept from information theory that quantifies the randomness or unpredictability in a dataset. In the context of network traffic, entropy is used to measure the distribution of IP addresses from which data packets originate. Normal network traffic typically has a more uniform distribution of IP addresses, leading to higher entropy, whereas DDoS attack traffic often shows a lower entropy due to the concentration of traffic from a few IP sources.

Steps of the Approach:
Simulating Network Traffic:

Normal Traffic: This is simulated by generating data packets from a wide range of IP addresses, resulting in a more even distribution and higher entropy.
Attack Traffic: Simulated by concentrating the data packets from a small subset of IP addresses, which reduces the entropy.
Entropy Calculation:

The entropy of the traffic is calculated using the Shannon entropy formula:
𝐻
=
−
∑
𝑖
=
1
𝑛
𝑝
(
𝑖
)
log
⁡
2
𝑝
(
𝑖
)
H=− 
i=1
∑
n
​
 p(i)log 
2
​
 p(i)

where 
𝑝
(
𝑖
)
p(i) is the probability of packets originating from IP address 
𝑖
i. This calculation provides a single entropy value that reflects the diversity of the IP address distribution in the traffic.
Threshold Setting:

A threshold entropy value is determined by averaging the entropy values calculated from both normal and attack traffic simulations. This threshold is used to classify new traffic as either normal or indicative of a DDoS attack.
Detection and Accuracy Measurement:

The system classifies incoming traffic by comparing its entropy to the threshold. If the entropy is below the threshold, the traffic is flagged as a potential DDoS attack. The accuracy of this detection method is evaluated by simulating multiple instances of normal and attack traffic and measuring the proportion of correct classifications.
3. Implementation
The program was implemented in Python, using a combination of standard libraries such as math for entropy calculation and random for traffic simulation. Key functions include:

send_packets(): Generates traffic by creating a list of IP addresses, either distributed uniformly (for normal traffic) or concentrated (for attack traffic).
compute_entropy(): Calculates the entropy of the given traffic data based on the distribution of IP addresses.
detect_ddos(): Classifies traffic as normal or a potential DDoS attack by comparing the computed entropy to a predetermined threshold.
find_accuracy(): Evaluates the accuracy of the detection method by simulating multiple test cases and calculating the proportion of correct detections.
4. Results
The simulation results demonstrated the effectiveness of entropy-based analysis for detecting DDoS attacks. The entropy of normal traffic was significantly higher than that of attack traffic, allowing for a clear distinction between the two. The threshold entropy, set as the midpoint between normal and attack entropy values, effectively identified attack scenarios with high accuracy.

5. Conclusion
The entropy-based method for DDoS attack detection provides a robust approach to identifying abnormal traffic patterns indicative of an attack. By measuring the diversity of IP addresses in network traffic, this method can effectively distinguish between normal operations and potential threats. Future work could explore the integration of this technique with real-time network monitoring systems, as well as the application of more sophisticated machine learning algorithms to enhance detection accuracy.
