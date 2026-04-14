"""
Advanced Logging System
"""

import logging
import os
from datetime import datetime

def setup_logger(log_file='logs/experiment.log'):
    """Setup professional logging"""
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized at {datetime.now()}")
    
    return logger

class ExperimentLogger:
    """Class for tracking experiments"""
    
    def __init__(self, experiment_name):
        self.experiment_name = experiment_name
        self.start_time = datetime.now()
        self.metrics = {}
        
    def log_metric(self, name, value):
        self.metrics[name] = value
        print(f"📊 {name}: {value}")
    
    def log_params(self, params):
        for key, value in params.items():
            print(f"⚙️ {key}: {value}")
    
    def save_results(self, filepath):
        import json
        results = {
            'experiment_name': self.experiment_name,
            'start_time': str(self.start_time),
            'end_time': str(datetime.now()),
            'metrics': self.metrics
        }
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"✅ Results saved to {filepath}")