# Maze QL

A small Python maze simulation and starting point for experimenting with Q-learning. An agent takes random actions in a fixed maze, receives rewards, and tries to reach the goal.

The current implementation uses random movement only. It initializes a `q_table` with visited states but does not yet calculate Q-values or learn a policy.

## Requirements

- Python 3
- No third-party dependencies; only the standard-library `random` module is used.

## Run

From the project directory:

```sh
python3 main.py
```

The script prints the maze, followed by each move's starting position, chosen action, and resulting position. It reports wall collisions and successful goal arrivals, then prints the move count, total reward, and completion status for each episode. Results vary between runs because actions are chosen randomly.

## The maze

```text
#####
#S#G#
# # #
#   #
#####
```

| Symbol | Meaning |
| --- | --- |
| `#` | Wall |
| `S` | Starting position |
| `G` | Goal |
| Space | Walkable cell |

Positions are represented as zero-based `(row, column)` tuples. The agent starts at `(1, 1)` and the goal is at `(1, 3)`.

## Simulation rules

- Each run contains two episodes, each starting at `S`.
- Each episode allows up to ten actions: `up`, `right`, `down`, or `left`.
- A wall collision leaves the agent in its current position.
- Reaching the goal ends the episode immediately.

| Outcome | Reward |
| --- | ---: |
| Ordinary move | -1 |
| Wall collision | -5 |
| Reaching the goal | +10 |

## Customize

All code lives in `main.py`. Edit `maze` to change the layout, `start_row` and `start_col` to change the starting position, `range(2)` to change the episode count, or `counter < 10` to change the action limit. Rewards are assigned inside the movement loop.

Keep the maze rectangular with a solid wall border, and keep the starting coordinates aligned with `S`; the movement code relies on those conditions when checking neighboring cells.
