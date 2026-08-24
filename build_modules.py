import os
import base64

def write_file(rel_path, content):
    full_path = os.path.join(r'C:\Users\harsh\.gemini\antigravity\scratch\sales-dashboard', rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote: {rel_path}')

print('Script template ready')
