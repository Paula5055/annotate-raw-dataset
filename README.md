# annotate-raw-dataset
# Annotate Raw Dataset — Rome Weather Classification

## Project Overview
This project annotates a dataset of 250 weather images from Rome
as part of the AI Foundations course. The goal is to label each
image with the correct weather condition responsibly and ethically,
following best practices in data annotation.

## Dataset
- **Source:** Kaggle — Rome Weather Image Classification
  (rogeriovaz/rome-weather-classification)
- **Size:** 250 images total, 50 per weather category
- **Categories:** Cloudy, Foggy, Rainy, Snowy, Sunny

## Annotation Tool
Label Studio (local/community version)

## Files
- `data/Rome Weather/` — original raw images organized by category
- `annotate.py` — Python script that processes Label Studio export
- `annotations.json` — raw Label Studio export with all labels
- `labeled_dataset.csv` — final labeled dataset (image + label)
- `labeling_guide.md` — detailed annotation rules and ethics notes

## How to Run
1. Install dependencies: `pip install label-studio pandas`
2. Open Label Studio: `label-studio`
3. Run the annotation script: `python annotate.py`

## Ethical Considerations
- Dataset contains no sensitive personal data
- Small number of incidental faces visible in some images
- Geographic bias: all images from Rome, Italy
- Ambiguous images were skipped to ensure label quality
- See `labeling_guide.md` for full ethical documentation

## Results
| Label | Count |
|---|---|
| Foggy | 50 |
| Snowy | 50 |
| Sunny | 50 |
| Rainy | 49 |
| Cloudy | 44 |
| Skipped | 7 |
| **Total labeled** | **243** |