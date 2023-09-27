import random
random.seed(100)

def selection(population, fit_chromosomes):
    fitnessscore=[]
    for chromosome in population:
        individual_fitness=100-abs(30-(chromosome[0]+2*chromosome[1]-3*chromosome[2]+chromosome[3]+4*chromosome[4]+chromosome[5]))
        fitnessscore.append(individual_fitness)

    print('Fitness score:', fitnessscore)
    total_fitness=sum(fitnessscore)
    print('Total fitness:', total_fitness)
    score_card=list(zip(fitnessscore,population))
    print('Score card:', score_card)
    score_card.sort(reverse=True)
    print('Score card sorted:', score_card)

    for individual in score_card:
        if individual[0]==100:
            if individual[1] not in fit_chromosomes:
                fit_chromosomes.append(individual[1])
    print(fit_chromosomes)
    
    score_card=score_card[:4]
    score, population=zip(*score_card)
    return list(population)

fit_chromosomes=[]
population=[[random.randint(1,9) for i in range(6)] for j in range(6)]
print(population)
print(selection(population, fit_chromosomes))




import random
def crossover(population):
    random.shuffle(population)
    fatherchromosome=population[:2]
    motherchromosome=population[2:]
    children=[]
    for i in range(len(fatherchromosome)):
        crossoversite=random.randint(1,5)
        print('Crossoversite: ', crossoversite)
        fatherfragments=[fatherchromosome[i][:crossoversite],fatherchromosome[i][crossoversite:]]
        motherfragments=[motherchromosome[i][:crossoversite],motherchromosome[i][crossoversite:]]
        firstchild=fatherfragments[0]+motherfragments[1]
        children.append(firstchild)
        secondchild=motherfragments[0]+fatherfragments[1]
        children.append(secondchild)
        print('Father fragment: '+str(fatherfragments) +'and Mother fragment:' +str(motherfragments)+' formed firstchild: '+str(firstchild)+' and secondchild: '+str(secondchild))
    return children


population=[[5, 4, 3, 3, 4, 6], [3, 8, 8, 3, 7, 6], [5, 7, 3, 2, 3, 1], [7, 9, 2, 9, 2, 2]]
crossover_children=crossover(population)
print('Crossover_children:', crossover_children)
population=population+crossover_children
print('Population Now:', population)


def mutation(population):
    mutatedchromosomes=[]
    for chromosome in population:
        mutation_site=random.randint(0,5)
        print('Original chromosome:', chromosome)
        chromosome[mutation_site]=random.randint(1,9)
        print('Mutation site:', mutation_site)
        print('Mutated chromosome:', chromosome)
        mutatedchromosomes.append(chromosome)
    return mutatedchromosomes

population=[[3, 8, 8, 3, 7, 6], [5, 4, 3, 3, 4, 6], [5, 7, 3, 2, 3, 1], [7, 9, 2, 9, 2, 2], [3, 8, 8, 3, 7, 1], [5, 7, 
3, 2, 3, 6], [5, 9, 2, 9, 2, 2], [7, 4, 3, 3, 4, 6]]

mutated_population=mutation(population)
print('Mutated Population: ', mutated_population)
population=population+mutated_population



def get_fit_chromosomes(generations):
    population=[[random.randint(1,9) for i in range(6)] for j in range(6)]
    fit_chromosomes=[]
    for generation in range(generations):
        generation+=1
        population=selection(population, fit_chromosomes, generation)
        crossover_children=crossover(population)
        population=population+crossover_children
        mutated_population=mutation(population)
        population=population+mutated_population
        #random.shuffle(population)

    return fit_chromosomes