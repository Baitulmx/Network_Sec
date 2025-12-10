import random
import time

NUM_HOSTS = 50
infection_chance = 0.30 # chance of successful infection per attempt
attempts_per_step = 2

hosts = ["healthy"] * NUM_HOSTS
hosts[0] = "infected" # start point
# Simulate one step of infection spread
def simulate_step():
    new_infections = 0
    # For each infected host, attempt to infect others
    for i, h in enumerate(hosts):
        if h == "infected":
            for _ in range(attempts_per_step):
                target = random.randint(0, NUM_HOSTS - 1)
                if hosts[target] == "healthy" and random.random() < infection_chance:
                    hosts[target] = "infected"
                    new_infections += 1
    return new_infections
# Run simulation until all hosts are infected
step = 0
while "healthy" in hosts:
    infected_now = simulate_step()
    step += 1
    print(f"Step {step}: {hosts.count('infected')} infected")

    time.sleep(0.2)

print("All hosts infected!")
