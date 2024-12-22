def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive_ratings = [rating for rating in ratings if rating in [4, 5]]
    positive_percentage = (len(positive_ratings) / len(ratings)) * 100
    return "Positive Feedback: " + str(round(positive_percentage, 2)) + "%"


ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_feedback = calculate_positive_feedback_percentage(ratings)
print(positive_feedback)
