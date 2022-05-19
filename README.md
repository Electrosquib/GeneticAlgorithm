# GeneticAlgorithm
A completely scratch-built genetic algorithm class written in python.
- Requires only Numpy.

How it works:
A genetic algorithm, as the name implies, simulates biological evolution in code in order to solve (or estimate) a given problem.
In real-life, animals have evolved to survive all kinds of environments and climates, and we learned from biology that code can do the same. 

1: The first step in this genetic algorithm is creating the genome, this is kind of like the organism that we are replicating. It is represented by boolean values in a list. At first, the genome is generated completely by random, but in future generations, the genomes inherit from their parents.

2: Next, the algorithm generates a population of these genomes, which will represent a single generation in this experiment. This is specified in the class object's instantiation. 

3: In the third step, the genetic algorithm finds the fitness for each genome in the population. The fitness function returns a value that defines how well a genome performs. In the code, I have included a built-in function tailored to the knapsack problem (explored below), but your fitness function will change depending on your application. The fitness function is one thing you will have to code yourself depending on your situation. 

4: Next, two genomes at random are chosen out of the population and pitted together in a tournement. The genome with the highest fitness score will win. The same thing is repeated again, and the two winners are stored. There is also another method of parent-finding called the roulette wheel, which factors in a genome's fitness score, but this method is not incorporated in this algorithm.

5: At this point, the two winners undergo a crossover operation. This means that genes to either side of a certain crossover point are switched around in the two genomes. This occurs in nature when a chromosome breaks and then reconnects differently. In the algorithm, the crossover point is fixed and should be assigned to an integer less than the length of your genomes in the function call. There is sometimes another option at this point to incorporate mutation in the genome. This means that at random (determined by your specified mutation rate) a single gene value is flipped. This code does not incorporate mutations, but it is easy to implement on your own. You also need to specify your crossover rate percentage chance. This is an integer between 0-100 and determines how often the crossover is done.

6: Steps 4-5 are repeated until the number of children in the new generation matches the old population. You now have an entirely new population whos genomes should perform slightly better in your fitness function than your original population. The tournament, crossover, and mutation are then repeated on this population to produce a new generation. The cycle continues until it iterates through how much generations you specified. The average fitness of the populations should mostly increase with time until it levels off eventually. At this point, the population is pretty optimized and the highest-performing genome of the final generation is printed to the console. 

Other than that, I think the code is pretty self-explanatory as I have included comments on the different functions. I hope you have learned something from using this class and that it helped you out. Many thanks for checking it out!
