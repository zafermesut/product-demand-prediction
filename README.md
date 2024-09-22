# Product Demand Prediction

## Introduction

In the competitive retail environment, determining the optimal price for a product during the holiday season is crucial for maximizing sales. This project aims to help a product company predict the demand for its products at different price points, enabling them to offer competitive discounts compared to other market players. 

The company provided a dataset of past sales and price changes, and the objective is to build a machine learning model that can predict the demand for products based on price fluctuations. By doing this, the company can ensure their products are priced optimally to drive higher sales during peak times, such as the holiday season.

In this project, we developed a demand prediction model using **Decision Tree Regressor**, which learns from historical price and sales data to forecast future demand. The model was deployed on **Hugging Face Spaces**, making it accessible for predictions through a web interface.

## Dataset

The dataset used for this project contains the following fields:
- `product_id`: Unique identifier for each product.
- `store_id`: Unique identifier for each store where the product was sold.
- `total_price`: The actual price at which the product was sold.
- `base_price`: The original price of the product before discounts.
- `units_sold`: The number of units sold (i.e., the demand for the product).

The dataset was sourced from [this GitHub repository](https://raw.githubusercontent.com/amankharwal/Website-data/master/demand.csv).

### Data Insights:
The dataset contains important information regarding the relationship between product prices and units sold. This can be leveraged to understand how price variations affect demand.

## Model

We employed a **Decision Tree Regressor** to model the demand prediction task. Decision trees are a non-parametric supervised learning algorithm, well-suited for regression tasks that involve learning non-linear relationships between features (in this case, price) and the target variable (units sold).

### Key Features:
- `total_price`: Represents the final price after applying discounts. This is the most crucial feature for demand prediction.
- `base_price`: Serves as a reference price that provides insights into the magnitude of discounts offered.
- `units_sold`: This is our target variable that the model aims to predict.

## Deployment

The project has been deployed on **Hugging Face Spaces**. You can access and interact with the model using the following link:

🔗 [Product Demand Prediction on Hugging Face Spaces](https://huggingface.co/spaces/zafermbilen/product-demand-prediction)

## Usage

### Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/zafermbilen/product-demand-prediction.git
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook to train the model:
    ```bash
    jupyter notebook
    ```

4. You can test the model by providing new data points in the web interface provided on Hugging Face.

## Results

The Decision Tree Regressor was able to accurately predict the demand for products based on price. By analyzing the predictions, the company can adjust their pricing strategy to optimize sales during the holiday season.

## Conclusion

This project demonstrates the application of machine learning in predicting product demand based on pricing. By leveraging a Decision Tree Regressor model, the company can make data-driven decisions on pricing strategies to maximize sales, especially during high-demand periods like the holiday season.

---

Feel free to explore the model and the predictions using the Hugging Face Spaces link above!

