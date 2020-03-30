class Shark:
    def swim(self):
        print("Акула пливе.")

    def skeleton(self):
        print("Скелет акули складається з хрящів.")


class Clownfish:
    def swim(self):
        print("Риба Немо пливе.")

    def skeleton(self):
        print("Скелет риби Немо складається з кісток.")

clown = Clownfish()
shark = Shark()

fishes = [clown, shark]

for fish in fishes:
    fish.skeleton()