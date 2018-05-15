import priority
class Task:
    id = 0
    opis = 0
    priorytet = 0

    def __init__(self, timestamp, description, prior):
        self.id = timestamp
        self.opis = description
        self.priorytet = priority.Priority(prior)

    def __str__(self):
        return "Task id:(" + str(self.id) + ") " + " opis:(" + str(self.opis) + ")" + "priorytet:(" + str(self.priorytet) + ")"
