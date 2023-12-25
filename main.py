from generator import ReadmeGenerator
from options import Options


options = {
    'project_name': 'Test Project',
    'celery': True,
    'storage': True,
    'pytest': True,
}
options = Options(**options)
writer = ReadmeGenerator(options)

with open('example_output.md', 'w') as f:
    f.write(writer.generate_content())
