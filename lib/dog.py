#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name  # Store the dog's name
        self.breed = breed  # Store the dog's breed, defaulting to "Mutt"

# Example usage:
fido = Dog("Fido")  # No breed provided, defaults to "Mutt"
buddy = Dog("Buddy", "Golden Retriever")  # Breed provided

# Accessing attributes
print(fido.name)   # Output: Fido
print(fido.breed)  # Output: Mutt

print(buddy.name)  # Output: Buddy
print(buddy.breed) # Output: Golden Retriever

pass