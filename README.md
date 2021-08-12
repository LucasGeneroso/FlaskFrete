# **FlaskFrete**
API FLask desenvolvida para o teste da vaga de backend da KaBuM!

## Como usar
Você deve baixar ou clonar o projeto deste repositório (FlaskFrete)

Após baixar o projeto, será necessário criar um ambiente virtual **(venv)**, para isso execute o seguite comando na pasta que baixou o projeto:
```
python -m venv venv (nome do ambiente virtual)
```
Após vamos ativar-lá:

**Para sistema operacional linux**:
```
cd venv (nome do seu ambiente virtual criado)
source bin/activate
```
**Para sistemas windows**
```
cd Scripts
activate
```
Com o ambiente virtual instalado e aberto, vamos instalar os pacotes (estão no arquivo **requirements.txt**)

Na pasta em que o arquivo se encontra, execute o seguinte comando para dar inicio:
```
pip install -r requirements.txt
```
**Aguarde a instalação de todos os pacotes**

Após isso, vamos executar o projeto para que a API funcione. Rode o seguinte comando na pasta raiz do projeto:
```
python app.py
```

Se tudo correr bem, os seguintes log's apareceram no seu terminal:

![image](https://user-images.githubusercontent.com/36650872/129263823-e3de0266-481d-4a9f-9702-d44243a481b4.png)

bom, com tudo funcionando vamos para os testes.

## Testando a API

O teste pode ser feito a partir do **Swagger** onde se encontram todos os endpoints disponíveis da API.

### Swagger
Para testar a API e suas funcionalidades pelo Swagger é necessário apenas acessar a rota **http://localhost:5000/api/doc** em seu navegador (com o projeto já rodando, vide passo anterior).

**Você irá ver a seguinte tela**:

![image](https://user-images.githubusercontent.com/36650872/129263903-6743d420-a457-4a9a-9dfa-8391dc2e8f4a.png)

Para iniciar os testes, é preciso criar as transporadoras com as informações que você deseja em  **POST /shippings**
Você também pode ver todas as transportadoras já criadas em **GET /shippings**
Assim como também pode consultar ou deletar uma especifica que deseja em **GET /shippings/<id>** e **DELETE /shippings/<id>**

**Após as transporadoras estarem configuradas, podemos partir para o calculo do frete, na rota: POST /freight**

Será necessário enviar um paylaod contendo as informações do pacote que deseja enviar, neste formato:
```
{
   "dimension":{
      "heigth":102,
      "width":40
   },
   "weight":400
}
```
e então o retorno será das transportadoras cadastradas que estão elegiveis para realizar a entrega. Caso nenhuma se encaixe, o resto será uma lista vázia.
  
**Caso fique em duvida em algum payload que necessite enviar na API, os modelos estão disponives logo abaixo das requisições**
