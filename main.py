from generator import ReadmeGenerator


options = {
    'project_name': 'Test Project',
    'celery': True,
    'storage': True,
    'pytest': False,
    'https': False,
}
writer = ReadmeGenerator(**options)

with open('example_output.md', 'w') as f:
    f.write(writer.generate_content())
