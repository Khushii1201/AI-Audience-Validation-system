class Session:

    def __init__(self, topic):
        self.topic = topic

    def __str__(self):
        return f"Session Topic: {self.topic}"