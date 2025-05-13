import random

class MolecularGenerator:
    def __init__(self):
        self.molecular_structures = ["C6H12O6", "C9H12N2O", "C16H18O2"]

    def generate_molecule(self):
        return random.choice(self.molecular_structures)
