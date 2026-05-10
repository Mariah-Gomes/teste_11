# Relatório — Lab 11: Pipeline CI

## Objetivo

Configurar um pipeline de CI com GitHub Actions para validar automaticamente lint, testes e cobertura mínima.

## Etapa 1 — Pipeline inicial

Foi criado o arquivo:

```text
.github/workflows/ci.yml

O pipeline contém:

trigger em push e pull_request para main;
setup do Python 3.11;
instalação via requirements.txt;
lint com flake8;
testes com pytest;
cobertura mínima de 80%;
publicação do relatório de cobertura como artefato.
Etapa 2 — Pipeline vermelho

Na primeira execução, o pipeline falhou porque a cobertura estava abaixo de 80%.

Também foi identificado erro de lint por import não utilizado.

Etapa 3 — Correção

Foram adicionados testes para as funções que ainda não estavam cobertas:

dividir
dividir com divisão por zero
eh_par
potencia

Após isso, a cobertura passou para 100%.

Comandos usados localmente
python -m flake8 . --max-line-length=100
python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=80
Resultado final

O pipeline passou com sucesso, validando:

lint;
testes automatizados;
cobertura mínima exigida;
relatório de cobertura publicado como artefato.

Depois commita junto:

```powershell
git add relatorio.md
git commit -m "docs: adicionar relatorio do pipeline"
git push origin pipeline