In Logistic Regression, the Coefficient tells you the direction(Positive = Churns, Negative = Stays),and the Odds Ratio tells you the magnitude(How much more likely)


In this case we have :

The "Bad Guys" (Drivers of Churn)
These features have Positive (+) coefficients and Odds Ratios >

Contract_Month-to-month (Coeff: 1.02, Odds: 2.78)

    The Story: This is the single biggest risk factor.

    Interpretation: A customer with a Month-to-month contract is nearly 2.8 times (278%) more likely to churn than the average baseline.

    Business Action: The company should try to move these people to longer contracts immediately.

MonthlyCharges (Coeff: 0.027, Odds: 1.02)

    The Story: Higher bills make people leave, but it accumulates.

    Interpretation: For every $1 increase in their monthly bill, the odds of churning go up by roughly 2.8%.

    Context: This looks small, but it adds up! If a bill increases by $50, the risk of churn doesn't just go up by 2%; it compounds significantly ($1.02^{50}$). Expensive plans are risky.

The "Good Guys" (The Protectors)

These features have Negative (-) coefficients and Odds Ratios < 1.

Contract_Two year (Coeff: -1.01, Odds: 0.36)

    Interpretation: A customer on a 2-year contract has their churn odds slashed to 0.36x. In other words, they are roughly 64% less likely to churn compared to the baseline.

    Business Action: This is your safest customer segment.

tenure (Coeff: -0.034, Odds: 0.96)

    Interpretation: For every 1 extra month a customer stays with the company, their risk of churning drops by roughly 4% ($1 - 0.96$).
    
    Context: A customer who has been there for 2 years (24 months) is significantly safer than a new customer.

The model achieved 80% accuracy. More importantly, we identified that contract type is the primary driver of churn. Customers on Month-to-month contracts are nearly 3x more likely to leave.

Recommendation: We should launch a marketing campaign offering a $10 discount to Month-to-month users if they switch to a 1-Year or 2-Year contract. This small discount will likely cost less than losing the customer entirely."

The data showed clear, linear trends (like 'Higher Costs = Higher Churn'). The Logistic Regression model captured these general trends effectively, achieving 80% accuracy.

In contrast, the Random Forest proved to be too complex for this specific dataset. It likely overfitted by memorizing the noise in the training data rather than learning the general rules, which caused its performance to drop to 76% on unseen data. 