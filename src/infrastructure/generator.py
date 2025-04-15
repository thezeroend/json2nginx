import os
from typing import List, Dict
from domain.directives import Directives

def generate_location_blocks(routes: List[Dict]):
    """
    Gera os blocos de configuração do Nginx a partir das rotas fornecidas.

    Args:
        routes (List[Dict]): Lista de dicionários contendo as informações das rotas.
    """
    routes = routes["routes"]
    for route in routes:
        # Define o nome do arquivo de configuração com base no caminho da rota
        route_path = route.get("path", "").replace("/", "_").strip("_")
        config_filename = f"{route_path}_nginx.conf"

        # Gera o conteúdo do arquivo de configuração
        config_content = generate_config_content(route)

        return config_content

        # # Salva o arquivo de configuração no diretório de saída
        # config_path = os.path.join(output_dir, config_filename)
        # with open(config_path, 'w') as config_file:
        #     config_file.write(config_content)
        #     print(f"Configuração gerada para {route.get('path')}: {config_path}")

def generate_config_content(route: Dict) -> str:
    modifier = route.get("modifier", "")
    path = route["path"]

    location_block = f"location {modifier + ' ' if modifier else ''}{path} {{\n"
    
    for directive, value in route.items():
        if directive in Directives.RESERVED_KEYS:
            continue
        
        if directive not in Directives.ALLOWED_DIRECTIVES:
            raise ValueError(f"Diretiva '{directive}' não permitida na configuração do Nginx.")
        
        # Gerando o conteúdo do arquivo com base nas diretivas permitidas
        if isinstance(value, list):
            for item in value:
                location_block += f"    {directive} {item};\n"
        else:
            location_block += f"    {directive} {value};\n"
    
    location_block += "}\n"
    
    return location_block
