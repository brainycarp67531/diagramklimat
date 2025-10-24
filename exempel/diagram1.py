import pandas as pd
import matplotlib.pyplot as plt

# Exempeldata: kWh per månad
data = {
    "Månad": ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"],
    "Energiförbrukning (kWh)": [3200, 2800, 2500, 2000, 1800, 1500, 1300, 1400, 1700, 2200, 2600, 3100]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,4))
plt.plot(df["Månad"], df["Energiförbrukning (kWh)"], marker="o", color="tab:blue")
plt.title("Energiförbrukning per månad")
plt.xlabel("Månad")
plt.ylabel("kWh")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("diagram1.png", dpi=300, bbox_inches="tight")
# plt.show()
