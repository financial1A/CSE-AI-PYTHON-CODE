import numpy as np
import matplotlib.pyplot as plt

def gambler_ruin_with_stop_loss(starting_amount, goal, stop_loss, win_probability, num_simulations):
    results = []

    for _ in range(num_simulations):
        money = starting_amount
        path = [money]
        
        while 0 < money < goal:
            if money <= stop_loss:  # Stop if hitting the stop-loss limit
                break
            if np.random.random() < win_probability:
                money += 1  # Win a dollar
            else:
                money -= 1  # Lose a dollar
            path.append(money)

        results.append(path)

    return results

# Parameters
starting_amount = 10
goal = 20
stop_loss = 5
win_probability = 0.51
num_simulations = 10

# Run simulations
paths = gambler_ruin_with_stop_loss(starting_amount, goal, stop_loss, win_probability, num_simulations)

# Plotting the results
plt.figure(figsize=(10, 6))
for path in paths:
    plt.plot(path)

plt.title("Gambler's Ruin Simulation with Stop-Loss")
plt.xlabel("Number of Bets")
plt.ylabel("Amount of Money")
plt.axhline(y=goal, color='green', linestyle='--', label='Goal')
plt.axhline(y=stop_loss, color='orange', linestyle='--', label='Stop-Loss')
plt.axhline(y=0, color='red', linestyle='--', label='Bankrupt')
plt.legend()
plt.show()
