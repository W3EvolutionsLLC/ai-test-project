#!/usr/bin/env python3
"""
AI Test Project - Main Application

This is a sample application for testing the AI development automation system.
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, Any


class AITestApp:
    """Sample application for AI development automation testing."""
    
    def __init__(self):
        self.env = os.getenv('ENV', 'DEV')
        self.jira_ticket = os.getenv('JIRA_TICKET', 'UNKNOWN')
        self.ai_agent_id = os.getenv('AI_AGENT_ID', 'test-agent')
        
    def get_config(self) -> Dict[str, Any]:
        """Get application configuration based on environment."""
        config = {
            'environment': self.env,
            'jira_ticket': self.jira_ticket,
            'ai_agent_id': self.ai_agent_id,
            'timestamp': datetime.now().isoformat(),
            'version': '1.0.0'
        }
        
        # Environment-specific configuration
        if self.env == 'DEV':
            config.update({
                'debug': True,
                'database_url': 'sqlite:///dev.db',
                'log_level': 'DEBUG'
            })
        elif self.env == 'INTEGRATION':
            config.update({
                'debug': False,
                'database_url': 'postgresql://localhost/integration_db',
                'log_level': 'INFO'
            })
        elif self.env == 'STAGING':
            config.update({
                'debug': False,
                'database_url': 'postgresql://staging-db/app_db',
                'log_level': 'WARNING'
            })
        elif self.env == 'PROD':
            config.update({
                'debug': False,
                'database_url': 'postgresql://prod-db/app_db',
                'log_level': 'ERROR'
            })
            
        return config
    
    def run(self):
        """Run the application."""
        config = self.get_config()
        
        print(f"AI Test Application Starting...")
        print(f"Environment: {config['environment']}")
        print(f"Jira Ticket: {config['jira_ticket']}")
        print(f"AI Agent: {config['ai_agent_id']}")
        print(f"Timestamp: {config['timestamp']}")
        print(f"Configuration: {json.dumps(config, indent=2)}")
        
        # Simulate some work
        self.process_data()
        
        print("Application completed successfully!")
        return 0
    
    def process_data(self):
        """Simulate data processing."""
        print("Processing data...")
        
        # Simulate different behavior based on environment
        if self.env == 'DEV':
            print("Running in development mode - using sample data")
        elif self.env == 'INTEGRATION':
            print("Running integration tests")
        elif self.env == 'STAGING':
            print("Running staging validation")
        elif self.env == 'PROD':
            print("Running production workload")
        
        print("Data processing complete")


def main():
    """Main entry point."""
    app = AITestApp()
    return app.run()


if __name__ == '__main__':
    sys.exit(main())
