import random
import time

THRESHOLD = 20  # suspicious number of outbound connections per interval

def get_outbound_connections():
    # Simulated outbound traffic volume
    return random.randint(0, 40)
# Monitor network traffic
while True:
    count = get_outbound_connections()
    print(f"Outbound connections: {count}")

    if count > THRESHOLD:
        print("⚠️ ALERT: Possible worm-like activity detected!")

    time.sleep(1)
