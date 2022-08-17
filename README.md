# Catalogador-sinais-IQ-Option

Este projeto foi desenvolvido em Python para efetuar a catalogação percentual do tipo de velas para IQOPTION de acordo com um timeframe específico. Utiliza API não ofical para estabelecer conexão com a IQ OPTION.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

```
=> Pyton 3.7 ou superior instalado;
=> Instalar as dependências necessárias "requeriments.txt": pip install -r /path/to/requirements.txt.
```

### 🔧 Pré-configurações

Utilize o arquivo "config.txt" para efetuar inserir os parâmetros necessários para a catalogação.

### ⚙️ Executando o programa

Navegue até a pasta onde se encontra o codigo via CMD e execute o código abaixo 

```
python main.py
 
```

### 📨 Distribuição

É possivel efetuar a distribuição para usuários que não possuem pyton instalados em suas máquinas através da biblioteca pyinstaller. 

```
pip install pyinstaller 

```

Navegar até a pasta onde se enocntra via cmd e executar código abaixo para criar o arquivo de especificação 

```
pyi-makespec main.py --onefile  --name iqoption-catalogador-exe

```

A compilação poderá ser fetuada conforme código abaixo

```
pyinstaller --clean iqoption-catalogador-exe.spec

```

## 📦 Desenvolvimento

Lauro Cerqueira

LinkdIn: https://www.linkedin.com/in/lauro-cerqueira-70473568/

Instagram : laurorcerqueira

## 🛠️ Construído com

* [Lu-Yi-Hsun Unofficial IQOPTION API](https://github.com/Lu-Yi-Hsun/iqoptionapi)
* [Python 3.8](https://www.python.org/downloads/release/python-380/)

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Agradecimentos

* Conte a outras pessoas sobre este projeto 📢
* Convide alguém da equipe para uma cerveja 🍺 
* Obrigado publicamente 🤓.


