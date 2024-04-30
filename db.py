import os
import yaml
import redis

def load_config():
    """Load configuration from the YAML file."""
    try:
        config_file_path = os.path.join('Final', 'config.yaml')
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file not found: {config_file_path}")
        with open(config_file_path, "r") as file:
            config = yaml.safe_load(file)
            if config is None:
                raise yaml.YAMLError("No data found in the YAML file.")
            print("Loaded config:", config)
            return config
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

def get_redis_connection():
    """Create a Redis connection using the configuration."""
    config = load_config()
    if config is None:
        return None
    conn = redis.Redis(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=config["redis"]["db"],
        decode_responses=True,
        username=config["redis"]["user"],
        password=config["redis"]["password"],
    )
    print("Redis connection:", conn)
    return conn