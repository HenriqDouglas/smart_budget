# 🧠 Smart Budget

Sistema pessoal de gestão de orçamento, feito para uso diário por quem busca **clareza, simplicidade e inteligência financeira**.

## 🚀 Tecnologias Utilizadas

- ⚙️ **Back-end**: Python, Flask, SQLAlchemy
- 🗃️ **Banco de dados**: PostgreSQL (Neon)
- 🌐 **Front-end**: React + TypeScript + Material UI
- ☁️ **Hospedagem planejada**: Render (API), Vercel (Front)

---

## 📂 Estrutura do Projeto

```
smart_budget/
├── backend/        # API Flask
│   ├── app.py
│   ├── models/
│   ├── routes/
│   └── database/
├── frontend/       # React com TypeScript + MUI
│   ├── src/
│   └── public/
└── README.md
```

---

## 🧪 Como Executar Localmente

### 🔹 Requisitos

- Python 3.10+
- Node.js 18+
- PostgreSQL (banco criado na [Neon](https://neon.tech))
- Git

### 🔸 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

> Lembre-se de configurar seu `.env` com a string da Neon:

```
DATABASE_URL=postgresql://usuario:senha@ep-xxxxx.us-east-2.aws.neon.tech/db_nome
```

### 🔸 Frontend

```bash
cd frontend
npm install
npm run dev
```

Acesse no navegador: [http://localhost:5173](http://localhost:5173)

---

## ✅ Status do Projeto

- [x] Estrutura profissional com Git e ambiente virtual
- [x] React com TypeScript e Material UI
- [x] Conexão com PostgreSQL via SQLAlchemy
- [ ] Modelos e rotas de despesas
- [ ] Dashboard com análise de gastos
- [ ] Importação de planilhas e simulação de impacto
- [ ] Publicação em ambiente web

---

## 👤 Autor

**Henrique Abreu**  
Desenvolvedor, analista de TI e sonhador financeiro ✨  
[GitHub](https://github.com/HenriqDouglas)

---

## 📜 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, melhorar e compartilhar.
