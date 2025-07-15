# car-sales-dashboard

This project is a web application dashboard built with Streamlit to analyze a dataset of car sales advertisements. Users can explore the data through various visualizations and interactive filters.

## Features

- Displays the distribution of car conditions through a histogram.
- Shows the relationship between odometer readings and price with a scatter plot.
- Allows users to filter the data by price range using an interactive slider.
- Provides an option to break down the scatter plot by vehicle type using a checkbox.

## Technologies Used

- Python
- Pandas
- Plotly Express
- Streamlit

## How to Launch Locally

To run this project on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nyein-V/car-sales-dashboard.git
    cd car-sales-dashboard
    ```
    *(Note: Replace with your actual GitHub username.)*

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
The application should now be running in your web browser.