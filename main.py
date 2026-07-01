import json, random, os

script_dir = os.path.dirname(os.path.abspath(__file__))
topics_path = os.path.join(script_dir, "topics.json")
used_path = os.path.join(script_dir, "used_ids.json")

with open(topics_path, "r", encoding="utf-8") as f:
    topics = json.load(f)

try:
    with open(used_path, "r") as f:
        used_ids = set(json.load(f))
except FileNotFoundError:
    used_ids = set()

available = [t for t in topics if t["id"] not in used_ids]

if not available:
    print(f"You've completed all {len(topics)} topics! Resetting the pool.")
    used_ids = set()
    available = topics

chosen = random.choice(available)
used_ids.add(chosen["id"])

with open(used_path, "w") as f:
    json.dump(list(used_ids), f)

print(f"{chosen['main_topic']} - {chosen['topic']}")