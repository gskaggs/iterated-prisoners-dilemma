from strategies.genetic import GENETIC

# TEST: Recombination and construction
chromosome0 = ["C", "C", "C", "C"] 
chromosome1 = ["C", "C", "C", "C"]
parent0 = GENETIC(1, chromosome0)
parent1 = GENETIC(1, chromosome1)

child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome == ["C", "C", "C", "C"])
assert(child1.chromosome == ["C", "C", "C", "C"])

chromosome0 = ["C", "C", "C", "C"] 
chromosome1 = ["D", "D", "D", "D"]
parent0 = GENETIC(1, chromosome0)
parent1 = GENETIC(1, chromosome1)

child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome.count("C") + child1.chromosome.count("C") == 4)

parent0 = GENETIC(3)
parent1 = GENETIC(3)
child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome_len == parent0.chromosome_len)
assert(child1.chromosome_len == parent0.chromosome_len)

print("Passed: Recombination and construction")

# TEST: Observe and next action 
chromosome = ["C", "D", "C", "D"] 
agent = GENETIC(1, chromosome)

agent.observe_actions("C", "C")
assert(agent.next_action() == "C")

agent.observe_actions("C", "D")
assert(agent.next_action() == "D")

agent.observe_actions("D", "C")
assert(agent.next_action() == "C")

agent.observe_actions("D", "D")
assert(agent.next_action() == "D")

agent = GENETIC(2)
agent.chromosome[0] = "C"
agent.chromosome[3] = "D"
agent.chromosome[15] = "C"

assert(agent.next_action() == "C")

agent.observe_actions("D", "D")
assert(agent.next_action() == "D")

agent.observe_actions("D", "D")
assert(agent.next_action() == "C")

print("Passed: Observe and next action")

