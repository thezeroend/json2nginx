class Directives:
    """Classe que contém as diretivas permitidas e chaves reservadas para configuração do Nginx."""
    
    # Diretivas permitidas para o Nginx
    ALLOWED_DIRECTIVES = [
        "proxy_pass",
        "proxy_set_header",
        "rewrite",
        "add_header",
        "auth_basic",
        "auth_basic_user_file",
        "allow",
        "deny",
        "location",
        "return",
        "limit_except"
    ]
    
    # Chaves reservadas que não devem ser usadas diretamente nas rotas
    RESERVED_KEYS = [
        "path",
        "modifier",
    ]
