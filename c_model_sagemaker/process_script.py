

import boto3
import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to execute C++ file and capture output
def run_cpp_executable(input_path, output_path):
    try:
        # Print input for logging
        logging.info(f"Reading Input Data from: {input_path}")

        # Read and print the content of the input file before passing to C++
        with open(input_path, 'r') as file:
            input_data = file.read()
            logging.info(f"Input Data:\n{input_data}")

        if os.path.exists('./a.out'):
            logging.info("a.out exists and is executable.")
        else:
            logging.error("a.out does not exist or is not executable.")

            
        
        # Execute the C++ executable and pass input file as argument
        result = subprocess.run(['./a.out', input_path], capture_output=True, text=True, check=True)
        
        # printing result from the execution
        logging.info(f"Result from C++ execution:\n{result.stdout}")

        # Capture and save the output from a.out
        output_data = result.stdout.strip()
        with open(output_path, 'w') as f:
            f.write(output_data)
        
        # Log the output
        logging.info(f"Output Data:\n{output_data}")
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing C++ executable: {str(e)}")
    except Exception as e:
        logging.error(f"General error processing the file: {str(e)}")

if __name__ == '__main__':
    # Paths to input and output (provided by SageMaker environment)
    input_dir = '/opt/ml/processing/input'
    output_dir = '/opt/ml/processing/output'
    
    # Specify the input and output files
    input_file = os.path.join(input_dir, 'input_data.csv')
    output_file = os.path.join(output_dir, 'processed_output.csv')
    
    # Run the C++ executable to process data and log results
    run_cpp_executable(input_file, output_file)

