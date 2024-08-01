import json
import os
from typing import Dict, Any

class JSONStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: Dict[str, Dict[str, Any]] = self._load_data()

    def _load_data(self) -> Dict[str, Dict[str, Any]]:
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def _save_data(self) -> None:
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def save(self, collection: str, key: str, value: Any) -> None:
        if collection not in self.data:
            self.data[collection] = {}
        self.data[collection][key] = value
        self._save_data()

    def load(self, collection: str, key: str) -> Any:
        return self.data.get(collection, {}).get(key)

    # def delete(self, collection: str, key: str) -> None:
    #     if collection in self.data and key in self.data[collection]:
    #         del self.data[collection][key]
    #         self._save_data()

    # def load_all(self, collection: str) -> Dict[str, Any]:
    #     return self.data.get(collection, {})