global_monitoring_config = {
    "data_collection_interval": 60,
    "cpu_threshold": 80, 
    "memory_threshold": 70,
    "logging_level": "INFO"
}
global_user_settings = {
    "theme_color": "light",
    "font_size": "medium"
}
def print_variable_address(name, var):
    """
    Print the memory address of a variable using Python's built-in id() function.
    """
    print(f"{name} address: {id(var)}")

def resolve_config(global_config, local_config):
    """
    Merge global configuration with local overrides and return the final configuration.
    """
    config = global_config.copy()
    config.update(local_config)
    return config

def demonstrate_scope_and_visibility():
    print("Global Monitoring Configuration:", global_monitoring_config)
    print_variable_address("global_monitoring_config", global_monitoring_config)

    print("Global User Settings:", global_user_settings)
    print_variable_address("global_user_settings", global_user_settings)

    service1_config = {
        "data_collection_interval": 30,
        "logging_level": "DEBUG"
    }
    service1_final = resolve_config(global_monitoring_config, service1_config)
    print("Service 1 Config:", service1_final)
    print_variable_address("service1_final", service1_final)

    service2_config = {
        "cpu_threshold": 90,
        "memory_threshold": 80,
        "logging_level": "WARNING"
    }
    service2_final = resolve_config(global_monitoring_config, service2_config)
    print("Service 2 Config:", service2_final)
    print_variable_address("service2_final", service2_final)

    service3_final = resolve_config(global_monitoring_config, {})
    print("Service 3 Config:", service3_final)
    print_variable_address("service3_final", service3_final)

    user1_settings = {
        "theme_color": "dark",
        "font_size": "large"
    }
    user1_final = resolve_config(global_user_settings, user1_settings)
    print("User 1 Settings:", user1_final)
    print_variable_address("user1_final", user1_final)

    user2_final = resolve_config(global_user_settings, {})
    print("User 2 Settings:", user2_final)
    print_variable_address("user2_final", user2_final)

if __name__ == "__main__":
    demonstrate_scope_and_visibility()