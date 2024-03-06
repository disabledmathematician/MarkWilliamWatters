import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
def randomroll(trials, samples):
	sum = []
	d1 = [x for x in range(1, 7)]
	d2 = [x for x in range(1, 7)]
	trial_total = []
	for x in range(samples):
		for x in range(trials):
			n1 = random.choice(d1)
			n2 = random.choice(d2)
			n3 = n1 + n2
			sum.append(n3)
		trial_total.append(sum)
	return trial_total

def plot(trial_total):
		plt.figure(0, dpi=150, figsize=[15, 7])
		all = []
		for L in trial_total:
			for e in L:
				all.append(e)
#		means = []
#		for x in trial_total:
#			means.append(np.mean(x))
#		print(means)
#		plt.hist(means)
		plt.hist(all)
		plt.show()

# Charles Truscott

L = randomroll(6, 6)
print(L)
plot(L)
			