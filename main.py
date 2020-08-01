from strategies.classics import *
from strategies.genetic import GENETIC
from config import LAMBDA, EPISODES, T, R, P, S

classics = [ALLC(), ALLD(), RAND(), GRIM(), TFT(), CTFT(), STFT(), TFTT(), PAVLOV(), NET_NICE()]

def reset(strategies):
    for strategy in strategies:
        strategy.reset()

# Returns the result of iterative prisoner's delima between two agents
def IPD(agent0, agent1, debug=False):
    # Action keys are (Opponent, Self)
    rewards = {("C", "D"): T, ("C", "C"): R, ("D", "D"): P, ("D", "C"): S}

    score = [0, 0]
    period_counts = []
    for _ in range(EPISODES):
        continue_prob = LAMBDA
        period_count = 0

        while random.random() <= continue_prob:
            continue_prob *= LAMBDA
            period_count += 1

            action0 = agent0.next_action()
            action1 = agent1.next_action()

            score[0] += rewards[(action1, action0)]
            score[1] += rewards[(action0, action1)]

            agent0.observe_actions(action1, action0)
            agent1.observe_actions(action0, action1)
        period_counts.append(period_count)

    if debug:
        print("Encounter between", agent0.name, "and", agent1.name)
        print("Number of episodes:", EPISODES)
        print("Average period count:", sum(period_counts) / len(period_counts))
        print("Score:", score[0], score[1])
        print()

    return tuple(score)

def round_robin(strategies, debug=False):
    for agent0 in strategies:
        for agent1 in strategies:
            agent0.reset(), agent1.reset()
            score = IPD(agent0, agent1, debug=debug) 
            agent0.score += score[0]
            agent1.score += score[1]
    
    # Sort reverse order of score
    strategies.sort(key=lambda agent: -1 * agent.score)

    if debug:
        print("*** End of round robin ***")
        for agent in strategies:
            print(agent.name, agent.score)

round_robin(classics, debug=True)