import os
import unittest
import subprocess


class DockerTestCase(unittest.TestCase):
    """Tests for Docker configuration (skipped in normal test runs)"""

    @unittest.skipIf(os.environ.get('SKIP_DOCKER_TESTS', 'True') == 'True',
                     "Docker tests are skipped by default. Set SKIP_DOCKER_TESTS=False to run.")
    def test_docker_build(self):
        """Test that Docker image builds successfully"""
        result = subprocess.run(['docker', 'build', '-t', 'static-django-test', '.'],
                                cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Docker build failed: {result.stderr}")
        
    @unittest.skipIf(os.environ.get('SKIP_DOCKER_TESTS', 'True') == 'True',
                     "Docker tests are skipped by default. Set SKIP_DOCKER_TESTS=False to run.")
    def test_docker_compose(self):
        """Test that docker-compose file is valid"""
        result = subprocess.run(['docker-compose', 'config'],
                                cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Docker compose validation failed: {result.stderr}")
