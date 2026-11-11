from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent.parent / "data" / "health_study_dataset.csv"
df = pd.read_csv(file_path)

print(df.head())