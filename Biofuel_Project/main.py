"""
COMPLETE COMPLEX PROJECT - Main Execution File
Includes: Multi-model comparison, Advanced optimization, Comprehensive reporting
"""

import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data.dataset_generator import BiofuelDatasetGenerator
from src.models.random_forest_model import OptimizedRandomForest
from src.models.xgboost_model import OptimizedXGBoost
from src.optimization.differential_evolution import MultiObjectiveOptimizer
from src.optimization.genetic_algorithm import GeneticAlgorithmOptimizer
from src.optimization.particle_swarm import ParticleSwarmOptimizer
from src.utils.logger import setup_logger, ExperimentLogger

print("="*70)
print("COMPLETE COMPLEX BIOFUEL OPTIMIZATION SYSTEM")
print("Advanced AI Framework for Sustainable Energy Production")
print("="*70)

# Setup Logger
logger = setup_logger('results/logs/experiment.log')
exp_logger = ExperimentLogger("Biofuel_Optimization_Complete")

print("\n[STEP 1] Generating Advanced Dataset...")
generator = BiofuelDatasetGenerator(None, random_seed=42)
df = generator.generate_full_dataset(5000)
df.to_csv('data/raw/biofuel_raw.csv', index=False)
print(f"✅ Dataset: {df.shape[0]} samples, {df.shape[1]} features")

# Prepare data
features = ['Temperature_C', 'Time_hours', 'pH', 'Enzyme_mL', 'Substrate_gL', 'Inoculum_mL']
target = 'Biofuel_Yield_gL'

X = df[features]
y = df[target]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================
# SECTION 1: MULTIPLE MODEL COMPARISON
# ============================================

print("\n" + "="*70)
print("SECTION 1: MODEL COMPARISON")
print("="*70)

# Model 1: Random Forest
print("\n[Model 1] Training Random Forest...")
rf_model = OptimizedRandomForest({'models': {'random_forest': {}}})
rf_model.train(X_train_scaled, y_train)
rf_metrics = rf_model.evaluate(X_test_scaled, y_test)
print(f"   R²: {rf_metrics['R2']:.4f}, MAE: {rf_metrics['MAE']:.2f} g/L")

# Model 2: XGBoost
print("\n[Model 2] Training XGBoost...")
xgb_model = OptimizedXGBoost({})
xgb_model.train(X_train_scaled, y_train)
xgb_metrics = xgb_model.evaluate(X_test_scaled, y_test)
print(f"   R²: {xgb_metrics['R2']:.4f}, MAE: {xgb_metrics['MAE']:.2f} g/L")

# Model Comparison
print("\n📊 MODEL COMPARISON:")
print("-"*50)
print(f"{'Model':<15} {'R² Score':<12} {'MAE (g/L)':<12}")
print("-"*50)
print(f"{'Random Forest':<15} {rf_metrics['R2']:.4f}       {rf_metrics['MAE']:.2f}")
print(f"{'XGBoost':<15} {xgb_metrics['R2']:.4f}       {xgb_metrics['MAE']:.2f}")
print("-"*50)

# Select best model
best_model = rf_model if rf_metrics['R2'] > xgb_metrics['R2'] else xgb_model
best_model_name = "Random Forest" if rf_metrics['R2'] > xgb_metrics['R2'] else "XGBoost"
print(f"\n✅ Best Model: {best_model_name}")

# ============================================
# SECTION 2: FEATURE IMPORTANCE ANALYSIS
# ============================================

print("\n" + "="*70)
print("SECTION 2: FEATURE IMPORTANCE ANALYSIS")
print("="*70)

importance = best_model.model.feature_importances_
print("\n📊 FEATURE IMPORTANCE RANKING:")
for name, imp in sorted(zip(features, importance), key=lambda x: x[1], reverse=True):
    print(f"   {name:<20}: {imp*100:.1f}%")

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.barh(features, importance, color=['darkgreen' if i==0 else 'lightgreen' for i in range(len(features))])
plt.xlabel('Importance')
plt.title('Feature Importance for Biofuel Yield Prediction')
plt.tight_layout()
plt.savefig('results/figures/feature_importance.png', dpi=300)
print("\n✅ Graph saved: results/figures/feature_importance.png")

# ============================================
# SECTION 3: MULTI-ALGORITHM OPTIMIZATION
# ============================================

print("\n" + "="*70)
print("SECTION 3: MULTI-ALGORITHM OPTIMIZATION")
print("="*70)

bounds = [(30, 40), (24, 96), (4.5, 6.0), (10, 40), (50, 200), (5, 20)]

# Optimization 1: Differential Evolution
print("\n[Optimizer 1] Differential Evolution...")
from scipy.optimize import differential_evolution
def objective(params):
    import pandas as pd
    params_df = pd.DataFrame([params], columns=features)
    params_scaled = scaler.transform(params_df)
    return -best_model.model.predict(params_scaled)[0]

de_result = differential_evolution(objective, bounds, maxiter=100, popsize=30, seed=42)
de_yield = -de_result.fun
de_params = de_result.x
print(f"   Yield: {de_yield:.2f} g/L")

# Optimization 2: Genetic Algorithm
print("\n[Optimizer 2] Genetic Algorithm...")
ga_optimizer = GeneticAlgorithmOptimizer(best_model.model, scaler, features, bounds, population_size=40)
ga_result = ga_optimizer.optimize(generations=80)
ga_yield = ga_result['optimal_yield']
print(f"   Yield: {ga_yield:.2f} g/L")

