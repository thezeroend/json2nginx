from collections import defaultdict
from domain.directives import Directives

def validate_routes(configs_por_arquivo):
    """
    Valida as rotas nos arquivos JSON para garantir que todas as diretivas
    sejam permitidas e não haja diretivas inválidas.
    """
    erros = defaultdict(list)

    for filename, config_data in configs_por_arquivo.items():
        routes = config_data.get("routes", [])
        for route in routes:
            path = route.get("path", "<sem path>")
            for key in route:
                if key not in Directives.RESERVED_KEYS and key not in Directives.ALLOWED_DIRECTIVES:
                    erros[filename].append((path, key))
    
    if erros:
        raise ValueError("Diretivas inválidas encontradas:\n" + format_validation_error(erros))


def format_validation_error(erros):
    """
    Formata os erros de validação para uma saída legível.
    """
    error_message = ""
    for arquivo, problemas in erros.items():
        error_message += f"Arquivo: {arquivo}\n"
        for path, diretiva in problemas:
            error_message += f"  - Rota '{path}': diretiva inválida -> '{diretiva}'\n"
        error_message += "\n"
    error_message += f"Diretivas permitidas: {', '.join(sorted(Directives.ALLOWED_DIRECTIVES))}"
    return error_message
