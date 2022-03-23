# Conversor .ofx > .xlsx

## O que é?

Script desenvolvido pelo departamento de TI ([@jpricardo](https://www.github.com/jpricardo)) a fim de facilitar a conversão de relatórios bancários (exportados no formato *.ofx*) para o formato *.xlsx*, facilitando assim o lançamento no sistema.

## Como instalar?

### Usuário comum

- Caso não esteja confortável em fazer a instalação por conta própria, **COMUNIQUE AO TI**
- Procure, em sua pasta TEMP (`C:\TEMP`), a pasta `CONVERSOR OFX`
- Copie a pasta para sua área de trabalho
- **PRONTO!**

### Desenvolvedor

- Instale o *Python 3.10.3*
- Clone esse repositório (ou baixe o *.zip*)
- Pelo terminal, navegue até a pasta `src/`, com `cd src`
- Para gerar um executável, instale o `pyinstaller` e utilize o comando `pyinstaller main.py --onefile`
- Retire o executável de dentro da pasta `dist/` e deixe junto do arquivo `main.py`, em `src/`
- Para distribuir a atualização, substitua o executável na máquina remota

## Como funciona?

- Insira os arquivos *.ofx* dentro da pasta `entrada/`
- Rode o arquivo `src/main.exe`, pelo atalho `converter`
- Verifique a pasta `saída/`
- **PRONTO**

## Não funcionou, e agora??

- Abra um chamado para o TI

*Obrigado, e ótimos ventos!*
