import logging
import os

def get_aws_region_from_env():
    """Returns the AWS region from the AWS_REGION environment variable."""
    return os.environ.get('AWS_REGION')

def get_log_level_from_env():
    """Returns the log level from the LOG_LEVEL environment variable."""
    log_level = os.environ.get('LOG_LEVEL')
    if log_level is None:
        return logging.INFO
    else:
        return getattr(logging, log_level.upper())

def get_aws_credentials_file_path():
    """Returns the path to the AWS credentials file."""
    return os.path.expanduser('~/.aws/credentials')

def get_infra_terraform_config_file_path():
    """Returns the path to the infra-terraform configuration file."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.tf')