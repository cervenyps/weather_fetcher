# Weather Fetcher

**Weather Fetcher** é um pacote Python simples para obter a temperatura atual em várias cidades (Nova York, Vancouver, Londres, Tóquio e Amsterdã) usando o serviço `wttr.in`.
## Instalação

Você pode instalar o pacote diretamente do PyPI usando o pip:

```bash
pip install weather_fetcher
```

## Como utilizar
```phyton
from weather_fetcher.temperature import get_temperatures

temperaturas = get_temperatures()
print(temperaturas)
```

Que irá retornar um dicionário com as temperaturas atuais das cidades.

