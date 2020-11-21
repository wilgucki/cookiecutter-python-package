import os


if '{{ cookiecutter.use_click }}'.lower() != 'y':
    os.remove(os.path.join(os.getcwd(), 'src', '{{ cookiecutter.project_slug }}', 'cli.py'))
