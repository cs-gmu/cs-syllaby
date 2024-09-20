import pandas as pd
import os

# Paths
current_directory = os.getcwd() 
excel_file_path = os.path.join(current_directory, 'SPRING 2025_GMU CS DEPARTMENT SYLLABY SUBMISSION.xlsx')
mkdocs_file_path = os.path.join(current_directory, 'docs/Markdown/spring_2025.md')
syllabi_folder_path = os.path.join(current_directory, 'Syllabi') 

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Read the existing Markdown file
file = open(mkdocs_file_path, 'r')
lines = file.readlines()
print(lines)
# Find the position to insert new entries
table_start = lines.index('|--------|-------------|----------------------------------------|--------------------|\n')
if table_start is None:
    raise ValueError('Table header line not found in the Markdown file.')# Generate new entries
else: 
    table_start += 1
new_entries = []

for index, row in df.iterrows():
    # Assume the file naming convention includes the course name
    file_link = row['File Upload (PDF)']  # Extract the file link
    file_name = file_link.split('/')[-1]  # Extract the file name from the URL
    print(file_name)
    file_path = os.path.join(syllabi_folder_path, file_name)

    if os.path.exists(file_path):
        # Prepare Markdown link for the file
        link = f"[{row['Number ']}]({file_link})"
        new_entry = f"| {link} | {row['Section(s)']} | {'Name1'} | {row['Instructor']} |\n"
        new_entries.append(new_entry)
    else:
        print(f"File not found: {file_path}")
print(new_entries)
# # Insert new entries into the Markdown file
lines[table_start:table_start] = new_entries

# Write the updated content back to the Markdown file
with open(mkdocs_file_path, 'w') as file:
    file.writelines(lines)

print("Markdown file updated successfully.")