# Optimization 3: Particle Swarm Optimization
print("\n[Optimizer 3] Particle Swarm Optimization...")
pso_optimizer = ParticleSwarmOptimizer(best_model.model, scaler, features, bounds, n_particles=30)
pso_result = pso_optimizer.optimize(iterations=80)
pso_yield = pso_result['optimal_yield']
print(f"   Yield: {pso_yield:.2f} g/L")

# Optimization Comparison
print("\n📊 OPTIMIZATION ALGORITHM COMPARISON:")
print("-"*50)
print(f"{'Algorithm':<25} {'Optimal Yield (g/L)':<20}")
print("-"*50)
print(f"{'Differential Evolution':<25} {de_yield:.2f}")
print(f"{'Genetic Algorithm':<25} {ga_yield:.2f}")
print(f"{'Particle Swarm':<25} {pso_yield:.2f}")
print("-"*50)

# Select best optimizer
yields = {'DE': de_yield, 'GA': ga_yield, 'PSO': pso_yield}
best_algo = max(yields, key=yields.get)
print(f"\n✅ Best Optimization Algorithm: {best_algo} with {yields[best_algo]:.2f} g/L")

# ============================================
# SECTION 4: COMPLETE REPORT GENERATION
# ============================================

print("\n" + "="*70)
print("SECTION 4: GENERATING COMPLETE REPORT")
print("="*70)

baseline_yield = best_model.model.predict(scaler.transform(X.mean().values.reshape(1, -1)))[0]
improvement = ((de_yield - baseline_yield) / baseline_yield) * 100

with open('results/reports/complete_project_report.txt', 'w') as f:
    f.write("="*70 + "\n")
    f.write("COMPLETE COMPLEX BIOFUEL OPTIMIZATION SYSTEM\n")
    f.write("Final Project Report\n")
    f.write("="*70 + "\n\n")
    f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("1. DATASET INFORMATION\n")
    f.write("-"*50 + "\n")
    f.write(f"   Total Samples: {df.shape[0]}\n")
    f.write(f"   Features: {len(features)}\n")
    f.write(f"   Parameters: {', '.join(features)}\n\n")
    
    f.write("2. MODEL PERFORMANCE\n")
    f.write("-"*50 + "\n")
    f.write(f"   Random Forest R²: {rf_metrics['R2']:.4f}\n")
    f.write(f"   Random Forest MAE: {rf_metrics['MAE']:.2f} g/L\n")
    f.write(f"   XGBoost R²: {xgb_metrics['R2']:.4f}\n")
    f.write(f"   XGBoost MAE: {xgb_metrics['MAE']:.2f} g/L\n")
    f.write(f"   Best Model: {best_model_name}\n\n")
    
    f.write("3. FEATURE IMPORTANCE\n")
    f.write("-"*50 + "\n")
    for name, imp in sorted(zip(features, importance), key=lambda x: x[1], reverse=True):
        f.write(f"   {name}: {imp*100:.1f}%\n")
    f.write("\n")
    
    f.write("4. OPTIMIZATION RESULTS\n")
    f.write("-"*50 + "\n")
    f.write(f"   Differential Evolution Yield: {de_yield:.2f} g/L\n")
    f.write(f"   Genetic Algorithm Yield: {ga_yield:.2f} g/L\n")
    f.write(f"   Particle Swarm Yield: {pso_yield:.2f} g/L\n")
    f.write(f"   Best Algorithm: {best_algo}\n\n")
    
    f.write("5. OPTIMAL PARAMETERS (Best from Differential Evolution)\n")
    f.write("-"*50 + "\n")
    for name, val in zip(features, de_params):
        f.write(f"   {name}: {val:.2f}\n")
    f.write(f"\n   Maximum Yield: {de_yield:.2f} g/L\n")
    f.write(f"   Baseline Yield: {baseline_yield:.2f} g/L\n")
    f.write(f"   Improvement: {improvement:.1f}%\n\n")
    
    f.write("6. SUSTAINABILITY IMPACT\n")
    f.write("-"*50 + "\n")
    f.write("   SDG 7: Affordable and Clean Energy\n")
    f.write("   SDG 9: Industry, Innovation and Infrastructure\n")
    f.write("   SDG 12: Responsible Consumption and Production\n")
    f.write("   SDG 13: Climate Action\n")

print("✅ Complete report saved: results/reports/complete_project_report.txt")

# ============================================
# FINAL SUMMARY
# ============================================

print("\n" + "="*70)
print("✅ PROJECT COMPLETED SUCCESSFULLY!")
print("="*70)
print(f"\n📊 SUMMARY:")
print(f"   • Dataset: {df.shape[0]} samples")
print(f"   • Best Model: {best_model_name} (R² = {max(rf_metrics['R2'], xgb_metrics['R2']):.4f})")
print(f"   • Best Optimization: {best_algo} ({yields[best_algo]:.2f} g/L)")
print(f"   • Improvement: {improvement:.1f}% over baseline")
print(f"\n📁 OUTPUT FILES:")
print(f"   • Data: data/raw/biofuel_raw.csv")
print(f"   • Models: models/random_forest.pkl")
print(f"   • Graph: results/figures/feature_importance.png")
print(f"   • Report: results/reports/complete_project_report.txt")
print(f"   • Logs: results/logs/experiment.log")
print("\n" + "="*70)