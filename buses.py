import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("BusesVis.csv")

# Title and description
st.title("Interactive Bus Data Visualizations")
st.write("Explore bus data with interactive features.")

# Visualization 1: Scatter Plot
st.header("1. Scatter Plot")

# Interactive Feature 1: Select X and Y Columns
x_column = st.selectbox("Select X-axis Column:", data.columns)
y_column = st.selectbox("Select Y-axis Column:", data.columns)

# Interactive Feature 2: Hue (Color) by a Categorical Column
hue_column = st.selectbox("Color by Column (Categorical):", data.select_dtypes(include="object").columns)
hue_categories = data[hue_column].unique()


# Create a scatter plot with interactivity
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=data, x=x_column, y=y_column, hue=hue_column, palette="Set1")
plt.title(f"Scatter Plot: {x_column} vs {y_column}")

# Display the scatter plot using st.pyplot() with the figure object
st.pyplot(scatter_plot.figure)

# Additional Information
st.write("This scatter plot allows you to choose X and Y columns, color-coding based on a categorical column, and adjust the size of data points.")


# Visualization 2: Histogram with Filters
st.header("2. Histogram with Filters")

# Interactive Feature 4: Select a Numeric Column for the Histogram
hist_column = st.selectbox("Choose a Numeric Column for Histogram:", data.select_dtypes(include="number").columns)

# Interactive Feature 5: Adjust the Number of Bins
num_bins = st.slider("Number of Bins:", min_value=5, max_value=50, value=20)

# Interactive Feature 6: Apply KDE (Kernel Density Estimation)
kde_enabled = st.checkbox("Enable KDE (Kernel Density Estimation)")

# Create a histogram with filters
fig, ax = plt.subplots(figsize=(10, 6))
if kde_enabled:
    sns.histplot(data=data, x=hist_column, bins=num_bins, kde=True, ax=ax)
    ax.set_title(f"Histogram with KDE: {hist_column}")
else:
    sns.histplot(data=data, x=hist_column, bins=num_bins, kde=False, ax=ax)
    ax.set_title(f"Histogram: {hist_column}")

# Display the histogram using st.pyplot() with the figure object
st.pyplot(fig)

# Additional Information
st.write("This histogram allows you to choose a numeric column, adjust the number of bins, and optionally enable Kernel Density Estimation (KDE).")

