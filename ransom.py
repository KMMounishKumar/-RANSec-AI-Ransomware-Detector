
import os
import time

def simulate_encryption(target_dir="test_data"):
    os.makedirs(target_dir, exist_ok=True)
    for i in range(3):
        file_path = os.path.join(target_dir, f"important_doc_{i}.txt")
        with open(file_path, "w") as f:
            f.write("This file has been encrypted by fake ransomware.")
        time.sleep(1)
        print(f"[Simulate] Encrypted {file_path}")

if __name__ == '__main__':
    simulate_encryption()
