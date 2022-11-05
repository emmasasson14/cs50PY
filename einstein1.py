#get mass integer from the user
def main():
    mass = int(input())
    energy = convert(mass)
    print(energy)

#call function convert to convert m to E value
def convert(mass):
    energy = (mass * 90000000000000000)
    return energy

main()