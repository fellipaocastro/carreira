# carreira

![build status](https://github.com/fellipaocastro/carreira/actions/workflows/code_analysis.yml/badge.svg)(https://github.com/fellipaocastro/carreira/actions)

![carreira](https://raw.githubusercontent.com/fellipaocastro/carreira/main/carreira/carreira.png)

## tempo trabalhado em cada empresa/órgão

### setup recomendado

```bash
pyenv virtualenv 3.12.3 carreira
```
```bash
pip install -r requirements/local.txt
```
```bash
python -m carreira
```

### testes automatizados

```bash
pytest -vv --diff-symbols --cov carreira
```

### análise estática de código

```bash
pylint carreira
```

### análise de convenções de estilo

```bash
pycodestyle carreira
```