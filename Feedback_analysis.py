def calculate_positive_feedback_percentage(ratings):
#Calculate the percentage of positive feedback (ratings 4 or 5)
    if not ratings:  # If no ratings are provided
        return 0.0
# Count positive feedback ratings (4 or 5)
    positive_count = sum(1 for rating in ratings if rating == 4 or rating == 5)
# Calculate the percentage of positive feedback
    percentage = (positive_count / len(ratings)) * 100

    return percentage
# Input Example
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
# Calculate the positive feedback percentage
positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
# Output the result
print(f"Positive Feedback: {positive_feedback_percentage:.2f}%")
