
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv("ab_testing_data.csv")

print("A/B TESTING AND HYPOTHESIS TESTING")
print("----------------------------------")

# Calculate conversion rates
data["Conversion_Rate"] = (
    data["Conversions"] / data["Visitors"]
) * 100

# Group analysis
group_results = data.groupby("Group").agg({
    "Visitors": "sum",
    "Conversions": "sum"
})

group_results["Conversion_Rate"] = (
    group_results["Conversions"] /
    group_results["Visitors"]
) * 100

print("\nGROUP RESULTS:")
print(group_results)

# Hypothesis testing
group_A = data[data["Group"] == "A"]["Conversion_Rate"]
group_B = data[data["Group"] == "B"]["Conversion_Rate"]

t_stat, p_value = ttest_ind(group_A, group_B)

print("\nHYPOTHESIS TESTING")
print("Null Hypothesis (H0): No significant difference")
print("Alternative Hypothesis (H1): Significant difference")

print("\nT-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Result: Reject the Null Hypothesis")
    print("There is a significant difference between A and B.")
else:
    print("Result: Fail to Reject the Null Hypothesis")
    print("There is no significant difference between A and B.")

# Visualization
group_results["Conversion_Rate"].plot(
    kind="bar",
    color=["skyblue", "orange"],
    title="A/B Testing Conversion Rate Comparison"
)

plt.xlabel("Group")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("ab_testing_result.png")
plt.show()
