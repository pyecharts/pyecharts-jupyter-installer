from mock import patch, MagicMock
from nose.tools import raises

from pyecharts_jupyter_installer.jupyter_install import InvalidRegistry


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
