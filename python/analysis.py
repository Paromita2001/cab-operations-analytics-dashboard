import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/trips.csv")

payment = df["payment_method"].value_counts()

print(payment)

plt.figure(figsize=(8, 5))

payment.plot(kind="pie", autopct="%1.1f%%")

plt.title("Payment Methods")

plt.ylabel("")

plt.show()