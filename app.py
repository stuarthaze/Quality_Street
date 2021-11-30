import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

n = st.button(value=80) # Number of examples
k = st.button(value= 10) # Number of categories
jitter=st.button.(value=0.4)
t = st.button(value=100) # Number of repetitions

p = [1/k]*k # Probabilities

Mean_vals = np.mean(results, axis=0)
X = 1 + np.ones((t,1))*np.arange(k) + jitter*np.random.rand(t, k)-0.5*jitter
Y = results + jitter*np.random.rand(t, k) - 0.5*jitter
fig = st.pyplot()
fig.scatter(X,Y)
# plt.figure(figsize=(12, 8))
# plt.scatter(X, Y, s=6, alpha=0.8)
# plt.grid()
# plt.plot(np.arange(k)+1, Mean_vals, color='black', marker='x', markersize = 15, linestyle=':', linewidth=1)
# plt.title(f'Distribution of results for n = {n} and k = {k}')
# for i in range(k):
#     plt.text(i+1, 0.1, f'{Mean_vals[i]:.1f}')

# ax = plt.gca()
# ax.set_ylim([0, np.max(Y)])
st.p