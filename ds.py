import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Industry": [
        "Agriculture", "Manufacturing", "Energy Production",
        "Construction", "Mining", "Services"
    ],
    "Water_Usage_million_m3": [700, 200, 120, 50, 30, 20]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.bar(df["Industry"], df["Water_Usage_million_m3"], color='skyblue', edgecolor='black')
plt.xlabel("Industry", fontsize=12)
plt.ylabel("Water Usage (million m³)", fontsize=12)
plt.title("Water Usage by Industry (Sample FAO Aquastat Data)", fontsize=14)
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
