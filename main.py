import random

maze = [
        ['#', '#', '#', '#', '#'], 
        ['#', 'S', '#', 'G', '#'],
        ['#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#']
        ]



for row in maze:
    print(' '.join(row))

print('---------')

start_row = 1
start_col = 1

actions = ['up', 'right', 'down', 'left']

q_table = {}

for episode in range(2):

    agent_row = start_row
    agent_col = start_col

    counter = 0

    total_reward = 0

    done = False

    while counter < 10:
        state = (agent_row, agent_col)
        print(state)

        if state not in q_table:
            q_table[state] = {}

        action = random.choice(actions)
        print(action)
        counter += 1
        reward = -1

        if action == 'right':
            if maze[agent_row][agent_col + 1] == '#':
                print('Wall')
                reward = -5
            else:
                agent_col += 1
        elif action == 'down':
            if maze[agent_row + 1][agent_col] == '#':
                print('Wall')
                reward = -5
            else:
                agent_row += 1
        elif action == 'left':
            if maze[agent_row][agent_col - 1] == '#':
                print('Wall')
                reward = -5
            else:
                agent_col -= 1
        elif action == 'up':
            if maze[agent_row - 1][agent_col] == '#':
                print('Wall')
                reward = -5
            else:
                agent_row -= 1
        else:
            print('Unknown Action')

        next_state = (agent_row, agent_col)
        print(next_state)


        if maze[agent_row][agent_col] == 'G':
            print('Goal reached!')
            reward = 10
            total_reward += reward
            done = True
            break

        total_reward += reward


    print(f'Counter: {counter}')

    print(f'Total reward: {total_reward}')

    print(f'Done: {done}')