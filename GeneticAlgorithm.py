# A Python-based Genetic Algorithm
import random
import numpy as np

things = [
    ['Computer',[1000,10]],
    ['Headphones',[50,5]],
    ['Charger',[20,1]],
    ['Bracelet',[400,2]],
    ['TV',[900,40]],
    ['XBox',[300,10]],
    ['DVD Player',[40, 7]],
    ['Lamp', [20, 15]],
    ['Guitar', [250, 20]],
    ['Desk', [100, 80]]
]

population = 500
limit = 180

class GeneticAlgorithm:

    def __init__(self, iterable, population_size=100):
        self.iterable = iterable
        self.population_size = population_size
    '''
    iterable: the thing you want to find optimal parameters for. Formatted as:
    things = [
    ['Computer',[1000,10]],
    ['Headphones',[50,5]],
    ['Charger',[20,1]],
    ['Bracelet',[400,20]],
    ['TV',[900,40]],
    ['XBox',[300,10]]
    ]

    population_size: the population size of the original group of genomes.
    '''
    # def prepare_population(self, iterable):
    #     '''
    #     Sorts and eliminates duplicates in population (Ascending order).
    #     '''
    #     non_duplicates = []
    #     for i in iterable:
    #         if i not in non_duplicates:
    #             non_duplicates.append(i)
    #     return non_duplicates
            
    def generate_chromosome(self):
        '''
        Generates a list of random boolean values for all items in iterable. Used as the parent chromosomes in a genetic algorithm.
        '''
        self.chromosome = [random.choice([1,0]) for i in range(len(self.iterable))]
        return self.chromosome

    def generate_population(self):
        '''
        Generates the population of initial chromosome in a genetic algorithm. Takes two parameters:
        iterable: The thing that it creates chromosomes of (dictionary, list, etc.).
        amount: How much chromosomes you want in the population (default: 100)
        '''

        self.population = [self.generate_chromosome() for i in range(self.population_size)]
        self.population_size = len(self.population)
        return self.population

    def crossover(self, parents, point):
        '''
        parents: The two parent chromosomes that are used to make children.
        crossover_rate: The rate at which crossover occurs in the reproduction process. (As a whole number e.g. '50' is fifty percent)
        mutation_rate:  The rate which mutation occurs in the reproduction process. (As a whole number e.g. '5' is five percent)
        '''

        parent1 = np.array(parents[0][0])
        parent2 = np.array(parents[1][0])
        self.child1=np.append(parent1[point:], parent2[:point])
        self.child2=np.append(parent2[point:], parent1[:point])
        # print(self.child1, self.child2)
        return [list(self.child1), list(self.child2)]
        # for count, p in enumerate(parents):
        #     i = count
        #     print(i)
        #     if random.randint(0,100) < crossover_rate:
        #         print('Initiating Crossover')
        #         rand = random.randint(0, len(parents[0][0])-1)
        #         for j in range(rand):
        #             self.child1.append(parents[i][0][j])
        #             self.child2.append(parents[i][0][j])
        #         for k in range(len(parents[0][0])-rand):
        #             self.child1.append(parents[i][0][j+k])
        #             self.child2.insert(0, parents[i][0][j+k])

        #     if random.randint(0,100) < mutation_rate:
        #         mutrand = random.randint(0,1)
        #         p = random.randint(0, len(self.child1))
        #         if mutrand == 0:
        #             if self.child1[p] == 1:
        #                 self.child1[p] = 0
        #             else:
        #                 self.child1[p] = 1

        #         else:
        #             if self.child2[p] == 1:
        #                 self.child2[p] = 0
        #             else:
        #                 self.child2[p] = 1
        # return [self.child1, self.child2]


    def tournament(self, fitness_data):
        self.fitness_length = len(fitness_data)
        self.selected_first = []
        for i in range(2):
            self.selected_first.append(fitness_data[random.randint(0, self.fitness_length-1)])
        self.selected_second = []
        for i in range(2):
            self.selected_second.append(fitness_data[random.randint(0, self.fitness_length-1)])

        if self.selected_first[0][1]>self.selected_first[1][1]:
            self.first_highest = self.selected_first[0]
        else:
            self.first_highest = self.selected_first[1]
        if self.selected_second[0][1]>self.selected_second[1][1]:
            self.second_highest = self.selected_second[0]
        else:
            self.second_highest = self.selected_second[1]
        self.result = [self.first_highest, self.second_highest]
        # print(self.selected_first, self.selected_second)
        return self.result

    def original_generation(self):
        pop = find_fitness(algo.generate_population(), things, limit)
        return pop

    def generate_generation(self, pop, crossover_rate, point):
        res = []
        for i in range(len(pop)):
            tourn = self.tournament(pop)
            rand = random.randint(0, 100)
            if rand < crossover_rate:
                for j in self.crossover(tourn, point):
                    res.append(j)
        return res
    def average_fitness(self, population):
        sum = 0
        for count, i in enumerate(population):
            sum += population[count-1][1]
        try:
            return sum/len(population)
        except:
            return 0
def find_fitness(population, iterable, limit):
        '''
        Finds the fitness of a population of chromosomes. This function will change depending on your application of a genetic algorithm.
        In this case, it returns the sum of all true (1) boolean values in each chromosome, depending on your iterable (list of ).
        If the sum exceeds the limit, the fitness score of the chromosome is returned as zero.
        This fitness function is intended to solve the knapsack problem, where the maximum value of items is found, not exceeding a weight limit.
        This function returns a list of lists, each containing the chromosome and the fitness score.

        Example:
        [
            [[1,0,1,0,1],7]
            ...
        ]
        '''
        new_list = []
        for chromosome in population:
            value = 0
            weight = 0
            for count, gene in enumerate(chromosome):
                if gene == 1:
                    value += iterable[count][1][0]
                    weight += iterable[count][1][1]
            if weight < limit and value != 0:
                new_list.append([chromosome, value])
        return new_list

algo = GeneticAlgorithm(things, population_size=population)
#tresult = algo.tournament(find_fitness(algo.generate_population(), things, limit))
#print(tresult)
#print(algo.crossover(tresult, 50, 5, 3))
#print(algo.generate_generation(algo.original_generation(), 50, 3))

final_gen = find_fitness(algo.generate_generation(algo.original_generation(), 50, 3), things, limit)
for i in range(20):
    print(f'Generation: {i} ({algo.average_fitness(final_gen)})')
    final_gen = find_fitness(algo.generate_generation(final_gen, 50, 3), things, limit)

maximum = 0
chromosome = []
for i in final_gen:
    if i[1] > maximum:
        maximum = i[1]
        chromosome = i[0] 
print(chromosome,': ', maximum)