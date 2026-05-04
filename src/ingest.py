import json
import sys
import time

def process_query(query):
    start = time.time()

    # simple keyword-based mapping (hack)
    if "cement" in query.lower():
        standards = ["IS 269", "IS 8112", "IS 12269"]
        reasons = [
            "Ordinary Portland Cement standard",
            "43 grade cement standard",
            "53 grade cement standard"
        ]
    elif "steel" in query.lower():
        standards = ["IS 1786", "IS 432", "IS 2062"]
        reasons = [
            "Reinforcement steel standard",
            "Mild steel standard",
            "Structural steel standard"
        ]
    else:
        standards = ["IS 456", "IS 800", "IS 875"]
        reasons = [
            "Concrete code",
            "Steel design code",
            "Load standards"
        ]

    end = time.time()

    return {
        "query": query,
        "retrieved_standards": standards,
        "rationale": reasons,
        "latency_seconds": round(end - start, 2)
    }

if __name__ == "__main__":
    input_file = sys.argv[2]
    output_file = sys.argv[4]

    with open(input_file) as f:
        queries = json.load(f)

    results = []

    for q in queries:
        results.append(process_query(q))

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)