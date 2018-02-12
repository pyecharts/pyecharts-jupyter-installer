import os
import sys
from mock import patch, MagicMock
from nose.tools import raises, eq_

from pyecharts_jupyter_installer.jupyter_install import InvalidRegistry

PY2 = sys.version_info[0] == 2

if PY2:
    from StringIO import StringIO
else:
    from io import StringIO


@patch('pyecharts_jupyter_installer.jupyter_install._install')
@patch('pyecharts_jupyter_installer.jupyter_install.install.run')
def test_install_cmd_for(fake_run, fake_install):
    from pyecharts_jupyter_installer.jupyter_install import install_cmd_for
    from distutils.dist import Distribution
    cmd_dict = install_cmd_for("abc", "def")
    install_class = cmd_dict['install']
    installer = install_class(Distribution())
    installer.run()
    fake_install.assert_called_with("abc", "def")


@patch('pyecharts_jupyter_installer.jupyter_install.__get_jupyter_note_utils')
@patch('warnings.warn')
def test_jupyter_install(fake_warn, fake_jupyter):
    fake_jupyter.return_value = (None, None)
    from pyecharts_jupyter_installer.jupyter_install import _jupyter_install
    _jupyter_install('abc', 'abc', 'abc')
    fake_warn.assert_called()


@patch('pyecharts_jupyter_installer.jupyter_install.__get_jupyter_note_utils')
def test_jupyter_install_with_jupyter_present(fake_jupyter):
    install_nbextension = MagicMock()
    ConfigManager = MagicMock()
    fake_jupyter.return_value = (install_nbextension, ConfigManager)
    from pyecharts_jupyter_installer.jupyter_install import _jupyter_install
    _jupyter_install('abc', 'abc', 'abc')
    install_nbextension.assert_called()


def test_get_jupyter_note_utils():
    import pyecharts_jupyter_installer.jupyter_install as test
    test.__get_jupyter_note_utils()


@raises(InvalidRegistry)
def test_validate_registry():
    from pyecharts_jupyter_installer.jupyter_install import _validate_registry
    __test_registry__ = {
        'FILE_MAP': None
    }
    _validate_registry(__test_registry__)


def test_load_registry_json():
    import pyecharts_jupyter_installer.jupyter_install as test
    content = test._load_registry_json(os.path.join(
        "tests", "fixtures", "fake_registry.json"))
    eq_(content, {"test": "ok"})


@patch('pyecharts_jupyter_installer.jupyter_install._load_registry_json')
@patch('pyecharts_jupyter_installer.jupyter_install._validate_registry')
@patch('pyecharts_jupyter_installer.jupyter_install._jupyter_install')
def test_install_function(fake_a, fake_b, fake_c):
    import pyecharts_jupyter_installer.jupyter_install as test
    test._install('test', 'is mocked')
    fake_c.assert_called()


@patch('sys.stdout', new_callable=StringIO)
@patch('pyecharts_jupyter_installer.jupyter_install._load_registry_json')
@patch('pyecharts_jupyter_installer.jupyter_install._validate_registry')
def test_install_function_failed(fake_validate_registry, fake_b, stdout):
    fake_validate_registry.side_effect = InvalidRegistry
    import pyecharts_jupyter_installer.jupyter_install as test
    test._install('test', 'is mocked')
    assert "Invalid registry:" in stdout.getvalue()
