# BCS601-USN4MW23CS076 — Cloud Computing Lab Project

**Subject:** Cloud Computing (BCS601)  
**USN:** 4mw23cs076  
**Repo:** `bcs601_4mwcs076`  
**Platform:** Render (free tier)  
**Language:** Python 3 + Flask

---

## 🚀 Live URL

> **https://bcs601-usn4mw23cs076.onrender.com**  
> *(Replace with your actual Render URL after deployment)*

---

## 📋 Programs Included

| # | Program | Input | Output |
|---|---------|-------|--------|
| 1 | HCF & LCM | 18, 12 | HCF=6, LCM=36 |
| 2 | String Reversal | "Fun with Programming" | "gnimmargorP htiw nuF" |
| 3 | Factorials (4–8) | 4,5,6,7,8 | 24, 120, 720, 5040, 40320 |

---

## 🗂 Project Structure

```
bcs601_4mwcs076/
├── app.py            # Main Flask application
├── requirements.txt  # Python dependencies
├── Procfile          # Render/Heroku start command
└── README.md         # This file
```

---

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/mohithkotian/bcs601_4mwcs076.git
cd bcs601_4mwcs076

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
# Open http://localhost:5000
```

---

## ☁️ Deploy on Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo `bcs601_4mwcs076`
4. Set **Build Command:** `pip install -r requirements.txt`
5. Set **Start Command:** `gunicorn app:app`
6. Click **Deploy** — Render gives you a free `.onrender.com` URL

---

## 🔗 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Render Deployment Guide](https://render.com/docs/deploy-flask)
- [Python math.gcd](https://docs.python.org/3/library/math.html#math.gcd)
- [Python math.factorial](https://docs.python.org/3/library/math.html#math.factorial)
