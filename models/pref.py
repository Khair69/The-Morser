from pathlib import Path
import sys

def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "../data/assets"
    return Path(__file__).parent / "../data/assets"

def relative_to_assets(ASSETS_PATH,path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_base_path_json():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "../data/custom_sets"
    return Path(__file__).parent / "../data/custom_sets"