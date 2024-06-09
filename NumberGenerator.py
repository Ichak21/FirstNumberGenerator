class NumberGenerator():
    
    def __init__(self) -> None:
        pass
    
    def _isPrime(self, number:int, previous:list):
        check = True
        for prime in previous:
            if number % prime == 0  and prime != 1 :
                check = False
        return check

    def generate(self, nb_numbers:int):
        listPrime =[1]
        number = 2
        
        while nb_numbers > 0:
            if self._isPrime(number, listPrime):
                listPrime.append(number)
                nb_numbers -= 1
            number += 1
        return listPrime
            
            
def main():
    generator = NumberGenerator()
    print(generator.generate(1000000))

if __name__ == "__main__":
    main()