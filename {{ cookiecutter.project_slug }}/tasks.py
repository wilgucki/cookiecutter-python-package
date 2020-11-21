from invoke import task


@task
def clean(c):
    """Remove all artifacts"""
    clean_build(c)
    clean_pyc(c)
    clean_test(c)
    clean_docs(c)


@task
def clean_build(c):
    """Remove build artifacts including editable package"""
    c.run('rm -rf build/')
    c.run('rm -rf dist/')
    c.run('rm -rf .eggs/')
    c.run('find . -name \'*.egg-info\' -exec rm -rf {} +')
    c.run('find . -name \'*.egg\' -exec rm -f {} +')


@task
def clean_pyc(c):
    """Remove Python file artifacts"""
    c.run('find . -name \'*.pyc\' -exec rm -f {} +')
    c.run('find . -name \'*.pyo\' -exec rm -f {} +')
    c.run('find . -name \'*~\' -exec rm -f {} +')
    c.run('find . -name \'__pycache__\' -exec rm -rf {} +')


@task
def clean_test(c):
    """Remove test and coverage artifacts"""
    c.run('rm -rf .coverage')
    c.run('rm -rf .pytest_cache')


@task
def clean_docs(c):
    """Remove generated docs"""
    c.run('rm -rf docs/_build/')


@task
def lint(c):
    """Check style with flake8"""
    c.run('flake8 src tests')


@task
def test(c):
    """Run tests"""
    c.run('pytest')


@task
def coverage(c):
    """Check code coverage"""
    c.run('coverage run --source src -m pytest')
    c.run('coverage report -m')
    c.run('coverage html')


@task(clean_docs)
def docs(c):
    """Generate HTML documentation"""
    with c.cd('docs'):
        c.run('make html')
