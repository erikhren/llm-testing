import csv
import json
from typing import Any, Dict, List


def load_json(path) -> List[Dict[str, Any]]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_results(results: List[Dict[str, Any]], path='results.csv'):
    keys = results[0].keys()
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)