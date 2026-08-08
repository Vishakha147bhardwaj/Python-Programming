import os
def load_or_create_config(config_path):
    default_settings = "theme=dark\nthreads=4\ncache=true\n"

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            print("Configuration found. Loading settings...")
            return file.read()

    except FileNotFoundError:
        print(f"Warning: '{config_path}' not found. Generating defaults...")
        try:
            with open(config_path, "w", encoding="utf-8") as file:
                file.write(default_settings)
            return default_settings
        except PermissionError:
            print("Critical Error: Write permissions denied on directory.")
            raise


config_data = load_or_create_config("settings.txt")
print(config_data)