import configparser


def read_file_path_config(path) -> str | None:
    """讀取路徑"""
    config = configparser.ConfigParser()
    config.read(f"{path}/config.ini", encoding='utf-8')
    path_config = config.get("path", "log_path")xx
