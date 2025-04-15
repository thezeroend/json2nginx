# json2nginx

Gere arquivos de configuração de rotas Nginx a partir de arquivos JSON de forma simples, rápida e validada.

---

## 📦 Visão Geral

Este projeto converte arquivos `.json` contendo configurações de rotas em arquivos `.conf` para uso com o Nginx. Cada arquivo JSON pode conter múltiplas rotas, e cada rota é convertida em um bloco `location`.

⚠️ O projeto **não oferece suporte a diretivas de arquivos estáticos** como `root`, `alias` ou similares.

---

## 🧠 Motivação

Facilitar a manutenção de configurações complexas de rotas Nginx em ambientes que exigem automação, versionamento e validação robusta de diretivas.

---

## 🛠️ Como Usar

### Pré-requisitos

- Python 3.8+
- (opcional) `pip install -r requirements.txt`

### Executando

```bash
python src/main.py --configs-dir <pasta_dos_json> --output-dir <pasta_de_saida>
```

- --configs-dir: Caminho para a pasta contendo os arquivos .json de configuração.
- --output-dir: Caminho para a pasta onde os arquivos .conf serão salvos.

---
## ✅ Regras e Validações
- Os arquivos JSON devem conter uma chave routes, que mapeia para uma lista de objetos.
- Cada rota deve conter obrigatoriamente a chave path.
- Todas as diretivas usadas devem estar dentro do conjunto de diretivas permitidas.
- Diretivas não suportadas causam erro de validação com a lista completa de diretivas inválidas.

Exemplo de JSON Válido

```json
{
  "routes": [
    {
      "path": "/api/v1/",
      "proxy_pass": "http://backend1.local",
      "proxy_set_header": [
        "X-Forwarded-For $remote_addr",
        "X-Forwarded-Proto $scheme"
      ]
    },
    {
      "path": "/api/v2/",
      "proxy_pass": "http://backend2.local"
    }
  ]
}
```

## 📌 Observações
Cada arquivo JSON gera um arquivo .conf separado com o nome baseado na rota (/api/v1/ → api_v1.conf).

A configuração Nginx gerada não inclui blocos server, listen, nem server_name.

##🤝 Contribuições
Sinta-se à vontade para abrir issues, enviar PRs ou sugerir melhorias!
