import random
import time

# Kézrázás szimulálása
def shake_hands():
    print("Kézrázás...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Kész!")
    time.sleep(0.5)

# Random szám generálása 1 és 5 között
def shake_and_generate_number():
    shake_hands()  # Kézrázás
    random_number = random.randint(1, 5)  # Random szám generálása
    print(f"A generált szám: {random_number}")

# Program futtatása
if __name__ == "__main__":
    shake_and_generate_number()

## vauuuuuu nagy kiraly vagyok
