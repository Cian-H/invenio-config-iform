# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 Graz University of Technology.
#
# invenio-config-iform is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_config_iform import InvenioConfigIform


def test_version() -> None:
    """Test version import."""
    from invenio_config_iform import __version__

    assert __version__


def test_init() -> None:
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioConfigIform(app)
    assert "invenio-config-iform" in app.extensions

    app = Flask("testapp")
    ext = InvenioConfigIform()
    assert "invenio-config-iform" not in app.extensions
    ext.init_app(app)
    assert "invenio-config-iform" in app.extensions
