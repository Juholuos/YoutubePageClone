from time import sleep
a = """Moi mitä kuuluu?
tänään on ollut lämmin sää.
Onko sielläkin oLlut?"""

for line in a.splitlines():
    print(line)
    sleep(2)