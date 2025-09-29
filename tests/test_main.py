#!/usr/bin/env python3
"""
Tests for the AI Test Project main application.
"""

import os
import pytest
import sys
from unittest.mock import patch

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import AITestApp


class TestAITestApp:
    """Test cases for AITestApp."""
    
    def test_init_default_values(self):
        """Test initialization with default values."""
        app = AITestApp()
        assert app.env == 'DEV'
        assert app.jira_ticket == 'UNKNOWN'
        assert app.ai_agent_id == 'test-agent'
    
    @patch.dict(os.environ, {
        'ENV': 'INTEGRATION',
        'JIRA_TICKET': 'PROJ-123',
        'AI_AGENT_ID': 'ai-agent-001'
    })
    def test_init_with_env_vars(self):
        """Test initialization with environment variables."""
        app = AITestApp()
        assert app.env == 'INTEGRATION'
        assert app.jira_ticket == 'PROJ-123'
        assert app.ai_agent_id == 'ai-agent-001'
    
    def test_get_config_dev(self):
        """Test configuration for DEV environment."""
        app = AITestApp()
        app.env = 'DEV'
        config = app.get_config()
        
        assert config['environment'] == 'DEV'
        assert config['debug'] is True
        assert config['database_url'] == 'sqlite:///dev.db'
        assert config['log_level'] == 'DEBUG'
    
    def test_get_config_integration(self):
        """Test configuration for INTEGRATION environment."""
        app = AITestApp()
        app.env = 'INTEGRATION'
        config = app.get_config()
        
        assert config['environment'] == 'INTEGRATION'
        assert config['debug'] is False
        assert config['database_url'] == 'postgresql://localhost/integration_db'
        assert config['log_level'] == 'INFO'
    
    def test_get_config_staging(self):
        """Test configuration for STAGING environment."""
        app = AITestApp()
        app.env = 'STAGING'
        config = app.get_config()
        
        assert config['environment'] == 'STAGING'
        assert config['debug'] is False
        assert config['database_url'] == 'postgresql://staging-db/app_db'
        assert config['log_level'] == 'WARNING'
    
    def test_get_config_prod(self):
        """Test configuration for PROD environment."""
        app = AITestApp()
        app.env = 'PROD'
        config = app.get_config()
        
        assert config['environment'] == 'PROD'
        assert config['debug'] is False
        assert config['database_url'] == 'postgresql://prod-db/app_db'
        assert config['log_level'] == 'ERROR'
    
    def test_run_returns_zero(self):
        """Test that run method returns 0 for success."""
        app = AITestApp()
        result = app.run()
        assert result == 0
    
    def test_process_data_no_exception(self):
        """Test that process_data runs without exception."""
        app = AITestApp()
        # Should not raise any exception
        app.process_data()


if __name__ == '__main__':
    pytest.main([__file__])
