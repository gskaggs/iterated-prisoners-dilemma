from strategies.genetic import GENETIC

chromosome0 = ["C", "C", "C", "C"] 
chromosome1 = ["C", "C", "C", "C"]
parent0 = GENETIC(1,chromosome0)
parent1 = GENETIC(1,chromosome1)

child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome == ["C", "C", "C", "C"])
assert(child1.chromosome == ["C", "C", "C", "C"])

chromosome0 = ["C", "C", "C", "C"] 
chromosome1 = ["D", "D", "D", "D"]
parent0 = GENETIC(1,chromosome0)
parent1 = GENETIC(1,chromosome1)

child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome.count("C") + child1.chromosome.count("C") == 4)

parent0 = GENETIC(3)
parent1 = GENETIC(3)
child0, child1 = GENETIC.from_parents([parent0, parent1], debug=True)
assert(child0.chromosome_len == parent0.chromosome_len)
assert(child1.chromosome_len == parent0.chromosome_len)