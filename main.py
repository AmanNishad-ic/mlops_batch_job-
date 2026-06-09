import pandas as pd
import numpy as np
import random
import yaml
import logging
import json

# config setup
with open('config.yaml','r') as file:
    config = yaml.safe_load(file)
    

seed = config['seed']
random.seed(seed)
np.random.seed(seed)

# logging setup
logging.basicConfig(
    filename = config['log_file'],
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# log massage
logging.info("Batch job started")

# csv file setup
df = pd.read_csv(config['input_file'])
df['price_change'] = df['close'] - df['open']
df["price_range"] = df['high'] - df['low']
df['direction'] = np.where(df['close']>df['open'],'UP','DOWN')
df.to_csv(config['output_file'],index=False)
logging.info('Processed File Seved Successfully')

# Metric Dictionary setup

metric = {
    'row_processed' : len(df),
    'avg_price_change' : float(df['price_change'].mean()),
    'up_candels' : int((df['direction']== 'UP').sum()),
    'down_candel' : int((df['direction']=='DOWN').sum())
}

# save metric

with open(config['metrics_file'] ,'w') as file:
    json.dump(metric,file,indent=4)
logging.info("Metric file genearted")

# log massage
logging.info(f'Data loaded successfully . Row = {len(df)}')
logging.info('Program Finished')
print('Program Run successfully')
