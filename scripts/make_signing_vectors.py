"""Regenerate fixtures/signing-vectors.json. Both language implementations must reproduce these exactly."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
from ficium_contract import sign

KEY = "test-key-not-a-secret-0123456789abcdef"
cases = [
    ("ascii body", '{"id":"evt_01J9FIXTURE0001","type":"ping"}', 1790000000),
    ("unicode body", '{"note":"Île Maurice, Rs 1 000"}', 1790000300),
    ("empty object", "{}", 1790000600),
]
out = [{"description": d, "key": KEY, "timestamp": t, "body": b,
        "header": sign(b.encode("utf-8"), KEY.encode("utf-8"), t)} for d, b, t in cases]
p = Path(__file__).resolve().parents[1] / "fixtures" / "signing-vectors.json"
p.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {len(out)} vectors")
