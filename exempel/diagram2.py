import matplotlib.pyplot as plt

byggnader = ["Kontor A", "Kontor B", "Lager", "Butik"]
förbrukning = [12000, 9000, 18000, 11000]

plt.bar(byggnader, förbrukning, color=["#4CAF50", "#FFC107", "#2196F3", "#E91E63"])
plt.title("Årlig energiförbrukning per byggnad")
plt.ylabel("kWh/år")
plt.tight_layout()
plt.savefig("diagram2.png", dpi=300, bbox_inches="tight")
# plt.show()
