import random
from genetic_config import CROSSOVER_RATE

class GENETIC():
    name = "GENETIC"
    observationToEncoding = {("C", "C"): 0, ("C", "D"): 1, ("D", "C"): 2, ("D", "D"): 3}

    @classmethod
    def from_parents(cls, parents, debug=False):
        assert(len(parents) == 2)
        p0, p1 = parents[0], parents[1]
        assert(p0.history_len == p1.history_len)
        assert(p0.chromosome_len == p1.chromosome_len)

        history_len = p0.history_len
        chromosome_len = p0.chromosome_len
        chromosome0 = p0.chromosome.copy()
        chromosome1 = p1.chromosome.copy()

        shouldRecombinate = random.random()
        assert(0 <= shouldRecombinate and shouldRecombinate <= 1)

        if shouldRecombinate<= CROSSOVER_RATE:
            indices = (random.randrange(0, chromosome_len), random.randrange(0, chromosome_len))
            l, r = min(indices), max(indices)
            for i in range(l, r+1):
                chromosome0[i], chromosome1[i] = chromosome1[i], chromosome0[i]
        
        if not debug:
            mutation_rate = 1 / chromosome_len if history_len <= 4 else 3 / chromosome_len
            for i in range(chromosome_len):
                if random.random() <= mutation_rate:
                    chromosome0[i] = "C" if chromosome0[i] == "D" else "D"
                if random.random() <= mutation_rate:
                    chromosome1[i] = "C" if chromosome1[i] == "D" else "D"

        else: 
            print("Creating new chromosomes with")
            print("Parents: ", p0.chromosome, p1.chromosome, sep="\n")
            print("And resultant children: ", chromosome0, chromosome1, sep="\n")
            print()

        return (cls(history_len, chromosome0), cls(history_len, chromosome1))
            
    def __init__(self, history_len, chromosome=None):
        self.history_len = history_len
        self.chromosome_len = 4 ** (history_len)
        self.history = 0
        if chromosome:
            assert(self.chromosome_len == len(chromosome))
            self.chromosome = chromosome
        else:
            self.chromosome = [random.choice(["C", "D"]) for _ in range(self.chromosome_len)]

    def next_action(self):
        return self.chromosome[self.history]

    def observe_actions(self, opponent, own):
        self.history <<= 2
        self.history |= GENETIC.observationToEncoding[(opponent, own)]
        self.history &= (1 << (2 * self.history_len)) - 1
        assert(self.history < self.chromosome_len)

    def reset(self):
        self.history = 0
                