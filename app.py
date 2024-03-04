import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_poisson_distribution(mu):
  """
  Plots the Poisson distribution with a given mean (mu).
  """
  x = np.arange(0, 30, 1)  # Range of x-axis (adjustable if needed)
  x_array = np.array([np.math.factorial(xx) for xx in x])
  y = np.exp(-mu) * (mu**x) / x_array  # Poisson probability mass function
  fig, ax = plt.subplots(figsize=(8, 5))
  ax.bar(x, y, color='skyblue', edgecolor='black')  # Plot bars
  ax.set_xlabel('Number of events (k)')
  ax.set_ylabel('Probability (P(k))')
  ax.set_title('Poisson Distribution (μ = {})'.format(mu))
  st.pyplot(fig)

def main():
  """
  Main function to run the Streamlit app.
  """
  st.title('Poisson Distribution Plotter')
  st.write('This app allows you to visualize a Poisson distribution and adjust its parameters.')

  mu = st.sidebar.slider('Mean (μ)', min_value=0.0, max_value=20.0, step=0.1, value=5.0)

  plot_poisson_distribution(mu)

if __name__ == '__main__':
  main()
