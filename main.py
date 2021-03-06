from strategies.classics import *
from strategies.genetic import GENETIC
from strategies.genetic_config import  NUM_GENERATIONS, GENERATION_SIZE, HISTORY_LEN, CROSSOVER_RATE, MIN_HISTORY_LEN, MAX_HISTORY_LEN
from tourney import print_rankings, IPD, round_robin, print_tourney_config

print("Genetic Config:")
print("Number of generations:", NUM_GENERATIONS, "| Generation size:", GENERATION_SIZE, "| Crossover rate:", CROSSOVER_RATE, "| History length", HISTORY_LEN)
print("\nTournanment Config:")
print_tourney_config()
print()

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

def genetic_evolution(competitors, genetics, debug=False):
    if debug:
        print("Beginning genetic evolution\n")

    for generation_count in range(NUM_GENERATIONS):
        for agent in genetics:
            assert(agent.name == "GENETIC")
            test_fitness(competitors, agent)
        
        if debug:
            print("Generation", generation_count + 1)
            print("Raw:")
            for count in range(GENERATION_SIZE):
                print(count + 1, genetics[count].score)
            print()
            print("Sorted:")
            print_rankings(genetics)
        
        if generation_count < NUM_GENERATIONS - 1:
            genetics = new_generation(genetics)
    
    if debug:
        # Print results
        strategies = competitors
        count = 1
        for agent in genetics:
            print("*** GENETIC", count, "***\n")
            print("Chromosome:", agent.chromosome, "\n")
            strategies.append(agent)
            round_robin(strategies)
            strategies.pop()
            count += 1

    return sorted(genetics, key=lambda agent: -1 * agent.score)

def cultural_evolution(classics, debug=False):
    if debug:
        print("Beginning cultural evolution\n")

    established_strategies = classics.copy()

    for history_len in range(MIN_HISTORY_LEN, MAX_HISTORY_LEN + 1):
        genetics = [GENETIC(history_len) for _ in range(GENERATION_SIZE)]
        genetics = genetic_evolution(established_strategies, genetics)

        assert(len(genetics) == GENERATION_SIZE)
        assert(genetics[0].score >= genetics[-1].score)

        best_genetic_strategy = genetics[0]
        best_genetic_strategy.name = "GENETIC " + str(history_len)
        print("Best chromosome for history length", history_len, best_genetic_strategy.chromosome)
        established_strategies.append(best_genetic_strategy)
    
    if debug:
        print("\nEnd of cultural evolution\n")
        round_robin(established_strategies, debug=True)

# Used for both genetic and cultural evolution
classics = [ALLC(), ALLD(), RAND(), GRIM(), TFT(), CTFT(), STFT(), TFTT(), PAVLOV(), NET_NICE()]

# Uncomment the following lines to do genetic evolution with a fixed history length:
# genetics = [GENETIC(HISTORY_LEN) for _ in range(GENERATION_SIZE)]
# genetic_evolution(classics, genetics, debug=True)

# Otherwise run cultural evolution in which members of several history lengths  
# compete and learn from each other:
cultural_evolution(classics, debug=True)