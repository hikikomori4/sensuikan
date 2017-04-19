TANK_STATUS_OK = 0
TANK_STATUS_ERROR = 1

class Tank:

    def __init__(self, name, capacity, state):
        self.name = name
        self.capacity = capacity
        self.state = state

tanks = [
    Tank('Носовая дифферентная цистерна', 1000, TANK_STATUS_OK),
    Tank('Кормовая дифферентная цистерна', 1000, TANK_STATUS_OK)
]




https://github.com/fasafgf/tmp/blob/master/tmp.py#L2


