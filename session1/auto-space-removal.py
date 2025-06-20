filename = input("Enter the name of the .txt file: ").strip()

with open(filename, 'r') as f:
    lines = f.readlines()

cleaned = [line.strip() for line in lines if line.strip()]

with open(filename, 'w') as f:
    f.write('\n'.join(cleaned))

print(f"File '{filename}' cleaned successfully.")

