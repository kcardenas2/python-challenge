#!/usr/bin/env python
# coding: utf-8

# In[42]:


import os
import csv


# In[43]:


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


# In[44]:


tot_months = 0
Net_Total = 0
Increase_ = 0
Decrease_ = 0
Month_greatest_increase = 0
month_greatest_decrease = 0
avg_change = []


# In[45]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    header = next (csvreader)
    back_row = next (csvreader)
 
 
            


# In[46]:


back_row =int(row[1])
tot_months += 1
Net_Total += int(row[1])
Month_greatest_increase = row[0]

    
for row in csvreader:

tot_months >1
Net_Total >1 (back_row)


# In[47]:


if back_row > Increase_great:
      Increase_ = ("back_row")
      Increase_
      
      
if (back_row) < Decrease_:
      Decrease_ = ("back_row")


# In[48]:


Month_change = sum(avg_change)/len(avg_change)

high= max(avg_change)
low= min(avg_change)


# In[52]:


print(f"Financial Analysis")
print(f"Total Months: {tot_months}")
print(f"Total: ${Net_Total}")
print(f"Average Change: ${Month_change}")
print(f"Greatest Increase in Profits:, {Month_greatest_increase}, (${high})")
print(f"Greatest Decrease in Profits:, {month_greatest_decrease}, ($(low))")


# In[58]:


output_file = os.path.join('budget_data_new')

with open (output_file, 'w') as csvfile:

    
    
    csvfile.write(f"Financial Analysis\n")
    csvfile.write(f"Total Months: {tot_months}\n")
    csvfile.write(f"Total: ${Net_Total}\n")
    csvfile.write(f"Average Change: ${avg_change}\n")
    csvfile.write(f"Greatest Increase in Profits:, {Month_greatest_increase}, (${high})\n")
    csvfile.write(f"Greatest Decrease in Profits:, {month_greatest_decrease}, (${low})\n")


# In[51]:





# In[ ]:




