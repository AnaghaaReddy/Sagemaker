# import subprocess
# import pandas as pd
# import argparse
# import os
# import logging
# from glob import glob

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def call_one_exe(file_path):
#     # Execute the C++ program with the CSV file path as an argument
#     p = subprocess.Popen(["./a.out", file_path], stdout=subprocess.PIPE)
#     p_out, err = p.communicate()
#     output = p_out.decode("utf-8")
#     return output.split(',')

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     args, _ = parser.parse_known_args()
#     logging.info('Received arguments: {}'.format(args))

#     # Find all CSV files in the input directory
#     files = glob('/opt/ml/processing/input/*.csv')
#     for i, f in enumerate(files):
#         try:
#             logging.info(f'Reading file: {f}')
#             # Call the C++ executable with the file path
#             predictions = call_one_exe(f)
            
#             # Save the predictions to an output CSV file
#             output_path = os.path.join('/opt/ml/processing/output', f'{i}_out.csv')
#             logging.info(f'Saving predictions to: {output_path}')
#             pd.DataFrame({'results': predictions}).to_csv(output_path, header=False, index=False)
#         except Exception as e:
#             logging.error(f'Error processing file {f}: {str(e)}')


import boto3
import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to print input and output
def print_input_output(input_path, output_path):
    try:
        # Read the input CSV
        input_data = pd.read_csv(input_path, header=None)
        logging.info(f"Input Data: \n{input_data}")
        
        # Process the data (example: sum of columns)
        output_data = input_data.sum(axis=1)  # Assuming two columns to sum
        output_data.to_csv(output_path, header=False, index=False)
        
        # Print the output
        logging.info(f"Output Data: \n{output_data}")
        
    except Exception as e:
        logging.error(f"Error processing the file: {str(e)}")

if __name__ == '__main__':
    # Paths to input and output (provided by SageMaker environment)
    input_dir = '/opt/ml/processing/input'
    output_dir = '/opt/ml/processing/output'
    
    # Get the input file (assuming there's only one file)
    input_file = os.path.join(input_dir, 'input_data.csv')
    output_file = os.path.join(output_dir, 'processed_output.csv')
    
    # Call the function to print input and output
    print_input_output(input_file, output_file)

