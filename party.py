from random import SystemRandom


class Party:
    def __init__(self, name, n, M):
        self.name = name
        self.M = M
        self.__secret_value = int(
            input("Enter a secret value for {}: ".format(name)))
        self.__random_values = []

        # Shared information between Parties
        self.shares = []
        self.column_sums = []

        # Generate n-1 random values
        for i in range(0, n-1):
            self.__random_values.append(SystemRandom().randint(0, self.M))
        self.__random_values.append(
            (self.__secret_value + self.M) - sum(self.__random_values) % self.M)

    def get_random_value(self, position):
        return self.__random_values[position]

    def give_random_value(self, random_value):
        self.shares.append(random_value)

    def get_column_sum(self):
        return sum(self.shares)

    def give_column_sum(self, column_sum):
        self.column_sums.append(column_sum)

    def calculate_f(self):
        return sum(self.column_sums) % self.M
