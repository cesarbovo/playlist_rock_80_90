
# Playlist de Rock Nacional

Aplicação em console desenvolvida em Python que simula um **player de músicas** utilizando o conceito de **lista duplamente ligada**.  
O sistema permite navegar entre as faixas, adicionar, remover, salvar e carregar músicas de uma playlist, representando fielmente o funcionamento básico de um reprodutor de áudio.  

O projeto utiliza apenas **bibliotecas padrão do Python**, aplicando conceitos de **Programação Orientada a Objetos (POO)** e **Estruturas de Dados** 

***

## 🚀 Requisitos

- Python >= 3.9  
- pip (gerenciador de pacotes padrão)
- As dependências listadas no arquivo `requirements.txt`

***

## ⚙️ Instalação

Siga os passos abaixo para configurar e executar o projeto no seu ambiente.

**1. Crie uma pasta para o projeto e adicione os arquivos:**

Coloque nesta pasta os seguintes arquivos:

- `playlist.py` (arquivo principal com o código completo)
- `requirements.txt` (contém os requisitos de execução)
- `musicas.json` (opcional, gerado automaticamente após salvar a playlist)

***

**2. Abra o terminal e navegue até a pasta criada:**

```bash
cd caminho/para/sua/pasta
```

***

**3. Crie e ative um ambiente virtual (recomendado):**

Para isolar o ambiente de execução do projeto, execute:

```bash
python -m venv venv
```

Ative o ambiente:

- **Windows (PowerShell):**
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  venv\Scripts\activate
  ```

- **Windows (CMD):**
  ```bash
  venv\Scripts\activate.bat
  ```

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

***

**4. Verifique os requisitos:**

Como o projeto utiliza apenas bibliotecas nativas, nenhuma instalação é necessária.  
Mas, se desejar garantir a compatibilidade do ambiente, confirme com:

```bash
pip install -r requirements.txt
```

***

## ▶️ Execução

Para rodar o programa, execute o arquivo principal no terminal:

```bash
python playlist.py
```

Ao iniciar, o programa exibirá o **menu interativo** com as opções disponíveis.

***

## ✅ Funcionalidades

- **Adicionar música:** inclui uma nova faixa à playlist.  
- **Remover música:** exclui uma música pelo título.  
- **Avançar:** toca a próxima música da lista.  
- **Retroceder:** volta para a música anterior.  
- **Exibir playlist:** mostra todas as faixas adicionadas.  
- **Salvar em JSON:** exporta a lista de músicas para o arquivo `playlist.json`.  
- **Carregar de JSON:** importa automaticamente músicas de um arquivo salvo.  
- **Encerrar:** sai do programa.  

***

## 🎸 Repertório Inicial

A playlist padrão é composta por faixas icônicas do **rock nacional dos anos 80 e 90**, como:

- Pro Dia Nascer Feliz – Barão Vermelho  
- Tempo Perdido – Legião Urbana  
- Primeiros Erros – Capital Inicial  
- O Tempo Não Para – Cazuza  
- Pelados em Santos – Mamonas Assassinas  

***

## 🧠 Conceitos Aplicados

- **Listas duplamente ligadas:** estrutura de dados customizada para navegação sequencial e reversa.  
- **Programação Orientada a Objetos (POO):** encapsulamento e modularidade.  
- **Manipulação de arquivos JSON:** serialização e persistência de dados.  
- **Interação via console:** menus textuais e laços de controle.  

***

## 🙌 Créditos

Desenvolvido como parte da **Pré-avaliação 2025_2** da FATEC Rio Claro  
Disciplina: **Estrutura de Dados e Linguagem de Programação II**

---

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/72032235/f0b93126-fb20-49f7-856a-23dafe2b2b8d/README-1.md)
