# src/infrastructure/reader.py

import json
import os

def load_json_configs(configs_dir):
    """
    Lê todos os arquivos JSON no diretório especificado e os retorna como um dicionário.
    """
    configs_por_arquivo = {}

    for filename in os.listdir(configs_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(configs_dir, filename)
            try:
                with open(filepath) as f:
                    configs_por_arquivo[filename] = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Erro ao ler {filename}: {e}")
    
    return configs_por_arquivo
