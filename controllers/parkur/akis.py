class Parkur:
    def __init__(self):
        self.state, self.x, self.gas = "HAZIR", 0.0, 400

    def step(self, dt, key=""):
        if key == "H":
            self.gas = 850
        elif key == "L":
            self.gas = 400
        if self.state == "HAZIR" and self.gas > 600:
            self.state = "ILERI"
        elif self.state == "UCTA" and key == "G":
            self.state = "GERI"
        elif self.state == "BEKLE" and self.gas <= 450:
            self.state = "HAZIR"
        if self.state == "ILERI":
            self.x = min(1.0, self.x + dt / 2)
            if self.x == 1.0:
                self.state = "UCTA"
        elif self.state == "GERI":
            self.x = max(0.0, self.x - dt / 2)
            if self.x == 0.0:
                self.state = "BEKLE"
