# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Mojib Wali.
# Copyright (C) 2020-2024 Graz University of Technology.
#
# invenio-config-iform is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from flask import Flask
import pytest

from invenio_config_iform import InvenioConfigIform


@pytest.fixture(scope="module")
def create_app(instance_path: str) -> Flask:
    """Application factory fixture."""

    def factory(**config: str) -> Flask:
        app = Flask("testapp", instance_path=instance_path)
        app.config.update(**config)
        InvenioConfigIform(app)
        return app

    return factory
