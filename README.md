# Genetic Algorithms for Iterated Prisoner's Dilemma Strategies

My implementation and adaptation of the paper ["Evolution of iterated prisoner's dilemma strategies with different history lengths in static and cultural environments"](https://www.researchgate.net/publication/220999970_Evolution_of_iterated_prisoner's_dilemma_strategies_with_different_history_lengths_in_static_and_cultural_environments) by Brunauer and Mayer. 

### Execution

To most easily view output results, I recommend:

`python3 main.py > output.txt`

### Configuration

- *tourney_config.py* contains values pertinent to each game of iterated prisoner's dilemma.
- *strategies/genetic_config.py* contains values pertinent to the incorporated genetic algorithms.

### Output Archive

The results of my various experiments may be found in the *archive* directory. Files prefixed *round_robin* involve only classical strategies. Files prefixed *genetic_round_robin* and *cultural_evolution* involve genetic and cultural evolution, respectively.

### Related Resources 

- [The Stanford's Encyclapedia of Philosophy's entry on the Prisoner's Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/#PostAxel) thoroughly summarizes developments both before and after Axelrod's original tournament and contains a wealth of references for future enquiry.
- [The Selfish Gene by Richard Dawkins](https://www.amazon.com/Selfish-Gene-Anniversary-Landmark-Paperback/dp/B0722G5V92/ref=sr_1_2?dchild=1&keywords=The+Selfish+Gene&qid=1591506014&sr=8-2#customerReviews) original sparked my curiosity in evolutionary stable strategies and iterated prisoner's dilemma.