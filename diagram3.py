import matplotlib.pyplot as plt

källor = ["El", "Fjärrvärme", "Biogas", "Solenergi"]
andel = [55, 30, 10, 5]

plt.pie(andel, labels=källor, autopct="%1.1f%%", startangle=90, colors=["#1976D2","#FF7043","#9CCC65","#FFD54F"])
plt.title("Fördelning av energikällor")
plt.savefig("diagram3.png", dpi=300, bbox_inches="tight")
# plt.show()
