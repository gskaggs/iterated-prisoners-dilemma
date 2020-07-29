from random import * 
CROSSOVER_RATE = 0.6

class GENETIC():
    @classmethod
    def from_parents(cls, parents):
        assert(len(parents) == 2)
        p0, p1 = parents[0], parents[1]
        assert(p0.history_len == p1.history_len)
        assert(p0.chromosome_len == p1.chromosome_len)

        history_len = p0.history_len
        chromosome_len = p0.chromosome_len
        chromosome0 = p0.chromosome.copy()
        chromosome1 = p1.chromosome.copy()

        if random.random() <= CROSSOVER_RATE:
            indices = (random.randrange(0, chromosome_len), random.randrange(0, chromosome_len))
            l, r = min(indices), max(indices)
            for i in range(l, r+1):
                chromosome0[i], chromosome1[i] = chromosome1[i], chromosome0[i]
        
        mutation_rate = 1 / chromosome_len if history_len <= 4 else 3 / chromosome_len
        for i in range(chromosome_len):
            if random.random() <= mutation_rate:
                chromosome0[i] = "C" if chromosome0[i] == "D" else "D"
            if random.random() <= mutation_rate:
                chromosome1[i] = "C" if chromosome1[i] == "D" else "D"

        return (cls(history_len, chromosome0), cls(history_len, chromosome1))
            
    def __init__(self, history_len, chromosome=None):
        self.history_len = history_len
        self.chromosome_len = 4 ** (history_len)
        if chromosome:
            self.chromosome = chromosome
        else:
            self.chromosome = [random.choice(["C", "D"]) for _ in range(self.chromosome_len)]
                