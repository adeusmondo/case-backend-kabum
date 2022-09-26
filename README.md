# case-backend-kabum
 
Este projeto consiste em uma API de cálculo de frete.
 
## Como rodar o projeto
 
### Virtual Env
 
Para executar o projeto localmente, você precisa:
 
- [Python](https://www.python.org/downloads/) 3.7 ou maior
- [Poetry](https://python-poetry.org/)
 
Após instalar estas duas ferramentas e clonar o projeto, vá para a pasta do projeto e execute o seguinte comando:
 
```bash
poetry shell
poetry install
```
 
Esse comando acima irá criar a nossa virtual env e instalar as dependências necessárias para que o projeto seja executado.
 
Agora ainda na pasta do projeto podemos executar a aplicação da seguinte maneira:
 
```bash
python src/main.py
```
 
E assim nossa aplicação já estará de pé.
 
### Utilizando containers
 
Se você preferir rodar a app em containers, você só precisará da cli e do daemon do [docker](https://www.docker.com/). Após instalado, você pode executar o comando presente no Makefile, que irá fazer a build, executar o container e mostrar seus logs:
 
```bash
make docker-stuffs
```
 
Ou se preferir fazer manualmente os comandos:
 
```bash
docker build -t kabum-shipping:latest .
docker run --name kabum-shipping-api -p 8000:8000 -d kabum-shipping
docker logs -f kabum-shipping-api
```

## Como chamar o projeto

Após estar com o projeto rodando, você pode utilizar uma ferramenta como o cURL para fazer chamadas para as APIs, segue alguns exemplos.

### Listagem das opções de frete

```bash
curl --request GET http://0.0.0.0:8000/v1/shipping-options
```

### Calcular frete

```bash
curl --request POST http://0.0.0.0:8000/v1/calculate-shipping \
   -H 'Content-Type: application/json' \
   -d '{"dimensao":{"altura":102,"largura":40},"peso":400}'
```

```bash
curl --request POST http://0.0.0.0:8000/v1/calculate-shipping \
   -H 'Content-Type: application/json' \
   -d '{"dimensao":{"altura":152,"largura":50},"peso":850}'
```

```bash
curl --request POST http://0.0.0.0:8000/v1/calculate-shipping \
   -H 'Content-Type: application/json' \
   -d '{"dimensao":{"altura":230,"largura":162},"peso":5600}'
```

### Documentação

Você pode acessar toda a documentação do projeto através do endpoint `/docs` ou a documentação alternativa `/redoc`, desde que o projeto esteja rodando. Através da documentação você pode tambem realizar chamadas de API para os endpoints, assim como visualizar os schemas de input e output.

## Testes
 
No projeto possui uma pasta de `testes`, onde estão os testes e2e do projeto para cada endpoint, caso você deseja roda-los pode executar o comando presente no Makefile ou rodar no seu terminal o comando do pytest:
 
```bash
make test
# OU
pytest -vv --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=75
```
