import torch
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def f(x):
    return torch.pow((x-2.0),2)

def fP(x):
    return 2*x-4

x_axis_value = np.linspace(-7,9,100)

y_axis_value = f(torch.tensor(x_axis_value)).numpy()
y_axis_value_p = fP(torch.tensor(x_axis_value)).numpy()

sns.lineplot(x=x_axis_value, y=[0.0]*len(x_axis_value), label="0", color="black")
sns.lineplot(x=x_axis_value, y=y_axis_value, label='$f(x) => (x-2)^2$', color="blue")
sns.lineplot(x=x_axis_value, y=y_axis_value_p, label='$f\'(x) => 2x-4$', color="orange")
plt.show()