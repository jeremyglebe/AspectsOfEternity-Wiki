# Open Talents.md and read each line of the file
with open('Talents.md', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # Create a list of talents
    talents = []
    # Index counter
    index = 0
    # Loop through each line by index and process when encountering a talent
    while index < len(lines):
        # Get the current line
        line = lines[index]
        # Check if the line is a talent
        if line.startswith('##'):
            # Get the name of the talent (Everything after the ##)
            talent_name = line[2:]
            # Remove the leading and trailing whitespace
            talent_name = talent_name.strip()
            # Find the Short description of the talent, which will be the next
            # line to start with Short:
            while index < len(lines) and not lines[index].startswith('Short:'):
                index += 1
            if index < len(lines):
                # Get the short description of the talent
                talent_short = lines[index]
                # Remove the leading and trailing whitespace
                talent_short = talent_short[6:].strip()
                # Add the talent to the list
                talents.append((talent_name, talent_short))
        # Increment the index counter
        index += 1
# Print the list of talents with their short descriptions
for talent, desc in talents:
    print(f'{talent}: {desc}')
