# Labeling Guide — Rome Weather Classification

## Project Overview
- **Dataset:** Rome Weather Image Classification
- **Source:** Kaggle (rogeriovaz/rome-weather-classification)
- **Total images:** 250 (50 per category)
- **Labeling tool:** Label Studio (local)
- **Labeler:** Paula
- **Date:** May 2026

## Purpose of Labeling
To create a labeled image dataset for weather classification.
The labeled data will be used to train a machine learning model
that can automatically identify weather conditions from images.

## Label Definitions

| Label | Definition |
|---|---|
| **Cloudy** | Sky is covered with grey/white clouds, no blue sky visible |
| **Foggy** | Visibility is reduced, objects in distance appear blurred or invisible |
| **Rainy** | Visible rain, wet surfaces, or dark stormy sky |
| **Snowy** | Snow visible on ground, rooftops, or falling from sky |
| **Sunny** | Clear blue sky, bright sunlight visible |

## Edge Cases & Rules

- **Cloudy vs Foggy:** If visibility is clearly reduced → Foggy.
  If sky is just overcast but visibility is fine → Cloudy
- **Rainy vs Cloudy:** If no rain is visible but sky is dark → Cloudy.
  Only label Rainy if rain or wet surfaces are clearly visible
- **Ambiguous images:** If an image could belong to two categories
  and a clear decision cannot be made → Skip (unlabeled)

## Skipped Images
7 images were skipped during annotation:
- 6 Cloudy images — too ambiguous to distinguish from Foggy
- 1 Rainy image — no clear rain visible, could be Cloudy

**Reason:** Including weak or ambiguous images could confuse
the model during training and reduce its accuracy.
This is a deliberate quality decision.

## Ethical Considerations
- A small number of images contain people/faces in the background
  → Minor privacy concern, but faces are incidental and not the
  focus of the labeling task
- The few visible faces appear to be predominantly white/European,
  reflecting Rome's geographic and demographic context
  → If this dataset were used for people-related tasks, this would
  represent a significant diversity bias. For weather classification
  this has minimal impact, but is worth noting.
- Images are from one city (Rome) → Geographic bias possible.
  Model may not generalize well to weather in other regions
- All 5 weather categories have roughly equal representation
  (44-50 images each) → No significant class imbalance

## Dataset Statistics
| Label | Count |
|---|---|
| Foggy | 50 |
| Snowy | 50 |
| Sunny | 50 |
| Rainy | 49 |
| Cloudy | 44 |
| Skipped | 7 |
| **Total labeled** | **243** |

## Output Files
- `annotations.json` — raw Label Studio export
- `labeled_dataset.csv` — clean CSV with image names and labels