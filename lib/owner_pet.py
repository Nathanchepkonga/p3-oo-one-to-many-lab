class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet to the all list
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet {self.name}, Type: {self.pet_type}, Owner: {self.owner.name if self.owner else 'No owner'}>"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner."""
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("You can only add a Pet instance.")

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)

