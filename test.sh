pip freeze
nosetests --with-coverage --cover-package pyecharts_jupyter_installer --cover-package tests  tests docs/source pyecharts_jupyter_installer && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
