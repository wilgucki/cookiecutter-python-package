from setuptools import setup


setup(
{%- if cookiecutter.use_click.lower() == 'y' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli:main'
        ]
    }
{%- endif %}
)
