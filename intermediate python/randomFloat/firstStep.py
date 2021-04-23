# Import numpy as np
import numpy  as np 

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
print(np.random.randint(1,7))


# Starting step
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
   step = max(0,step-1)
elif dice <=5 :
    step=step+1
else:
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# Initialize random_walk
random_walk=[0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step=random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)