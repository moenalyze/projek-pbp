import pandas as pd
import random

# Generate random well coordinates
num_points = 50  # you can change this
data = {
    "X": [round(random.uniform(0, 1000), 2) for _ in range(num_points)],
    "Y": [round(random.uniform(0, 1000), 2) for _ in range(num_points)],
    "Z": [round(random.uniform(-5, -300), 2) for _ in range(num_points)]  # depth values
}

df = pd.DataFrame(data)

# Save as CSV
file_path = "sumur_pengeboran_acak.csv"
df.to_csv(file_path, index=False)

# df.head(10), file_path
