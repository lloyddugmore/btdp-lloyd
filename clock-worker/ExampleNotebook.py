# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # This is a Title
#
# This is a note.

# %%
import pandas as pd
from doers.adder import Adder

# %%
top_level_param = 'some value'

# %%
important_data = list(top_level_param)
important_df = pd.DataFrame(important_data)
important_df.head()

# %%
adder = Adder()
total = adder.add_something(2)
total

# %%
