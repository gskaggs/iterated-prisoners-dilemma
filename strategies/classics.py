import random

class ALLC():
    name = "ALLC"

    def __init__(self):
        self.score = 0

    def next_action(self):
        return "C"

    def observe_actions(self, opponent, own):
        pass

    def reset(self):
        pass
        
class ALLD():
    name = "ALLD"

    def __init__(self):
        self.score = 0

    def next_action(self):
        return "D"

    def observe_actions(self, opponent, own):
        pass
    
    def reset(self):
        pass

class RAND():
    name = "RAND"

    def __init__(self):
        self.score = 0

    def next_action(self):
        return random.choice(["C", "D"])

    def observe_actions(self, opponent, own):
        pass
    
    def reset(self):
        pass

class GRIM():
    name = "GRIM"

    def __init__(self):
        self.triggered = False
        self.score = 0

    def next_action(self):
        if self.triggered:
            return "D"
        else:
            return "C"
    
    def observe_actions(self, opponent, own):
        self.triggered = self.triggered or opponent == "D"
    
    def reset(self):
        self.triggered = False

class TFT():
    name = "TFT"

    def __init__(self):
        self.prev = "C"
        self.score = 0

    def next_action(self):
        return self.prev

    def observe_actions(self, opponent, own):
        self.prev = opponent

    def reset(self):
        self.prev = "C"

class CTFT():
    name = "CTFT"
    def __init__(self):
        self.status = "content"
        self.score = 0

    def next_action(self):
        if self.status == "content" or self.status == "contrite":
            return "C"
        else:
            return "D"

    def observe_actions(self, opponent, own):
        if self.status == "content":
            if opponent == "D" and own == "C":
                self.status = "provoked"
            if opponent == "C" and own == "D":
                self.status = "contrite"
        elif self.status == "contrite" and own == "C":
            self.status = "content"
        elif self.status == "provoked" and opponent == "C":
            self.status = "content"
    
    def reset(self):
        self.status = "content"

class STFT():
    name = "STFT"

    def __init__(self):
        self.prev = "D"
        self.score = 0

    def next_action(self):
        return self.prev

    def observe_actions(self, opponent, own):
        self.prev = opponent

    def reset(self):
        self.prev = "D"

class TFTT():
    name = "TFTT"

    def __init__(self):
        self.prev = ["D", "D"]
        self.score = 0

    def next_action(self):
        if self.prev[0] == "C" or self.prev[1] == "C":
            return "C"
        return "D"

    def observe_actions(self, opponent, own):
        self.prev[1] = self.prev[0]
        self.prev[0] = opponent

    def reset(self):
        self.prev = ["D", "D"]

class PAVLOV():
    name = "PAVLOV"

    def __init__(self):
        self.next = "C"
        self.score = 0

    def next_action(self):
        return self.next

    def observe_actions(self, opponent, own):
        if opponent == "D":
            self.next = "C" if self.next == "D" else "D"

    def reset(self):
        self.next = "C"

class NET_NICE():
    name = "NET_NICE"

    def __init__(self):
        self.own_defects = 0
        self.opp_defects = 0
        self.score = 0

    def next_action(self):
        return "C" if self.own_defects >= self.opp_defects else "D" 

    def observe_actions(self, opponent, own):
        if opponent == "D":
            self.opp_defects += 1
        if own == "D":
            self.own_defects += 1

    def reset(self):
        self.own_defects = 0
        self.opp_defects = 0