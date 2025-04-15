# GitHub Actions + GitHub Pages 🚀

Este é um projeto simples de demonstração de como utilizar **GitHub Actions** para realizar o deploy automático de um site estático via **GitHub Pages**.

## 📄 Sobre o projeto

- O site é uma página HTML simples hospedada com GitHub Pages.
- O deploy acontece automaticamente sempre que há um push na branch `main`.
- A publicação é feita na branch `gh-pages`, usando a action em **deploy.yml**

## ⚙️ Tecnologias e ferramentas

- GitHub Actions
- GitHub Pages
- HTML
- Git Bash + VSCode

## 📂 Estrutura

```bash
.
├── README.md
├── index.html
└── .github
    └── workflows
        └── deploy.yml
