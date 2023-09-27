import numpy as np
import matplotlib
import random 
import math
from IPython.display import display, Math



def ackley(xi):
    a = 20
    b = 0.2
    c = 2 * math.pi
    sum1 = sum([(x ** 2) for x in xi])
    sum2 = sum([math.cos(c * x) for x in xi])
    term1 = -a * math.exp(-b * math.sqrt(sum1 / len(xi)))
    term2 = -math.exp(sum2 / len(xi))
    return term1 + term2 + a + math.exp(1)

def calc(xi, eq ):
    if eq == 1:
        res = np.sum([
            x**2
            for x in xi
            
        ])
        return res 
    if eq == 2:
        res = 100*((xi[0])**2 - xi[1])**2 + (1-xi[0])**2
        return res 
    if eq == 3:
        res = np.sum([
            abs(x)
            for x in xi
            
        ])
        #print(res)
        return res 
    if eq == 4:
        a = np.array([[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32],
                    [-32,-32,-32,-32,-32,-16,-16,-16,-16,-16, 0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]])
        res = 0.002
        for j in range(25):
            fj = j + np.sum([
                (xi[i] -a[i,j])**6
                for i in range(len(xi)) 
            ])
            res =res +1/fj 
        #print(res)
        res = 1/res 
        return res 
    if eq==5:
        res = 10*len(xi)+np.sum([
                ((xi[i])**2 -10*math.cos(2*math.pi*xi[i]))
                for i in range(len(xi)) 
            ])
        return res 
    if eq==6:
        res = np.sum([
                (-xi[i]*math.sin(math.sqrt(abs(xi[i]))))
                for i in range(len(xi)) 
            ])
        return res 
    if eq==7:
        res = np.sum([
                ((xi[i]**2)/4000)
                for i in range(len(xi)) 
            ])
        res2 = 1 
        for i in range(len(xi)):
            res2 = res2*math.cos(xi[i]/math.sqrt(i+1))
        res = res + res2 +1 
        return res 
    if eq == 8:
        # a =20
        # b=0.2
        # c=2*math.pi
        # sum1 = np.sum([
        #         ((xi[i]**2))
        #         for i in range(len(xi)) 
        #     ])
        # sum2 = np.sum([
        #         (math.cos(c*xi[i]))
        #         for i in range(len(xi)) 
        #     ])
        # res = -a*math.exp((sum1/len(xi))**(-1/b))-math.exp(sum2/len(xi))+a+math.exp(1)
        res = ackley(xi)
        return res


def selection(population, fit_chromosomes, generation,eq,pop_size ):
    fitnessscore=[]
    for chromosome in population:
        individual_fitness=calc(chromosome,eq )
        #print(individual_fitness)
        fitnessscore.append(individual_fitness)

    total_fitness=sum(fitnessscore)
    print('Total fitness: ', total_fitness)
    print('Average Fitness:', total_fitness/len(population))
    score_card=list(zip(fitnessscore,population))
    score_card.sort(reverse=False)

    for individual in score_card:
        if eq ==3:
            if individual[0]<=1.0:
                if individual[1] not in fit_chromosomes:
                    fit_chromosomes.append(individual[1])
        elif eq ==4:
            if individual[0]<=1.1:
                if individual[1] not in fit_chromosomes:
                    fit_chromosomes.append(individual[1])
        elif eq ==6:
            if individual[0]<=-400.0:
                if individual[1] not in fit_chromosomes:
                    fit_chromosomes.append(individual[1])
        else:
            if individual[0]<=0.1:
                if individual[1] not in fit_chromosomes:
                    fit_chromosomes.append(individual[1])
    #next_gen = int(4/10*(pop_size))
    next_gen=4
    score_card=score_card[:next_gen]
    score, population=zip(*score_card)
    return list(population),fit_chromosomes

def population_gen(i,up_bound,low_bound,pop_size):
    population = []
    for k in range(pop_size):
        gene = []
        for j in range(i):
            gene.append(random.uniform(up_bound,low_bound))
            
        population.append(gene)
    return population


def crossover(population,l  ):
    random.shuffle(population)
    fatherchromosome=population[:2]
    motherchromosome=population[2:]
    children=[]
    for i in range(len(fatherchromosome)):
        crossoversite=random.randint(0,l-1)
        fatherfragments=[fatherchromosome[i][:crossoversite],fatherchromosome[i][crossoversite:]]
        motherfragments=[motherchromosome[i][:crossoversite],motherchromosome[i][crossoversite:]]
        firstchild=fatherfragments[0]+motherfragments[1]
        children.append(firstchild)
        secondchild=motherfragments[0]+fatherfragments[1]
        children.append(secondchild)
    return children

def mutation(population,up_bound,low_bound,i,generation,generations):
    mutatedchromosomes=[]

    for chromosome in population:
        if random.randint(0,100) <= (int(100-100*(generation/generations))):
            mutation_site=random.randint(0,i-1)
            chromosome[mutation_site]=random.uniform(up_bound,low_bound)
            mutatedchromosomes.append(chromosome)
    return mutatedchromosomes



def get_fit_chromosomes(i,up_bound,low_bound,pop_size,generations,eq ):
    population = population_gen(i,up_bound,low_bound,pop_size)
    print("Starting Population: ",population)
    fit_chromosomes=[]
    for generation in range(generations):
        generation+=1
        print('Generation:', generation)
        population,fit_chromosomes =selection(population, fit_chromosomes, generation,eq,pop_size )
        crossover_children=crossover(population,i)
        population=population+crossover_children
        mutated_population=mutation(population,up_bound,low_bound,i,generation,generations)
        population=population+mutated_population
        #random.shuffle(population)
    return (population), fit_chromosomes 
