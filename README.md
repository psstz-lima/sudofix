# SudoFix 🔧

![SudoFix Banner](public/social.png)

**SudoFix** é um hub de conhecimento para desenvolvedores, focado em resolver os erros de programação mais comuns de forma rápida e eficiente. O site utiliza Programmatic SEO para gerar tutoriais técnicos detalhados automaticamente via Inteligência Artificial.

🔗 **Acesse agora:** [sudofix.dev](https://sudofix.dev)

## 🚀 Funcionalidades

- **Multi-Linguagem (i18n)**: Suporte completo para **Inglês (EN)**, **Português (PT)** e **Espanhol (ES)**.
- **Frontend Unificado**: Arquitetura "Single Source of Truth" onde o layout é consistente em todos os idiomas.
- **Modo Escuro**: Detecção automática de preferência do sistema e toggle manual.
- **Conteúdo Gerado por IA**: Scripts em Python (`generator.py`) que criam posts Markdown baseados em sementes CSV.
- **Suporte a LLM Local**: Capacidade de rodar traduções e gerações usando **Ollama** (ex: `DevOps-Hybrid`) para privacidade e custo zero.
- **Busca Rápida**: Integração com **Pagefind** para indexação estática e busca instantânea.
- **UX Otimizada**: Botões de cópia de código, breadcrumbs para SEO e links de edição no GitHub.

## 🛠️ Tecnologias

- **Framework**: [Astro](https://astro.build) (Static Site Generation - SSG)
- **Estilização**: [Tailwind CSS v4](https://tailwindcss.com)
- **Backend (Scripts)**: Python 3.12 + Pandas + OpenAI Client (Groq/Ollama)
- **Deploy**: Cloudflare Pages
- **Busca**: Pagefind

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/psstz-lima/sudofix.git
cd sudofix

# Instalar dependências Frontend
npm install

# Instalar dependências Python (para scripts de geração)
pip install openai pandas python-dotenv slugify
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
# Opção 1: Usar Groq (Nuvem - Rápido)
GROQ_API_KEY=sua_chave_aqui

# Opção 2: Usar Ollama (Local - Gratuito)
# Não requer chave no .env, basta configurar o script para localhost:11434
```

## 📝 Gerando Conteúdo

Existem dois scripts principais para gerenciar o conteúdo:

### 1. Gerador de Artigos (`generator.py`)

Lê um arquivo CSV e cria tutoriais novos.

```bash
# Gerar artigos de Python
python3 generator.py errors.csv Python

# Gerar artigos de JavaScript
python3 generator.py js_errors.csv JavaScript
```

### 2. Tradução em Massa (`force_translate.py`)

Traduz artigos existentes do Inglês para Português e Espanhol. Suporta "retry" automático para evitar Rate Limits ou uso de LLM Local.

```bash
python3 force_translate.py
```

## 🏃‍♂️ Rodando Localmente

Para iniciar o servidor de desenvolvimento do Astro:

```bash
npm run dev
```

Acesse `http://localhost:4321`.

## 🚢 Deploy

O projeto é configurado para rodar no Cloudflare Pages.

```bash
# Build de produção
npm run build

# Deploy direto via terminal (requer login no Wrangler)
npx wrangler pages deploy dist --project-name=sudofix
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou Pull Requests.

---

_Desenvolvido com ❤️ por Paulo Lima._
