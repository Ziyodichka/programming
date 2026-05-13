# 🚀 FastAPI + Vercel + GitHub Actions CI/CD

Python FastAPI loyihasini GitHub orqali Vercel ga avtomatik deploy qilish.

## 📁 Loyiha strukturasi

```
fastapi-vercel-demo/
├── app/
│   ├── main.py              # FastAPI asosiy fayl
│   └── routers/
│       └── items.py         # API routerlar
├── tests/
│   └── test_main.py         # Pytest testlar
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions pipeline
├── vercel.json              # Vercel konfiguratsiya
├── requirements.txt
└── README.md
```

## ⚙️ CI/CD Pipeline qanday ishlaydi

```
Push to GitHub
      │
      ▼
┌─────────────┐
│  1. TEST    │  ← pytest + flake8 (barcha branch)
└──────┬──────┘
       │ ✅ o'tsa
       ▼
┌─────────────┐
│  2. DEPLOY  │  ← faqat `main` branch
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  3. NOTIFY  │  ← natija chiqaradi
└─────────────┘
```

## 🛠️ Sozlash bosqichlari

### 1. GitHub Secrets qo'shish

GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret nomi | Qayerdan olish |
|---|---|
| `VERCEL_TOKEN` | vercel.com → Settings → Tokens |
| `VERCEL_ORG_ID` | vercel.com → Settings → General → Team ID |
| `VERCEL_PROJECT_ID` | Vercel project → Settings → General → Project ID |

### 2. Vercel da loyiha yaratish

```bash
# Vercel CLI o'rnatish
npm install -g vercel

# Login
vercel login

# Loyihani ulash (birinchi marta)
vercel
```

### 3. GitHub ga push qilish

```bash
git init
git add .
git commit -m "feat: initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

Push qilgandan so'ng GitHub Actions avtomatik ishga tushadi! 🎉

## 🧪 Lokal ishga tushirish

```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# O'rnatish
pip install -r requirements.txt

# Serverni ishga tushirish
uvicorn app.main:app --reload

# Testlar
pytest tests/ -v
```

API docs: http://localhost:8000/docs

## 📡 API Endpointlar

| Method | URL | Tavsif |
|--------|-----|--------|
| GET | `/` | Asosiy sahifa |
| GET | `/health` | Health check |
| GET | `/api/v1/items/` | Barcha itemlar |
| GET | `/api/v1/items/{id}` | Bitta item |
| POST | `/api/v1/items/` | Yangi item |
