# EP 5 - GitHub Actions

Projeto simples em Python para demonstrar testes automatizados com GitHub Actions.

## O que o projeto faz

O pacote `ep5_actions` implementa pequenas funcoes para calcular estatisticas de uma lista de numeros:

- media
- mediana
- amplitude
- normalizacao min-max

## Como rodar localmente

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## GitHub Actions

O workflow em `.github/workflows/tests.yml` roda os testes automaticamente a cada `push` e `pull_request`.

A matriz de execucao usa:

- Sistemas operacionais: Ubuntu, macOS e Windows
- Versoes do Python: 3.11 e 3.12

Isso gera 6 combinacoes de teste no GitHub Actions.
