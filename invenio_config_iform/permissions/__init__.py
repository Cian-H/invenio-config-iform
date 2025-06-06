# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-config-iform is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Permission-policies and roles, based on `flask-principal`."""

from .policies import IformRDMRecordPermissionPolicy

__all__ = ("IformRDMRecordPermissionPolicy",)
