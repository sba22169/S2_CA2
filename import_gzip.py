import gzip

def extract_gz_file(gz_file, output_file):
    with gzip.open(gz_file, 'rb') as file:
        gz_content = file.read()

    with open(output_file, 'wb') as output:
        output.write(gz_content)

# Example usage
gz_file = 'data.gz'  # Replace with the path to your .gz file
output_file = 'extracted_data.txt'  # Replace with the desired path for the extracted output file

extract_gz_file(gz_file, output_file)
print("File extracted and stored as", output_file)
