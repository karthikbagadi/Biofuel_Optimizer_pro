"""
Particle Swarm Optimization
"""

import numpy as np
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

class ParticleSwarmOptimizer:
    """
    Particle Swarm Optimization for Biofuel Parameters
    """
    
    def __init__(self, model, scaler, feature_names, bounds, n_particles=30):
        self.model = model
        self.scaler = scaler
        self.feature_names = feature_names
        self.bounds = bounds
        self.n_particles = n_particles
        self.history = []
    
    def predict_yield(self, params):
        import pandas as pd
        params_df = pd.DataFrame([params], columns=self.feature_names)
        params_scaled = self.scaler.transform(params_df)
        return self.model.predict(params_scaled)[0]
    
    def optimize(self, iterations=100):
        """Run PSO optimization"""
        
        dim = len(self.bounds)
        
        # FIXED: Initialize particles within bounds correctly
        positions = np.zeros((self.n_particles, dim))
        for i in range(self.n_particles):
            for j in range(dim):
                positions[i, j] = np.random.uniform(self.bounds[j][0], self.bounds[j][1])
        
        velocities = np.random.uniform(-1, 1, (self.n_particles, dim))
        
        # Personal best
        pbest_pos = positions.copy()
        pbest_val = np.array([self.predict_yield(p) for p in positions])
        
        # Global best
        gbest_idx = np.argmax(pbest_val)
        gbest_pos = pbest_pos[gbest_idx].copy()
        gbest_val = pbest_val[gbest_idx]
        
        w = 0.7
        c1 = 1.5
        c2 = 1.5
        
        for iteration in range(iterations):
            for i in range(self.n_particles):
                r1, r2 = np.random.rand(2)
                
                velocities[i] = (w * velocities[i] +
                                c1 * r1 * (pbest_pos[i] - positions[i]) +
                                c2 * r2 * (gbest_pos - positions[i]))
                
                positions[i] = positions[i] + velocities[i]
                
                for j in range(dim):
                    positions[i][j] = np.clip(positions[i][j], self.bounds[j][0], self.bounds[j][1])
                
                current_val = self.predict_yield(positions[i])
                
                if current_val > pbest_val[i]:
                    pbest_val[i] = current_val
                    pbest_pos[i] = positions[i].copy()
                    
                    if current_val > gbest_val:
                        gbest_val = current_val
                        gbest_pos = positions[i].copy()
            
            self.history.append(gbest_val)
            
            if iteration % 20 == 0:
                logger.info(f"PSO Iter {iteration}: Best yield = {gbest_val:.2f} g/L")
        
        return {
            'optimal_params': {name: val for name, val in zip(self.feature_names, gbest_pos)},
            'optimal_yield': gbest_val,
            'history': self.history
        }
    
    def plot_convergence(self, save_path=None):
        plt.figure(figsize=(10, 6))
        plt.plot(self.history, linewidth=2, color='blue')
        plt.xlabel('Iteration')
        plt.ylabel('Best Yield (g/L)')
        plt.title('Particle Swarm Optimization Convergence')
        plt.grid(True, alpha=0.3)
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()