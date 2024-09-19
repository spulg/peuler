import numpy as np

# Grid size
n = 30
circus = np.ones((n, n), dtype=int)  # Initially, 1 flea per square

# Directions dictionary
directions = ["left", "right", "up", "down"]


# Movement functions for each flea
def left(i, j):
    circus[i][j] -= 1
    circus[i - 1][j] += 1


def right(i, j):
    circus[i][j] -= 1
    circus[i + 1][j] += 1


def up(i, j):
    circus[i][j] -= 1
    circus[i][j - 1] += 1


def down(i, j):
    circus[i][j] -= 1
    circus[i][j + 1] += 1


def move_flea(i, j):
    # Boundary conditions: fleas on the edges have fewer options
    options = []
    if i > 0: options.append("left")
    if i < n - 1: options.append("right")
    if j > 0: options.append("up")
    if j < n - 1: options.append("down")

    if options:
        direction = np.random.choice(options)
        if direction == "left":
            left(i, j)
        elif direction == "right":
            right(i, j)
        elif direction == "up":
            up(i, j)
        elif direction == "down":
            down(i, j)


def step():
    # We need to record fleas that are to be moved, because we can't modify the grid while iterating over it.
    flea_moves = []
    for i in range(n):
        for j in range(n):
            # Move each flea in (i, j) to a new location
            for _ in range(int(circus[i][j])):  # For each flea in this square
                flea_moves.append((i, j))

    # Move the fleas in their new directions
    for i, j in flea_moves:
        move_flea(i, j)


def simulate():
    for _ in range(50):  # 50 rings of the bell
        step()

    # Count number of unoccupied squares
    unoccupied = np.sum(circus == 0)
    print(f"Number of unoccupied squares: {unoccupied}")
    return unoccupied


average = 0
for _ in range(1000):
    average += simulate()

print(f"{average / 100:.6f}")

# np.set_printoptions(linewidth=2 ** 10)
# print(circus)

# Grid size
n = 30
num_states = n * n

# Initialize the transition matrix
T = np.zeros((num_states, num_states))


def index(i, j):
    return i * n + j


# Fill the transition matrix
for i in range(n):
    for j in range(n):
        idx = index(i, j)
        neighbors = []
        if i > 0: neighbors.append(index(i - 1, j))  # left
        if i < n - 1: neighbors.append(index(i + 1, j))  # right
        if j > 0: neighbors.append(index(i, j - 1))  # up
        if j < n - 1: neighbors.append(index(i, j + 1))  # down

        prob = 1 / len(neighbors)
        for neighbor in neighbors:
            T[idx, neighbor] = prob

# Initial probability vector (all fleas equally distributed)
p0 = np.ones(num_states) / num_states

# Evolve the system for 50 steps
p = p0
for _ in range(50):
    p = T @ p

# Calculate the expected number of unoccupied squares
# Each entry in p represents the probability of that square being occupied
expected_unoccupied = np.sum(1 - p)
print(f"Expected number of unoccupied squares: {expected_unoccupied:.6f}")
