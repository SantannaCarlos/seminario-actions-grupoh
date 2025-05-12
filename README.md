# GitHub Actions + GitHub Pages 🚀

Projeto de demonstração usando múltiplos containers com Docker Compose para realizar deploy automático de um site estático com GitHub Pages e fornecer relatórios dinâmicos via API.

---

## 📄 Sobre o Projeto

Este projeto simula um sistema automatizado inspirado no jogo **Satisfactory**, com:

- Uma página estática (frontend) interativa que consome uma API
- Um backend Python que lê o workflow do GitHub Actions (`deploy.yml`) e retorna um resumo via API
- Deploy automatizado via GitHub Actions para o GitHub Pages

---

## ⚙️ Tecnologias e Ferramentas

- GitHub Actions
- GitHub Pages
- HTML + JavaScript
- Python 3.9 + Flask + PyYAML
- Docker
- Docker Compose
- Nginx

---

## 🐳 Como executar com Docker Compose

> Pré-requisitos: Docker e Docker Compose instalados

1. Clone este repositório:

```bash
git clone https://github.com/SeuUsuario/seminario-actions-grupoh.git
cd seminario-actions-grupoh
```

2. Suba os containers:

```bash
docker-compose up --build
```

3. Acesse os serviços:

- **Frontend (site)**: http://localhost:8080
- **Backend (API)**: http://localhost:5000/api/workflow-summary

---

## 🔗 O que faz a API

A API `/api/workflow-summary` analisa o arquivo `.github/workflows/deploy.yml` e retorna algo assim:

```json
{
  "total_jobs": 1,
  "detalhes": {
    "deploy": 3
  }
}
```

Esse dado é carregado dinamicamente no site via JavaScript (`fetch()`).

---

## 📂 Estrutura do Projeto

```
/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── deploy.yml 
│       └── deploy-ghpages.yml  
├── docker-compose.yml
└── README.md
```

---

## 🧠 Possíveis melhorias

- Adicionar cache da API
- Geração de relatórios PDF
- Logs de deploy com histórico
- Exportar o JSON do summary

---