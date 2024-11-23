class Agent:
    def __init__(self, env, config):
        self.env = env
        self.config = config

    def act(self, state):
        raise NotImplementedError

    def learn(self, state, action, reward, next_state, done):
        raise NotImplementedError

    def save(self, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__