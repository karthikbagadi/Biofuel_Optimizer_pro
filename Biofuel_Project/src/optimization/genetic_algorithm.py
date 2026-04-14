"""
Genetic Algorithm Optimization
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

class GeneticAlgorithmOptimizer:
    """
    Genetic Algorithm for Biofuel Parameter Optimization
    """
    
    def __init__(self, model, scaler, feature_names, bounds, population_size=50):
        self.model = model
        self.scaler = scaler
        self.feature_names = feature_names
        self.bounds = bounds
        self.population_size = population_size
        self.history = []
    
    def predict_yield(self, params):
        """Predict yield for given parameters"""
        import pandas as pd
        params_df = pd.DataFrame([params], columns=self.feature_names)
        params_scaled = self.scaler.transform(params_df)
        return self.model.predict(params_scaled)[0]
    
    def initialize_population(self):
        """Create initial random population"""
        population = []
        for _ in range(self.population_size):
            individual = []
            for i, (low, high) in enumerate(self.bounds):
                individual.append(random.uniform(low, high))
            population.append(individual)
        return population
    
    def fitness(self, individual):
        """Calculate fitness (higher is better)"""
        return self.predict_yield(individual)
    
    def selection(self, population, fitness_scores):
        """Tournament selection"""
        selected = []
        for _ in range(len(population)):
            i1 = random.randint(0, len(population)-1)
            i2 = random.randint(0, len(population)-1)
            if fitness_scores[i1] > fitness_scores[i2]:
                selected.append(population[i1].copy())
            else:
                selected.append(population[i2].copy())
        return selected
    
    def crossover(self, parent1, parent2):
        """Uniform crossover"""
        child = []
        for i in range(len(parent1)):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        return child
    
    def mutate(self, individual, mutation_rate=0.1):
        """Gaussian mutation"""
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                noise = random.gauss(0, 0.1 * (self.bounds[i][1] - self.bounds[i][0]))
                individual[i] += noise
                individual[i] = np.clip(individual[i], self.bounds[i][0], self.bounds[i][1])
        return individual
    
    def optimize(self, generations=100):
        """Run genetic algorithm optimization"""
        
        population = self.initialize_population()
        best_fitness_history = []
        
        for gen in range(generations):
            fitness_scores = [self.fitness(ind) for ind in population]
            best_idx = np.argmax(fitness_scores)
            best_fitness = fitness_scores[best_idx]
            best_fitness_history.append(best_fitness)
            
            selected = self.selection(population, fitness_scores)
            
            new_population = []
            for i in range(0, len(selected), 2):
                if i+1 < len(selected):
                    child1 = self.crossover(selected[i], selected[i+1])
                    child2 = self.crossover(selected[i+1], selected[i])
                    child1 = self.mutate(child1)
                    child2 = self.mutate(child2)
                    new_population.extend([child1, child2])
            
            population = new_population[:self.population_size]
            
            if gen % 20 == 0:
                logger.info(f"GA Gen {gen}: Best yield = {best_fitness:.2f} g/L")
        
        self.history = best_fitness_history
        
        final_scores = [self.fitness(ind) for ind in population]
        best_idx = np.argmax(final_scores)
        best_params = population[best_idx]
        best_yield = final_scores[best_idx]
        
        return {
            'optimal_params': {name: val for name, val in zip(self.feature_names, best_params)},
            'optimal_yield': best_yield,
            'history': best_fitness_history
        }
    
    def plot_convergence(self, save_path=None):
        """Plot convergence history"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.history, linewidth=2, color='green')
        plt.xlabel('Generation')
        plt.ylabel('Best Yield (g/L)')
        plt.title('Genetic Algorithm Convergence')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()