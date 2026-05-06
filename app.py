from flask import Flask, render_template_string
import math

app = Flask(__name__)

# ── Helper functions ──────────────────────────────────────────────

def compute_hcf_lcm(a, b):
    hcf = math.gcd(a, b)
    lcm = abs(a * b) // hcf
    return hcf, lcm

def reverse_string(s):
    return s[::-1]

def factorials(start, end):
    return {n: math.factorial(n) for n in range(start, end + 1)}

# ── HTML Template ─────────────────────────────────────────────────

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BCS601-USN4MW23CS076 | Cloud App</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');
  :root {
    --bg: #0a0e1a; --card: #111827; --border: #1e2d45;
    --accent: #00d4ff; --green: #00ff88; --yellow: #ffd700;
    --text: #e2e8f0; --muted: #64748b;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: 'Syne', sans-serif; min-height: 100vh; }
  header { padding: 2rem; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
  header h1 { font-size: 1.4rem; font-weight: 800; color: var(--accent); letter-spacing: -0.02em; }
  header span { font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--muted); }
  .hero { padding: 3rem 2rem 1rem; text-align: center; }
  .hero h2 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; line-height: 1.1; }
  .hero h2 em { font-style: normal; color: var(--accent); }
  .hero p { margin-top: 0.8rem; color: var(--muted); font-size: 0.95rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; padding: 2rem; max-width: 1100px; margin: 0 auto; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1.8rem; position: relative; overflow: hidden; }
  .card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; }
  .card.blue::before { background: var(--accent); }
  .card.green::before { background: var(--green); }
  .card.yellow::before { background: var(--yellow); }
  .card-label { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin-bottom: 0.6rem; }
  .card h3 { font-size: 1.15rem; font-weight: 700; margin-bottom: 1.2rem; }
  .card.blue h3 { color: var(--accent); }
  .card.green h3 { color: var(--green); }
  .card.yellow h3 { color: var(--yellow); }
  .result-row { display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0; border-bottom: 1px solid var(--border); font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; }
  .result-row:last-child { border-bottom: none; }
  .result-row .label { color: var(--muted); }
  .result-row .value { font-weight: 700; font-size: 1rem; }
  .card.blue .value { color: var(--accent); }
  .card.green .value { color: var(--green); }
  .card.yellow .value { color: var(--yellow); }
  .string-box { background: #0d1b2a; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; font-family: 'JetBrains Mono', monospace; margin-top: 0.4rem; }
  .string-box .original { color: var(--muted); font-size: 0.8rem; margin-bottom: 0.4rem; }
  .string-box .reversed { color: var(--green); font-size: 1rem; font-weight: 700; word-break: break-all; }
  .arrow { color: var(--muted); margin: 0.3rem 0; font-size: 0.8rem; }
  footer { text-align: center; padding: 2rem; color: var(--muted); font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; border-top: 1px solid var(--border); margin-top: 1rem; }
  .badge { display: inline-flex; align-items: center; gap: 0.4rem; background: #0d2137; border: 1px solid var(--accent); color: var(--accent); font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; padding: 0.3rem 0.7rem; border-radius: 999px; margin-top: 1rem; }
  .dot { width: 6px; height: 6px; background: var(--green); border-radius: 50%; animation: pulse 1.5s infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
</style>
</head>
<body>
<header>
  <h1>BCS601-USN4MW23CS076</h1>
  <span>Deployed on Render · Python Flask · Cloud Lab</span>
</header>

<div class="hero">
  <h2>Cloud Computing <em>Lab Project</em></h2>
  <p>BCS601 · Three programs in one app · Deployed via Render</p>
  <div class="badge"><span class="dot"></span> Live on Render</div>
</div>

<div class="grid">

  <!-- Card 1: HCF & LCM -->
  <div class="card blue">
    <div class="card-label">Program 1</div>
    <h3>HCF &amp; LCM Calculator</h3>
    <div class="result-row"><span class="label">Input A</span><span class="value">{{ a }}</span></div>
    <div class="result-row"><span class="label">Input B</span><span class="value">{{ b }}</span></div>
    <div class="result-row"><span class="label">HCF (GCD)</span><span class="value">{{ hcf }}</span></div>
    <div class="result-row"><span class="label">LCM</span><span class="value">{{ lcm }}</span></div>
  </div>

  <!-- Card 2: String Reversal -->
  <div class="card green">
    <div class="card-label">Program 2</div>
    <h3>String Reversal</h3>
    <div class="string-box">
      <div class="original">Original:</div>
      <div class="reversed" style="color:var(--text)">{{ original_str }}</div>
      <div class="arrow">↓ reversed</div>
      <div class="reversed">{{ reversed_str }}</div>
    </div>
  </div>

  <!-- Card 3: Factorials -->
  <div class="card yellow">
    <div class="card-label">Program 3</div>
    <h3>Factorials (4 → 8)</h3>
    {% for n, f in fact_table.items() %}
    <div class="result-row">
      <span class="label">{{ n }}!</span>
      <span class="value">{{ f }}</span>
    </div>
    {% endfor %}
  </div>

</div>

<footer>
  BCS601-USN4MW23CS076 · bcs601_4mwcs076 · GitHub → Render CI/CD Pipeline · {{ year }}
</footer>
</body>
</html>
"""

# ── Routes ────────────────────────────────────────────────────────

@app.route("/")
def index():
    import datetime
    a, b = 18, 12
    hcf, lcm = compute_hcf_lcm(a, b)
    original = "Fun with Programming"
    return render_template_string(
        TEMPLATE,
        a=a, b=b, hcf=hcf, lcm=lcm,
        original_str=original,
        reversed_str=reverse_string(original),
        fact_table=factorials(4, 8),
        year=datetime.datetime.now().year
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
