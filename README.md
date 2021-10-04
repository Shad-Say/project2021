# project2021

## Concrete Compressive Strength Prediction

Concrete is one of the most important materials in Civil Engineering. Knowing the compressive strength of concrete is very important when constructing a building or a bridge. The Compressive Strength of Concrete is a highly nonlinear function of ingredients used in making it and their characteristics. Thus, using Machine Learning to predict the Strength could be useful in generating a combination of ingredients which result in high Strength.

### Dataset Description

The dataset consists of 1030 instances with 9 attributes and has no missing values. There are 8 input variables and 1 output variable. Seven input variables represent the amount of raw material (measured in kg/m³) and one represents Age (in Days). The target variable is Concrete Compressive Strength measured in (MPa — Mega Pascal). We shall explore the data to see how input features are affecting compressive strength.

### Exploratory Data Analysis

We can observe a high positive correlation between compressive Strength (CC_Strength) and Cement. this is true because strength concrete indeed increases with an increase in the amount of cement used in preparing it. Also, Age and Super Plasticizer are the other two factors influencing Compressive strength.
There are other strong correlations between the features,
A strong negative correlation between Super Plasticizer and Water.
positive correlations between Super Plasticizer and Fly Ash, Fine Aggregate.
These correlations are useful to understand the data in detail, as they give an idea about how a variable is affecting the other.

### References

- I-Cheng Yeh, “ Modeling of strength of high performance concrete using artificial neural networks,” Cement and Concrete Research, Vol. 28, №12, pp. 1797–1808 (1998).
- Ahsanul Kabir, Md Monjurul Hasan, Khasro Miah, “ Strength Prediction Model for Concrete”, ACEE Int. J. on Civil and Environmental Engineering, Vol. 2, №1, Aug 2013.
- https://archive.ics.uci.edu/ml/datasets/Concrete+Compressive+Strength
