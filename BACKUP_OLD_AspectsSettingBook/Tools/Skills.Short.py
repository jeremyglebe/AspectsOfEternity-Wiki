# Open Skills.md and read each line of the file
with open('Skills.md') as file:
    lines = file.readlines()
    # Skip the first two lines
    lines = lines[2:]
    # Create a list of skills
    skills = []
    for line in lines:
        # Split on the pipe character
        skill = line.split('|')
        # The skill name is the second item in the list
        skill_name = skill[1]
        # Remove the leading and trailing whitespace
        skill_name = skill_name.strip()
        # Add the skill to the list
        skills.append(skill_name)
# Print the list of skills with commas between each item
print(', '.join(skills))
