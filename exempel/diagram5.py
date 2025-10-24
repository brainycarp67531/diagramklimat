import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    "Månad": np.repeat(["Jan", "Feb", "Mar", "Apr"], 30),
    "kWh per dag": np.concatenate([
        np.random.normal(100, 15, 30),
        np.random.normal(90, 10, 30),
        np.random.normal(80, 8, 30),
        np.random.normal(70, 5, 30)
    ])
}
df = pd.DataFrame(data)

plt.figure(figsize=(8,4))
sns.boxplot(x="Månad", y="kWh per dag", hue="Månad", data=df, palette="Set2", legend=False)
plt.title("Daglig energiförbrukning – variation per månad")
plt.tight_layout()
plt.savefig("diagram5.png", dpi=300, bbox_inches="tight")
# plt.show()
