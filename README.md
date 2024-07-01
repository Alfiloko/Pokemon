# Pokémon Info

Este é um projeto Django que exibe informações sobre Pokémon usando a PokeAPI. Ele mostra detalhes como nome, altura, peso, habilidades e tipos, além de exibir imagens animadas dos Pokémon.

## Funcionalidades

- Pesquisar informações de qualquer Pokémon pelo nome ou ID.
- Exibir imagens animadas dos Pokémon (ou imagens padrão se a animada não estiver disponível)

## Requisitos

- Python 3.x
- Django
- Requests

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

## Uso

1. Acesse `http://127.0.0.1:8000/` no seu navegador.
2. Use a barra de pesquisa para procurar por um Pokémon pelo nome ou ID.
3. Veja as informações detalhadas sobre o Pokémon, incluindo sua imagem animada e ícones de tipos.

## Estrutura do Projeto

├── myproject/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── ...
├── myapp/
│ ├── views.py
│ ├── static/
| | └──image/
| | └──style/
│ ├── templates/
│ │ └── home.html
│ └── ...
├── manage.py
├── requirements.txt
└── README.md
