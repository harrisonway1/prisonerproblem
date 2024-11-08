import random
import matplotlib.pyplot as plt

# utils
def generate_valid_num(used_nums):
    num = random.randint(1,100)
    while num in used_nums:
        num = random.randint(1,100)
    return num

def generate_graph(data):
    plt.figure(figsize=(10, 5))
    turns = list(data.keys())
    frequencies = list(data.values())
    plt.bar(turns, frequencies, color='blue')
    plt.title('Number of Successful Prisoners in Random Choice')
    plt.xlabel('Suffessful Prisoners in Prisoner Problem')
    plt.ylabel('Frequency')
    plt.show()


class PrisonerProblem:
    def __init__(self):
        self.prisoners = [x for x in range(1, 101)]
        self.boxes = []
        self.prisoner_result_data = {}

    def create_boxes(self):
        used_numbers = set()
        while len(self.boxes) < 100:
            num = generate_valid_num(used_numbers)
            self.boxes.append(num)
            used_numbers.add(num)

    def clear_boxes(self):
        self.boxes = []

    def shuffle_boxes(self):
        random.shuffle(self.boxes)


class randomSolution(PrisonerProblem):
    def __init__(self):
        super().__init__()
    
    def sim_prisoner_turn(self, prisoner_num):
        visited = set()
        for turn in range(50):
            choice = random.randint(0, 99)
            while choice in visited:
                choice = random.randint(0,99)
            visited.add(choice)
            if self.boxes[choice] == prisoner_num:
                return True
        return False
    
    def iterate_prisoner_turn(self, iterations):
        for i in range(iterations):
            self.shuffle_boxes()
            tcount = 0
            for j in range(1, 101):
                if self.sim_prisoner_turn(j):
                    tcount += 1
            if tcount in self.prisoner_result_data:
                self.prisoner_result_data[tcount] += 1
            else:
                self.prisoner_result_data[tcount] = 1

eg1 = randomSolution()
eg1.create_boxes()
eg1.iterate_prisoner_turn(10000)
generate_graph(eg1.prisoner_result_data)
