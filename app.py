from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

def compute_hcf_lcm(a, b):
    hcf = math.gcd(a, b)
    lcm = abs(a * b) // hcf
    return hcf, lcm

def reverse_string(s):
    return s[::-1]

def factorials(start, end):
    return {n: math.factorial(n) for n in range(start, end + 1)}

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BCS601-4MW23CS076</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #07090f;
    --surface: #0e1117;
    --border: rgba(255,255,255,0.07);
    --accent1: #00f5c8;
    --accent2: #7c6dfa;
    --accent3: #ff6b6b;
    --text: #f0f2f8;
    --muted: #6b7280;
    --card: #111520;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Outfit', sans-serif;
    min-height: 100vh;
    background-image:
      radial-gradient(ellipse 80% 50% at 50% -20%, rgba(124,109,250,0.15), transparent),
      radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,245,200,0.07), transparent);
  }

  /* NAV */
  nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.2rem 2rem;
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(10px);
    position: sticky; top: 0; z-index: 100;
    background: rgba(7,9,15,0.8);
  }
  .nav-brand { font-family: 'Space Mono', monospace; font-size: 0.85rem; color: var(--accent1); letter-spacing: 0.05em; }
  .nav-pill {
    display: flex; align-items: center; gap: 0.5rem;
    background: rgba(0,245,200,0.08); border: 1px solid rgba(0,245,200,0.2);
    color: var(--accent1); font-size: 0.75rem; font-family: 'Space Mono', monospace;
    padding: 0.3rem 0.8rem; border-radius: 999px;
  }
  .nav-pill::before { content:''; width:7px; height:7px; border-radius:50%; background:var(--accent1); animation:blink 1.8s infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

  /* HERO */
  .hero { text-align: center; padding: 4rem 2rem 2.5rem; }
  .hero-eyebrow {
    display: inline-block; font-family: 'Space Mono', monospace; font-size: 0.7rem;
    letter-spacing: 0.2em; color: var(--accent2); text-transform: uppercase;
    border: 1px solid rgba(124,109,250,0.3); padding: 0.3rem 1rem; border-radius: 999px;
    margin-bottom: 1.5rem; background: rgba(124,109,250,0.08);
  }
  .hero h1 { font-size: clamp(2.2rem, 6vw, 4rem); font-weight: 800; line-height: 1.05; margin-bottom: 1rem; }
  .hero h1 span { color: var(--accent1); }
  .hero p { color: var(--muted); font-size: 1rem; font-weight: 300; }

  /* GRID */
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; padding: 1rem 2rem 4rem; max-width: 1200px; margin: 0 auto; }

  /* CARD */
  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
  }
  .card:hover { transform: translateY(-3px); }
  .card.c1:hover { border-color: rgba(0,245,200,0.3); }
  .card.c2:hover { border-color: rgba(124,109,250,0.3); }
  .card.c3:hover { border-color: rgba(255,107,107,0.3); }
  .card-top { padding: 1.4rem 1.4rem 0; }
  .card-tag { font-family: 'Space Mono', monospace; font-size: 0.65rem; letter-spacing: 0.15em; color: var(--muted); margin-bottom: 0.4rem; }
  .card-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 1.2rem; }
  .c1 .card-title { color: var(--accent1); }
  .c2 .card-title { color: var(--accent2); }
  .c3 .card-title { color: var(--accent3); }

  /* FORM */
  form { padding: 0 1.4rem; }
  .input-row { display: flex; gap: 0.6rem; margin-bottom: 0.8rem; flex-wrap: wrap; }
  input[type=text], input[type=number] {
    flex: 1; min-width: 80px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text);
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    padding: 0.55rem 0.9rem;
    outline: none;
    transition: border-color 0.2s;
  }
  input:focus { border-color: rgba(255,255,255,0.25); }
  .c1 input:focus { border-color: rgba(0,245,200,0.4); }
  .c2 input:focus { border-color: rgba(124,109,250,0.4); }
  .c3 input:focus { border-color: rgba(255,107,107,0.4); }
  input[type=number] { -moz-appearance: textfield; }
  input[type=number]::-webkit-outer-spin-button,
  input[type=number]::-webkit-inner-spin-button { -webkit-appearance: none; }

  button[type=submit] {
    width: 100%; padding: 0.65rem;
    border: none; border-radius: 8px; cursor: pointer;
    font-family: 'Outfit', sans-serif; font-size: 0.9rem; font-weight: 600;
    transition: opacity 0.15s, transform 0.15s;
    margin-bottom: 1.2rem;
  }
  button:hover { opacity: 0.85; transform: scale(0.99); }
  .c1 button[type=submit] { background: var(--accent1); color: #07090f; }
  .c2 button[type=submit] { background: var(--accent2); color: #fff; }
  .c3 button[type=submit] { background: var(--accent3); color: #fff; }

  /* RESULT */
  .result { background: rgba(255,255,255,0.03); border-top: 1px solid var(--border); padding: 1.2rem 1.4rem; }
  .result-row { display: flex; justify-content: space-between; align-items: center; padding: 0.4rem 0; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: 0.9rem; }
  .result-row:last-child { border-bottom: none; }
  .rl { color: var(--muted); }
  .rv { font-family: 'Space Mono', monospace; font-weight: 700; font-size: 1rem; }
  .c1 .rv { color: var(--accent1); }
  .c2 .rv { color: var(--accent2); }
  .c3 .rv { color: var(--accent3); }
  .string-display {
    background: rgba(0,0,0,0.3); border-radius: 8px; padding: 0.8rem;
    font-family: 'Space Mono', monospace; font-size: 0.8rem; word-break: break-all;
  }
  .s-label { color: var(--muted); font-size: 0.7rem; margin-bottom: 0.3rem; }
  .s-val { color: var(--text); margin-bottom: 0.6rem; }
  .s-arrow { color: var(--muted); font-size: 0.75rem; margin: 0.3rem 0; }
  .s-rev { color: var(--accent2); font-weight: 700; }
  .error { color: var(--accent3); font-size: 0.8rem; padding: 0.5rem 0; font-family: 'Space Mono', monospace; }

  /* FACTORIAL TABLE */
  .fact-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
  .fact-table th { text-align: left; color: var(--muted); font-weight: 400; font-size: 0.75rem; padding: 0.3rem 0; border-bottom: 1px solid var(--border); }
  .fact-table td { padding: 0.4rem 0; border-bottom: 1px solid rgba(255,255,255,0.03); }
  .fact-table td:last-child { text-align: right; font-family: 'Space Mono', monospace; font-weight: 700; color: var(--accent3); }
  .fact-range { display: flex; gap: 0.6rem; margin-bottom: 0.8rem; }
  .fact-range input { width: 70px; flex: none; text-align: center; }

  footer {
    text-align: center; padding: 1.5rem;
    color: var(--muted); font-family: 'Space Mono', monospace; font-size: 0.7rem;
    border-top: 1px solid var(--border);
  }
</style>
</head>
<body>

<nav>
  <span class="nav-brand">BCS601-4MW23CS076</span>
  <span class="nav-pill">Live on Render</span>
</nav>

<div class="hero">
  <div class="hero-eyebrow">Cloud Computing Lab · BCS601</div>
  <h1>Interactive <span>Math</span> Programs</h1>
  <p>Enter your own inputs — all three programs compute live</p>
</div>

<div class="grid">

  <!-- CARD 1: HCF & LCM -->
  <div class="card c1">
    <div class="card-top">
      <div class="card-tag">PROGRAM 01</div>
      <div class="card-title">HCF &amp; LCM Calculator</div>
    </div>
    <form method="POST" action="/">
      <input type="hidden" name="prog" value="hcf">
      <div class="input-row">
        <input type="number" name="a" placeholder="Number A" value="{{ hcf_a }}" required>
        <input type="number" name="b" placeholder="Number B" value="{{ hcf_b }}" required>
      </div>
      <button type="submit">Calculate →</button>
    </form>
    <div class="result">
      {% if hcf_result %}
      <div class="result-row"><span class="rl">Input A</span><span class="rv">{{ hcf_a }}</span></div>
      <div class="result-row"><span class="rl">Input B</span><span class="rv">{{ hcf_b }}</span></div>
      <div class="result-row"><span class="rl">HCF (GCD)</span><span class="rv">{{ hcf_result }}</span></div>
      <div class="result-row"><span class="rl">LCM</span><span class="rv">{{ lcm_result }}</span></div>
      {% else %}
      <div class="result-row"><span class="rl">Enter two numbers above</span></div>
      {% endif %}
    </div>
  </div>

  <!-- CARD 2: String Reversal -->
  <div class="card c2">
    <div class="card-top">
      <div class="card-tag">PROGRAM 02</div>
      <div class="card-title">String Reversal</div>
    </div>
    <form method="POST" action="/">
      <input type="hidden" name="prog" value="str">
      <div class="input-row">
        <input type="text" name="s" placeholder="Type any string..." value="{{ str_input }}" required>
      </div>
      <button type="submit">Reverse →</button>
    </form>
    <div class="result">
      {% if str_result %}
      <div class="string-display">
        <div class="s-label">Original:</div>
        <div class="s-val">{{ str_input }}</div>
        <div class="s-arrow">↓ reversed</div>
        <div class="s-rev">{{ str_result }}</div>
      </div>
      {% else %}
      <div class="result-row"><span class="rl">Enter a string above</span></div>
      {% endif %}
    </div>
  </div>

  <!-- CARD 3: Factorials -->
  <div class="card c3">
    <div class="card-top">
      <div class="card-tag">PROGRAM 03</div>
      <div class="card-title">Factorial Table</div>
    </div>
    <form method="POST" action="/">
      <input type="hidden" name="prog" value="fact">
      <div class="fact-range">
        <input type="number" name="fstart" placeholder="From" value="{{ fact_start }}" min="0" max="20" required>
        <input type="number" name="fend" placeholder="To" value="{{ fact_end }}" min="0" max="20" required>
      </div>
      <button type="submit">Compute →</button>
    </form>
    <div class="result">
      {% if fact_error %}
        <div class="error">{{ fact_error }}</div>
      {% elif fact_table %}
        <table class="fact-table">
          <tr><th>n</th><th>n!</th></tr>
          {% for n, f in fact_table.items() %}
          <tr><td>{{ n }}!</td><td>{{ "{:,}".format(f) }}</td></tr>
          {% endfor %}
        </table>
      {% else %}
      <div class="result-row"><span class="rl">Enter a range above</span></div>
      {% endif %}
    </div>
  </div>

</div>

<footer>BCS601-4MW23CS076 · bcs601_4mwcs076 · GitHub → Render CI/CD · 2026</footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    ctx = dict(
        hcf_a="", hcf_b="", hcf_result=None, lcm_result=None,
        str_input="", str_result=None,
        fact_start="4", fact_end="8", fact_table=factorials(4, 8), fact_error=None
    )

    if request.method == "POST":
        prog = request.form.get("prog")

        if prog == "hcf":
            try:
                a = int(request.form["a"])
                b = int(request.form["b"])
                ctx["hcf_a"] = a
                ctx["hcf_b"] = b
                ctx["hcf_result"], ctx["lcm_result"] = compute_hcf_lcm(a, b)
            except:
                pass

        elif prog == "str":
            s = request.form.get("s", "")
            ctx["str_input"] = s
            ctx["str_result"] = reverse_string(s)

        elif prog == "fact":
            try:
                fs = int(request.form["fstart"])
                fe = int(request.form["fend"])
                ctx["fact_start"] = fs
                ctx["fact_end"] = fe
                if fs < 0 or fe < 0:
                    ctx["fact_error"] = "Numbers must be 0 or greater"
                    ctx["fact_table"] = None
                elif fs > fe:
                    ctx["fact_error"] = "Start must be ≤ End"
                    ctx["fact_table"] = None
                elif fe - fs > 15:
                    ctx["fact_error"] = "Range too large (max 15)"
                    ctx["fact_table"] = None
                elif fe > 20:
                    ctx["fact_error"] = "Maximum value is 20"
                    ctx["fact_table"] = None
                else:
                    ctx["fact_table"] = factorials(fs, fe)
            except ValueError:
                ctx["fact_error"] = "Enter valid whole numbers"
                ctx["fact_table"] = None

    return render_template_string(TEMPLATE, **ctx)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
