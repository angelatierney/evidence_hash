import hashlib 
import csv 


#input phase use SHA256 and MD5

#create the file and name desitnation file 
output_file = "evidence_file.csv" 

#name destination file (endpoint of data) (inout is the file looking into) 
file_test= "sus_file.txt"



def calculate_forensic_hashes(file_path):
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as f:
        # Read the file in chunks to avoid memory issues
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            md5_hash.update(byte_block)

    return sha256_hash.hexdigest(), md5_hash.hexdigest()

# Calculate the hashes for the specified file
sha256_result, md5_result = calculate_forensic_hashes(file_test)






