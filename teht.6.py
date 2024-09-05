import random

def laske_pi_likiarvo(pisteiden_maara):
    n = 0

    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if x ** 2 + y ** 2 < 1:
            n += 1
    pi_likiarvo = 4 * n / pisteiden_maara
    return pi_likiarvo

def main():
    try:
        pisteiden_maara = int(input("Anna pisteiden määrä: "))
        if pisteiden_maara <= 0:
            print("Pisteiden määrän täytyy olla positiivinen kokonaisluku.")
            return

        pi_likiarvo = laske_pi_likiarvo(pisteiden_maara)
        print(f"Piin likiarvo on noin: {pi_likiarvo}")
    except ValueError:
        print("Syötteen täytyy olla kokonaisluku.")

if __name__ == "__main__":
    main()
