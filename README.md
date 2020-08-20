# predict_api

Primeiramente supondo que o usuário já tenha o python instalado em sua máquina e/ou a IDE PyCharm, os passos a seguir irão auxiliar 
o usuário a fazer o clone do repositório e tê-lo em sua máquina para testar.

Para ter acesso em sua máquina da api, o usuário deve clonar este repositório com o seguinte comando:
`git clone https://github.com/Giovannisb/predict_api.git`

Em seguida, vá para pasta em sua máquina que foi feita a clonagem dos arquivos deste repositório.

## CMD/linha de comando
Para executar o código da api, basta acessar a pasta api_predict
`cd api_predict`
Estando dentro da pasta com os arquivos, procuramos o arquivo chamado `app.py`. Este arquivo é responsável pelo servidor da aplicação.
Encontrando esse arquivo, iremos roda-lo com o seguinte comando: `python app.py`.
Pronto, a aplicação estará rodando e basta acessar no navegador a seguinte url: `127.0.0.1:5000/`

## IDE/PyCharm
Para executar a api dentro da IDE, basta abrir a pasta que foi clonada do repositório. Após esse processo, basta rodar o arquivo `app.py`
e a aplicação já estará rodando.

## Observações
A API classifica apenas imagens de gatos e cachorros, não classificando outros animais, objetos, etc.
