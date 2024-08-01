import numpy as np
import matplotlib.pyplot as plt

def gambler_scenario(initial_stake, bet_amount, target_amount, probability=0.5):
    win_loss = np.random.random()
    if(win_loss > 1-probability):
        win_loss = 1
    else:
        win_loss = 0
    if(win_loss):
        if (initial_stake + bet_amount < target_amount):
            return initial_stake + bet_amount
        else: 
            return target_amount
    else:
        if (initial_stake - bet_amount > 0):
            return initial_stake - bet_amount
        else:
            return 0
        


initial_stake = 500
target_amount = 1000
prob = 0.5
bet = 50
trials_size = 10000

income_array = []
rounds = []
count = 0

while(True):
    count += 1
    initial_stake = gambler_scenario(initial_stake, bet, target_amount, prob)
    if(initial_stake == 0 or initial_stake == target_amount):
        break
    else:
        income_array.append(initial_stake)
        rounds.append(count)


plt.plot(rounds, income_array)
plt.title('simulate the gambling scenaro')
plt.xlabel('number of rounds')
plt.ylabel('gambler stake')
plt.show()

initial_stake = 500
target_amount = 1000
prob = 0.5
bet = 50
trials_size = 10000
wins = 0
duration_of_wining = []
means = []

for j in range(trials_size):
    count = 0
    initial_stake = 500
    while(True):
        count += 1
        initial_stake = gambler_scenario(initial_stake, bet, target_amount, prob)
        if(initial_stake == target_amount):
            wins += 1
            duration_of_wining.append(count)
            break
        if(initial_stake == 0):
            break


win_probability = wins/trials_size
print(f'porbability of reaching target: {win_probability}')

mean = np.array(duration_of_wining).mean()
print(f'mean of rounds of success: {mean}')

for i in range(1, len(duration_of_wining)):
    means.append(np.array(duration_of_wining[:i]).mean())


plt.hist(means, bins=30, range=(0, max(means)))
plt.title(f'means for {trials_size}')
plt.show()

plt.plot([i for i in range(len(means))], means)
plt.title('line plot for iterate and means')
plt.show()

initial_stake_2 = 1000
target_amount_2 = 10000
prob_2 = 0.6
bet_2 = 50

income_array_2 = []
rounds_2 = []
count_2 = 0
while(True):
    count_2 += 1
    initial_stake_2 = gambler_scenario(initial_stake_2, bet_2, target_amount_2, prob_2)
    if(initial_stake_2 == 0 or initial_stake_2 == target_amount_2):
        break
    else:
        income_array_2.append(initial_stake_2)
        rounds_2.append(count_2)


plt.plot(rounds_2, income_array_2)
plt.title('simulate the gambling scenaro for 1000 times')
plt.xlabel('number of rounds')
plt.ylabel('gambler stake')
plt.show()

initial_stake_2 = 1000
target_amount_2 = 10000
prob_2 = 0.6
bet_2 = 50

wins_2 = 0
duration_of_wining_2 = []
means_2 = []

for j in range(trials_size):
    count_2 = 0
    initial_stake_2 = 1000
    while(True):
        count_2 += 1
        initial_stake_2 = gambler_scenario(initial_stake_2, bet_2, target_amount_2, prob_2)
        if(initial_stake_2 == target_amount_2):
            wins_2 += 1
            duration_of_wining_2.append(count_2)
            break
        if(initial_stake_2 == 0):
            break


win_probability_2 = wins_2/trials_size
print(f'porbability of reaching target: {win_probability_2}')

mean_2 = np.array(duration_of_wining_2).mean()
print(f'mean of durartion of success: {mean_2}')

for i in range(1, len(duration_of_wining_2)):
    means_2.append(np.array(duration_of_wining_2[:i]).mean())


plt.hist(means_2, bins=30, range=(0, max(means_2)))
plt.title(f'means for {trials_size}')
plt.show()

plt.plot([i for i in range(len(means_2))], means_2)
plt.title('line plot for iterate and means')
plt.show()

