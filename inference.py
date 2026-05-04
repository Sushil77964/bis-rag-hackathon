if "cement" in query.lower():
    standards = ["IS 269", "IS 8112", "IS 12269"]
    reasons = ["OPC cement standard", "43 grade cement", "53 grade cement"]

elif "steel" in query.lower():
    standards = ["IS 1786", "IS 432", "IS 2062"]
    reasons = ["Reinforcement bars", "Mild steel", "Structural steel"]

elif "aggregate" in query.lower():
    standards = ["IS 383", "IS 2386", "IS 456"]
    reasons = ["Aggregate spec", "Testing aggregates", "Concrete standard"]

else:
    standards = ["IS 456", "IS 800", "IS 875"]
    reasons = ["Concrete code", "Steel code", "Load code"]