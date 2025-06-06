# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-config-iform is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""`RoleNeed`s for permission policies.

To use these roles, add them to the database via:
    `$ invenio roles create iform_authenticated --description "..."`
then add roles to users via:
    `$ invenio roles add user@email.com iform_authenticated`
"""

from flask_principal import RoleNeed

# using `flask_principal.RoleNeed`` instead of `invenio_access.SystemRoleNeed`,
# because these roles are assigned by an admin rather than automatically by the system
iform_authenticated_user = RoleNeed("iform_authenticated")
