"""
Write a python script to find maximum size batch code from a dictionary where 
key-values in the dictionary are batch codes and data-values are size of the batch.
"""

# creating a dictionary of batch
batch = {'B101':200, 'B102':150, 'B107':700, 'B108':620, 'B109':910, 'B103':300, 'B104':500, 'B105':450, 'B106':600, 'B110':980}

batch_code = str()

# finding max size batch code
for k,v in batch.items() :
    if v == max(batch.values()) :
        batch_code = k

# printing max size batch code
print("Batch code of maximum size batch :", batch_code)
