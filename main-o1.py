def predict(dark_clouds, temperature_drop):
    storm = 0
    # if dark_clouds == 1 and temperature_drop == 1:
    #     storm = 1
    #
    return storm

# print(predict(0, 1))
# print(predict(1, 1))


import random


class Neuron:
    def __init__(self):
        self.w1 = random.random()
        self.w2 = random.random()
        self.t = random.random()

    def predict(self, dark_clouds, temperature_drop):
        storm = 0
        if (dark_clouds * self.w1 + temperature_drop * self.w2) > self.t:
            storm = 1
        return storm

    def learn(self, dark_clouds, temperature_drop, storm):
        error = self.predict(dark_clouds, temperature_drop) - storm
        self.w1 = error * dark_clouds / 100
        self.w2 = error * temperature_drop / 100
        self.t += error / 100

data = [[1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 1]]

def runTraining(neuron):
    for row in data:
        neuron.learn(row[0], row[1], row[2])

def runTesting(neuron):
    return [neuron.predict(row[0], row[1]) for row in data]

neuron = Neuron()

while True:
    output = runTesting(neuron)
    print("Predictions:", output)
    if output == [row[2] for row in data]:
        print("Training complete!")
        break

    runTraining(neuron)