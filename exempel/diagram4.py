import numpy as np
import matplotlib.pyplot as plt

kategorier = ["Pump 1", "Pump 2", "Fläkt", "Belysning"]
före = [12000, 15000, 8000, 5000]
efter = [9000, 11000, 6000, 4000]

x = np.arange(len(kategorier))
bredd = 0.35

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(x - bredd/2, före, bredd, label="Före", color="lightcoral")
ax.bar(x + bredd/2, efter, bredd, label="Efter", color="mediumseagreen")

ax.set_xticks(x)
ax.set_xticklabels(kategorier)
ax.set_ylabel("kWh/år")
ax.set_title("Energibesparing efter renovering")
ax.legend()
plt.tight_layout()
plt.savefig("diagram4.png", dpi=300, bbox_inches="tight")
# plt.show()
