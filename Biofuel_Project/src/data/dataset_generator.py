"""
Biofuel Dataset Generator - Complex Biochemical Simulation
Based on Michaelis-Menten kinetics and fermentation dynamics
"""

import numpy as np
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BiofuelDatasetGenerator:
    """
    Advanced synthetic dataset generator for biofuel production
    Incorporates:
    - Michaelis-Menten enzyme kinetics
    - Arrhenius temperature dependence
    - pH inhibition curves
    - Substrate inhibition at high concentrations
    """
    
    def __init__(self, config, random_seed=42):
        self.config = config
        np.random.seed(random_seed)
    
    def generate_parameters(self, n_samples):
        """Generate realistic process parameters"""
        
        temp = np.random.normal(35, 2.5, n_samples)
        temp = np.clip(temp, 30, 40)
        
        time = np.random.lognormal(mean=4.0, sigma=0.5, size=n_samples)
        time = np.clip(time, 24, 96)
        
        ph = np.random.beta(a=5, b=3, size=n_samples) * 1.5 + 4.5
        ph = np.clip(ph, 4.5, 6.0)
        
        substrate = np.random.uniform(50, 200, n_samples)
        enzyme = 0.15 * substrate + np.random.normal(0, 5, n_samples)
        enzyme = np.clip(enzyme, 10, 40)
        
        inoculum = np.random.gamma(shape=3, scale=2, size=n_samples)
        inoculum = np.clip(inoculum, 5, 20)
        
        return pd.DataFrame({
            'Temperature_C': np.round(temp, 1),
            'Time_hours': np.round(time, 1),
            'pH': np.round(ph, 2),
            'Enzyme_mL': np.round(enzyme, 1),
            'Substrate_gL': np.round(substrate, 1),
            'Inoculum_mL': np.round(inoculum, 1)
        })
    
    def michaelis_menten(self, enzyme, substrate):
        """Michaelis-Menten enzyme kinetics"""
        Vmax = 25.0
        Km = 30.0
        return Vmax * (enzyme / 20) * (substrate / (Km + substrate))
    
    def arrhenius_factor(self, temp, T_opt=35):
        """Temperature dependence using Arrhenius equation"""
        Ea = 50
        R = 0.008314
        T_k = temp + 273.15
        T_opt_k = T_opt + 273.15
        return np.exp(-Ea / R * (1/T_k - 1/T_opt_k))
    
    def ph_inhibition(self, ph, ph_opt=5.2):
        """pH inhibition curve"""
        sigma = 0.4
        return np.exp(-((ph - ph_opt)**2) / (2 * sigma**2))
    
    def calculate_yield(self, params):
        """Calculate biofuel yield using integrated kinetic model"""
        
        temp = params['Temperature_C'].values
        time = params['Time_hours'].values
        ph = params['pH'].values
        enzyme = params['Enzyme_mL'].values
        substrate = params['Substrate_gL'].values
        inoculum = params['Inoculum_mL'].values
        
        base_yield = self.michaelis_menten(enzyme, substrate)
        temp_factor = self.arrhenius_factor(temp)
        ph_factor = self.ph_inhibition(ph)
        
        time_factor = 1 - np.exp(-0.05 * time)
        inoculum_factor = 1 / (1 + np.exp(-0.3 * (inoculum - 12)))
        
        yield_value = base_yield * temp_factor * ph_factor * time_factor * inoculum_factor
        
        interaction = 0.05 * (enzyme / 20) * (substrate / 100) * (temp / 35)
        yield_value = yield_value + interaction
        
        noise = np.random.normal(0, 0.8, len(yield_value))
        yield_value = yield_value + noise
        
        yield_value = np.clip(yield_value, 5, 30)
        
        return np.round(yield_value, 2)
    
    def generate_full_dataset(self, n_samples=5000):
        """Generate complete dataset"""
        
        logger.info(f"Generating {n_samples} samples...")
        params = self.generate_parameters(n_samples)
        yield_value = self.calculate_yield(params)
        
        df = params.copy()
        df['Biofuel_Yield_gL'] = yield_value
        
        logger.info(f"Dataset generated: {df.shape[0]} rows")
        return df


if __name__ == "__main__":
    generator = BiofuelDatasetGenerator(None)
    df = generator.generate_full_dataset(1000)
    df.to_csv('../../data/raw/biofuel_raw.csv', index=False)
    print(df.head())