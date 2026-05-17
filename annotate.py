import json
import pandas as pd

# Load the exported JSON file from Label Studio
with open('annotations.json', 'r') as f:
    annotations = json.load(f)

# Create a list to store results
results = []

# Go through each labeled image
for item in annotations:
    # Get the image filename
    image_name = item['data']['image'].split('/')[-1]
    
    # Get the label that was assigned
    if item['annotations'] and item['annotations'][0]['result']:
        label = item['annotations'][0]['result'][0]['value']['choices'][0]
    else:
        label = 'unlabeled'
    
    results.append({
        'image': image_name,
        'label': label
    })

# Save as CSV
df = pd.DataFrame(results)
df.to_csv('labeled_dataset.csv', index=False)

print(f"Done! {len(results)} images labeled ✅")
print(df['label'].value_counts())