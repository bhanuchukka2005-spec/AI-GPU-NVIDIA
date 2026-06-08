import time
import psutil
import pandas as pd

from groq import Groq
from google import genai

# -----------------------------
# API KEYS (replace these)
# -----------------------------
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

# -----------------------------
# Clients
# -----------------------------
groq_client = Groq(api_key=GROQ_API_KEY)

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# -----------------------------
# Test Prompts
# -----------------------------
PROMPTS = [
    "Explain phishing attacks",
    "Write Python code for bubble sort",
    "Explain transformers in AI"
]

# -----------------------------
# Groq Benchmark
# -----------------------------
def benchmark_groq(prompt):
    process = psutil.Process()

    try:
        mem_before = process.memory_info().rss / 1024**2
        start = time.time()

        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )

        end = time.time()
        mem_after = process.memory_info().rss / 1024**2

        return {
            "provider": "groq",
            "prompt": prompt,
            "response": response.choices[0].message.content,
            "latency_sec": round(end - start, 4),
            "memory_before_mb": round(mem_before, 2),
            "memory_after_mb": round(mem_after, 2),
            "error": None
        }

    except Exception as e:
        return {
            "provider": "groq",
            "prompt": prompt,
            "response": None,
            "latency_sec": None,
            "memory_before_mb": None,
            "memory_after_mb": None,
            "error": str(e)
        }

# -----------------------------
# Gemini Benchmark
# -----------------------------
def benchmark_gemini(prompt):
    process = psutil.Process()

    try:
        mem_before = process.memory_info().rss / 1024**2
        start = time.time()

        response = gemini_client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        end = time.time()
        mem_after = process.memory_info().rss / 1024**2

        return {
            "provider": "gemini",
            "prompt": prompt,
            "response": response.text,
            "latency_sec": round(end - start, 4),
            "memory_before_mb": round(mem_before, 2),
            "memory_after_mb": round(mem_after, 2),
            "error": None
        }

    except Exception as e:
        return {
            "provider": "gemini",
            "prompt": prompt,
            "response": None,
            "latency_sec": None,
            "memory_before_mb": None,
            "memory_after_mb": None,
            "error": str(e)
        }

# -----------------------------
# Run Benchmark
# -----------------------------
results = []

for p in PROMPTS:
    print("\nTesting:", p)

    results.append(benchmark_groq(p))
    results.append(benchmark_gemini(p))

# -----------------------------
# Results Table
# -----------------------------
df = pd.DataFrame(results)

print("\n================ RESULTS ================\n")
print(df)

# Optional: save results
df.to_csv("llm_benchmark_results.csv", index=False)
print("\nSaved to llm_benchmark_results.csv")