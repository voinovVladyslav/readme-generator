from generator import ReadmeGenerator
from menu import Menu



menu = Menu()
menu.prompt_options()
writer = ReadmeGenerator(menu.get_options())

with open('output.md', 'w') as f:
    f.write(writer.generate_content())
