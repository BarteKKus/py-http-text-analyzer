import json
from pathlib import Path
from typing import Dict


def load_json_file(filepath: Path) -> Dict:
    """Load json file

    Args:
        filepath (Path): path with filename to load

    Raises:
        FileNotFoundError: if file was not found
        ValueError: on any decoding errors

    Returns:
        Dict: json file as dictionary
    """
    try:
        with filepath.open() as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON file '{filepath}': {e}")
