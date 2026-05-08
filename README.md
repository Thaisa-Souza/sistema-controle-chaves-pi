# Sistema Web para Gerenciamento de Chaves em Imobiliária de Pequeno Porte

Sistema web desenvolvido como projeto acadêmico com o objetivo de auxiliar no controle de retirada e devolução de chaves de imóveis destinados à locação em uma imobiliária de pequeno porte.

---

## Objetivo do Projeto

O sistema foi desenvolvido para solucionar dificuldades encontradas no controle manual de chaves, como:

- falta de controle em tempo real;
- dependência de registros em papel;
- dificuldade em identificar quem está com determinada chave;
- ausência de histórico organizado de movimentações;
- demora na consulta de informações;
- risco de perda de registros.

A proposta busca proporcionar maior organização, agilidade e segurança no gerenciamento das chaves dos imóveis.

---

## Funcionalidades

- Login de usuários
- Dashboard com indicadores
- Cadastro de imóveis
- Controle de status das chaves
- Registro de retirada de chaves
- Registro de devolução de chaves
- Histórico completo de movimentações
- Busca e filtros
- Paginação
- Layout responsivo para dispositivos móveis

---

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- Bootstrap 5
- HTML
- CSS

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Thaisa-Souza/sistema-controle-chaves-pi.git
```

### 2. Acessar a pasta

```bash
cd sistema-controle-chaves-pi
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar migrações

```bash
python manage.py migrate
```

### 7. Criar superusuário

```bash
python manage.py createsuperuser
```

### 8. Executar servidor

```bash
python manage.py runserver
```

### 9. Acessar no navegador

```text
http://127.0.0.1:8000/
```

---

## Observações

- Os dados e imagens utilizados neste projeto são fictícios e possuem finalidade exclusivamente acadêmica e demonstrativa.
- O sistema foi desenvolvido para fins educacionais.