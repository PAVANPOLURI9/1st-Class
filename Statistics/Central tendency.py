from statistics import mean, median, mode

# Sample survey responses (Scale: 1 = Strongly Disagree, 5 = Strongly Agree)
survey_responses = [3, 4, 5, 3, 4, 4, 5, 2, 3, 4, 3, 4, 5, 4, 3, 5, 2, 3, 4, 5]

# Calculate central tendency measures
mean_value = mean(survey_responses)
median_value = median(survey_responses)
mode_value = mode(survey_responses)

# Determine overall sentiment
if mean_value >= 4.5:
    sentiment = "Strongly Agree"
elif mean_value >= 3.5:
    sentiment = "Agree"
elif mean_value >= 2.5:
    sentiment = "Neutral"
elif mean_value >= 1.5:
    sentiment = "Disagree"
else:
    sentiment = "Strongly Disagree"

# Display results
print("Survey Results Analysis on New Technology Thoughts:")
print(f"Mean (Average Opinion): {mean_value:.2f}")
print(f"Median (Middle Opinion): {median_value}")
print(f"Mode (Most Common Opinion): {mode_value}")
print(f"Overall Sentiment: {sentiment}")
