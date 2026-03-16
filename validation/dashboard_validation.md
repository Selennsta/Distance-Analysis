# Dashboard Validation

## Scope
Validated dashboard functionality for:
- Smartphones
- Tractors
- User Upload

## Checks performed
- Main dashboard opens successfully in Streamlit
- Dataset selector works for all three datasets
- Nearest neighbors table is displayed for selected products
- Neighbors are ordered by ascending distance
- Cannibalization / overlap / unique positioning logic is displayed
- Neighbor distance bar chart renders
- Distance histogram renders
- PCA embedding renders
- Task 2 artifact generation works via `python -m dashboard.test_task2`
- Product removal simulation works inside the main dashboard

## Outputs confirmed
For each dataset folder, the following files were generated/available:
- dashboard_inputs.csv
- neighbor_bar.html
- distance_hist.html
- pca_embedding.html

## Sanity-check findings
- Similar products are mapped to lower distances
- More differentiated products have larger distances
- In the simulation, removed products are matched to the closest remaining substitute
- Example: removing Apple iPhone 11 returned Apple iPhone 11 (128GB) as closest substitute with a low distance