# Conversor .ofx > .xls

## O que é?

Script desenvolvido pelo departamento de TI ([@jpricardo](https://www.github.com/jpricardo)) a fim de facilitar a conversão de relatórios bancários (exportados no formato _.ofx_) para o formato _.xlsx_, facilitando assim o lançamento no sistema.

## Como utilizar?

### Usuário comum

- Acesse a url do aplicativo em seu navegador.
- Na página inicial, selecione um arquivo .ofx ou .txt, formatado. corretamente.
- Clique em "Converter".
- Aguarde o download de seu arquivo .xls.
- **Pronto!**

### Desenvolvedor

- Instale o _Python 3.10.3_.
- Clone esse repositório (ou baixe o _.zip_).
- Navegue até a pasta com os arquivos.
- Instale as dependências com `pip install -r requirements.txt`.
- Navegue até a pasta `/website`.
- Construa o banco de dados utilizando `python manage.py migrate`
- A página de administrador fica disponível em `<IP>:<PORT>/admin`. Para criar um novo usuário administrador, utilize `python manage.py createsuperuser` e siga as instruções.
- Para rodar o servidor em modo de desenvolvimento, utilize `python manage.py runserver 0.0.0.0:<PORT>`.

## Como funciona?

A conversão e geração da do arquivo .xls são realizados utilizando as bibliotecas _ofparse_ e _xlsxwriter_. Tanto os arquivos enviados quanto os resultantes do processamento ficam salvos no servidor.

## Não funcionou, e agora??

- Abra um chamado para o TI

_Obrigado, e ótimos ventos!_
