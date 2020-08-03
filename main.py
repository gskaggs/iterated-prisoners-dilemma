from strategies.classics import *
from strategies.genetic import GENETIC
from strategies.genetic_config import  NUM_GENERATIONS, GENERATION_SIZE, HISTORY_LEN, CROSSOVER_RATE
from tourney_config import LAMBDA, EPISODES, T, R, P, S

print("Genetic Config:")
print("Number of generations:", NUM_GENERATIONS, "| Generation size:", GENERATION_SIZE, "| Crossover rate:", CROSSOVER_RATE, "| History length", HISTORY_LEN)
print("\nTournanment Config:")
print("LAMBDA:", LAMBDA, "| Episodes:", EPISODES, "| T R P S:", T, R, P, S)
print()

classics = [ALLC(), ALLD(), RAND(), GRIM(), TFT(), CTFT(), STFT(), TFTT(), PAVLOV(), NET_NICE()]
genetics = [GENETIC(HISTORY_LEN) for _ in range(GENERATION_SIZE)]

def reset_scores(strategies):
    for agent in strategies:
        agent.score = 0

def print_rankings(strategies):
    # Sort reverse order of score
    sorted_strategies = sorted(strategies, key=lambda agent: -1 * agent.score)

    count = 1
    for agent in sorted_strategies:
        print(count, agent.name, agent.score)
        count += 1
    print()

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
    reset_scores(strategies)
    for agent0 in strategies:
        for agent1 in strategies:
            agent0.reset(), agent1.reset()
            score = IPD(agent0, agent1, debug=debug) 
            agent0.score += score[0]
            agent1.score += score[1]

    print("*** End of round robin ***")
    print_rankings(strategies)

def test_fitness(strategies, genetic, debug=False):
    strategies.append(genetic)
    genetic.score = 0
    for agent in strategies:
        agent.reset(), genetic.reset()
        score = IPD(agent, genetic, debug=debug) 
        genetic.score += score[1]

    strategies.pop()
    if debug:
        print("*** End of fitness test ***")

def new_generation(strategies):
    assert(len(strategies) == GENERATION_SIZE)
    cumulative_points = []
    count = 0
    for agent in strategies:
        assert(agent.name == "GENETIC")
        count += agent.score
        cumulative_points.append(count)

    result = []
    for _ in range(GENERATION_SIZE // 2):
        parents = random.choices(strategies, cum_weights=cumulative_points, k=2)
        children = GENETIC.from_parents(parents)
        result.extend(children)
    
    # In case GENERATION_SIZE is odd
    if len(result) < GENERATION_SIZE:
        parents = random.choices(strategies, cum_weights=cumulative_points, k=2)
        children = GENETIC.from_parents(parents)
        result.append(children[0])

    assert(len(result) == GENERATION_SIZE)

    return result

def genetic_evolution(classics, genetics, debug=False):
    if debug:
        print("Beginning genetic evolution\n")
    for generation_count in range(NUM_GENERATIONS):
        for agent in genetics:
            assert(agent.name == "GENETIC")
            test_fitness(classics, agent)
        
        if debug:
            print("Generation", generation_count + 1)
            print("Raw:")
            for count in range(GENERATION_SIZE):
                print(count + 1, genetics[count].score)
            print()
            print("Sorted:")
            print_rankings(genetics)

        genetics = new_generation(genetics)
    
    # Print results
    strategies = classics
    count = 1
    for agent in genetics:
        print("*** GENETIC", count, "***\n")
        print("Chromosome:", agent.chromosome, "\n")
        strategies.append(agent)
        round_robin(strategies)
        strategies.pop()
        count += 1

#round_robin(classics, debug=True)
genetic_evolution(classics, genetics, debug=True)