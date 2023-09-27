import random
random.seed(100)

def selection(population, fit_chromosomes, generation):
    fitnessscore=[]
    for chromosome in population:
        individual_fitness=100-abs(30-(chromosome[0]+2*chromosome[1]-3*chromosome[2]+chromosome[3]+4*chromosome[4]+chromosome[5]))
        fitnessscore.append(individual_fitness)

    total_fitness=sum(fitnessscore)
    print('Total fitness: ', total_fitness)
    score_card=list(zip(fitnessscore,population))
    score_card.sort(reverse=True)

    for individual in score_card:
        if individual[0]==100:
            if individual[1] not in fit_chromosomes:
                fit_chromosomes.append(individual[1])
    
    score_card=score_card[:4]
    score, population=zip(*score_card)
    return list(population)

def crossover(population):
    random.shuffle(population)
    fatherchromosome=population[:2]
    motherchromosome=population[2:]
    children=[]
    for i in range(len(fatherchromosome)):
        crossoversite=random.randint(1,5)
        fatherfragments=[fatherchromosome[i][:crossoversite],fatherchromosome[i][crossoversite:]]
        motherfragments=[motherchromosome[i][:crossoversite],motherchromosome[i][crossoversite:]]
        firstchild=fatherfragments[0]+motherfragments[1]
        children.append(firstchild)
        secondchild=motherfragments[0]+fatherfragments[1]
        children.append(secondchild)
    return children

def mutation(population):
    mutatedchromosomes=[]
    for chromosome in population:
        mutation_site=random.randint(0,5)
        chromosome[mutation_site]=random.randint(1,9)
        mutatedchromosomes.append(chromosome)
    return mutatedchromosomes

def get_fit_chromosomes(generations):
    population=[[random.randint(1,9) for i in range(6)] for j in range(6)]
    fit_chromosomes=[]
    for generation in range(generations):
        generation+=1
        print('Generation:', generation)
        population=selection(population, fit_chromosomes, generation)
        crossover_children=crossover(population)
        population=population+crossover_children
        mutated_population=mutation(population)
        population=population+mutated_population
        #random.shuffle(population)

    return fit_chromosomes

solution=get_fit_chromosomes(100)
print('-----------Solution-----------')
print(solution)
print(len(solution))