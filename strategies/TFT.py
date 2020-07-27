class TFT():
    def __init__(self):
        self.prev = "C"

    def get_action(self):
        return self.prev

    def record_actions(self, opponent, own):
        self.prev = opponent
        
