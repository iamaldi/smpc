from random import SystemRandom

class Party:
    def __init__(self, name, secretValue, n, M):
        self.name = name
        self.M = M
        self.__secretValue = secretValue
        self.__randomValues = []

        # Shared information between Parties
        self.shares = []
        self.columnSums = []

        # Generate n-1 random values
        for i in range(0, n-1):
            self.__randomValues.append(SystemRandom().randint(0, self.M))
        self.__randomValues.append((self.__secretValue + self.M) - sum(self.__randomValues) % self.M)

    # Give a random value to another Party
    def getRandomValue(self, position):
        return self.__randomValues[position]

    # Get a random value from another Party
    def giveRandomValue(self, randomValue):
        self.shares.append(randomValue)

    # Give your column sum to another Party
    def getColumnSum(self):
        return sum(self.shares)

    # Get a column sum from another Party
    def giveColumnSum(self, columnSum):
        self.columnSums.append(columnSum)

    # Calculate common function
    def calculateF(self):
        return sum(self.columnSums) % self.M