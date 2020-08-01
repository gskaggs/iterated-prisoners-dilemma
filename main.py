from strategies.classics import *
from strategies.genetic import GENETIC

classics = [ALLC(), ALLD(), RAND(), GRIM(), TFT(), CTFT(), STFT(), TFTT(), PAVLOV(), NET_NICE()]

def reset(strategies):
    for strategy in strategies:
        strategy.reset()


