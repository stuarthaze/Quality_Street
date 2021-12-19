import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#---- INPUT
st.header("Input Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    n = st.number_input(label="n: total number", value=80) # Number of examples
with col2:
    k = st.number_input(label="k: number of categories", value= 10) # Number of categories
with col3:
    t = st.number_input(label="t: number of trials", value=100) # Number of repetitions


#---- MATH
p = [1/k]*k #Probabilities
results = np.zeros((t,k))
for i in range(t):
    R = np.random.multinomial(n, p)
    R.sort()
    results[i] = R

Mean_vals = np.mean(results, axis=0)

#---- PLOT
st.subheader("Plot parameters")
col1, col2, col3 = st.columns(3)
with col1:
    jitter=st.number_input(label="plot jitter", value=0.4)
with col2:
    alpha=st.number_input(label="opacity",value=0.7)
with col3:
    size=st.number_input(label="symbol size", value=7)

X = 1 + np.ones((t,1))*np.arange(k) + jitter*np.random.rand(t, k)-0.5*jitter
Y = results + jitter*np.random.rand(t, k) - 0.5*jitter

fig, ax = plt.subplots()
ax.scatter(X,Y, s=size, alpha=alpha)
ax.plot(np.arange(k)+1, Mean_vals, color='black', marker='x', markersize = 15, linestyle=':', linewidth=1)
ax.grid()
ax.set_xticks(np.arange(1,k+1))

for i in range(k):
    plt.text(i+1, 0.1, f'{Mean_vals[i]:.1f}')

ax.set_ylim([0, np.max(Y)])
ax.set_title(f'Distribution of results for n = {n} and k = {k}')
ax.set_xlabel('Category ordered by count')
ax.set_ylabel('Number of items')
st.pyplot(fig)