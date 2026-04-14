"""
XGBoost Model with Hyperparameter Optimization
"""

import xgboost as xgb
import numpy as np
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error
import optuna
import joblib
import logging

logger = logging.getLogger(__name__)

class OptimizedXGBoost:
    """XGBoost Regressor with advanced tuning"""
    
    def __init__(self, config):
        self.config = config
        self.model = None
        self.best_params = None
    
    def optuna_tune(self, X_train, y_train, n_trials=100):
        """Bayesian optimization with Optuna"""
        
        def objective(trial):
            params = {
                'n_estimators': trial.suggest_int('n_estimators', 100, 500),
                'max_depth': trial.suggest_int('max_depth', 3, 10),
                'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3),
                'subsample': trial.suggest_float('subsample', 0.6, 1.0),
                'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
                'reg_alpha': trial.suggest_float('reg_alpha', 0, 2),
                'reg_lambda': trial.suggest_float('reg_lambda', 0, 2)
            }
            
            model = xgb.XGBRegressor(**params, random_state=42, n_jobs=-1)
            scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
            return scores.mean()
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=n_trials)
        
        self.best_params = study.best_params
        logger.info(f"Best XGBoost parameters: {self.best_params}")
        logger.info(f"Best CV score: {study.best_value:.4f}")
        
        return self.best_params
    
    def train(self, X_train, y_train, params=None):
        """Train XGBoost model"""
        
        if params is None:
            params = self.best_params or {}
        
        self.model = xgb.XGBRegressor(
            **params,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)
        return self
    
    def evaluate(self, X_test, y_test):
        """Evaluate model"""
        y_pred = self.model.predict(X_test)
        return {
            'R2': r2_score(y_test, y_pred),
            'MAE': mean_absolute_error(y_test, y_pred)
        }
    
    def get_feature_importance(self, feature_names):
        """Get feature importance"""
        importance = self.model.feature_importances_
        return sorted(zip(feature_names, importance), key=lambda x: x[1], reverse=True)
    
    def save(self, path):
        joblib.dump(self.model, path)