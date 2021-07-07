#!/usr/bin/env python
# coding: utf-8

# In[42]:


import os
import csv


# In[43]:


csvpath = os.path.join('election_data.csv')


# In[44]:


total_votes = 0 


# In[45]:


Khan_ = 0
Otooley_ = 0
Correy_ = 0
Li_ = 0


# In[71]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    header = next (csvreader)
    
    for row in csvreader:
        total_votes = total_votes =+ 1
        
        candidate_name = row[2]
        
        county_name = row[1]
        
        
    if (candidate_name == "Khan"):
        Khan_ =+1
        
    if (candidate_name == "Otooley"):
        Otooley_ =+1
    if (candidate_name == "Correy"):
        Correy_ =+1
    
    else: 
        Li_ =+ 1
        
        
        
        


# In[72]:


winning_percentage = 0
Percent_Khan = Khan_/total_votes
Percent_Li = Li_/total_votes
Percent_Coorey = Correy_/total_votes
Percent_Otooley = Otooley_/total_votes
        


# In[73]:


winner = max(candidate_name) 
if winner == Khan_:
        winner_name = "Khan"
if winner == Otooley_:
        winner_name = "Otooley"
if winner == Correy_:
        winner_name = "Correy"
else:
        winner_name = "Li_"
  
        
        


# In[74]:


print(f"Election Results")
print(f"Total Votes : {total_votes}")
print(f"Khan: {Percent_Khan:.3%}({Khan_})")
print(f"Correy: {Percent_Coorey:.3%}({Correy_})")
print(f"Otooley: {Percent_Otooley:.3%}({Otooley_})")
print(f"Li: {Percent_Li:.3%}({ Li_ })")
print(f"Winner: {winner_name }")


# In[78]:


output_file = os.path.join('election_data_revised.text')


# In[81]:


with open(output_file, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"Total Votes : {total_votes}\n")
    txtfile.write(f"Khan: {Percent_Khan:.3%}({Khan_})\n")
    txtfile.write(f"Correy: {Percent_Coorey:.3%}({Correy_})\n")
    txtfile.write(f"Otooley: {Percent_Otooley:.3%}({Otooley_})\n")
    txtfile.write(f"Li: {Percent_Li:.3%}({ Li_ })\n")
    txtfile.write(f"Winner: {winner_name }\n")


# In[ ]:




