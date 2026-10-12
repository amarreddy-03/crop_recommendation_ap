from crop_data import CROP_DATA


def recommend_crops(district, season, soil, water, rainfall):
    recommendations = []

    for crop, data in CROP_DATA.items():

        score = 0

        if season in data["seasons"]:
            score += 1

        if soil in data["soil"]:
            score += 1

        if water == data["water"]:
            score += 1

        if rainfall == data["rainfall"]:
            score += 1

        if district in data["districts"]:
            score += 1

        if score >= 3:
            recommendations.append({
                "crop": crop,
                "score": score,
                "description": data["description"]
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations