import numpy as np


def simulate_removal(df, dist_matrix, products_to_remove, threshold=None):
    if not products_to_remove:
        return {"error": "No products selected."}

    substitutes = {}
    substitute_distances = []
    gaps = []

    for product in products_to_remove:

        if product not in df.index:
            continue

        idx = df.index.get_loc(product)

        # distances from this product to all others
        distances = dist_matrix[idx]

        # exclude removed products
        candidate_indices = [
            i for i, name in enumerate(df.index)
            if name not in products_to_remove and name != product
        ]

        if not candidate_indices:
            continue

        candidate_distances = distances[candidate_indices]

        best_idx = candidate_indices[np.argmin(candidate_distances)]
        best_product = df.index[best_idx]
        best_distance = distances[best_idx]

        substitutes[product] = {
            "substitute": best_product,
            "distance": float(best_distance)
        }

        substitute_distances.append(best_distance)

        if threshold is not None and best_distance > threshold:
            gaps.append(product)

    if not substitute_distances:
        return {"error": "No substitutes found."}

    return {
        "substitutes": substitutes,
        "mean_dist": float(np.mean(substitute_distances)),
        "max_dist": float(np.max(substitute_distances)),
        "gaps": gaps
    }