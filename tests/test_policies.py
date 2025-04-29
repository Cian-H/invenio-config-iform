# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-config-iform is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Tests for permissions-policy."""

from invenio_rdm_records.services.permissions import RDMRecordPermissionPolicy

from invenio_config_iform.permissions.policies import IformRDMRecordPermissionPolicy

ALLOWED_DIFFERENCES = {
    "can_all",
    "can_authenticated",
    "can_create",
    "can_iform_authenticated",
    "can_search",
    "can_search_drafts",
    "can_view",
}


def test_policies_synced() -> None:
    """Make sure our permission-policy stays synced with invenio's."""
    iform_cans = {
        name: getattr(IformRDMRecordPermissionPolicy, name)
        for name in dir(IformRDMRecordPermissionPolicy)
        if name.startswith("can_")
    }
    rdm_cans = {
        name: getattr(RDMRecordPermissionPolicy, name)
        for name in dir(RDMRecordPermissionPolicy)
        if name.startswith("can_")
    }

    # check whether same set of `can_<action>`s`
    if extras := set(iform_cans) - set(rdm_cans) - ALLOWED_DIFFERENCES:
        msg = f"""
        I-Form's permission-policy has additional fields over invenio-rdm's:{extras}
        if this is intentional, add to ALLOWED_DIFFERENCES in test-file
        otherwise remove extraneous fields from IformRDMRecordPermissionPolicy
        """
        raise KeyError(msg)

    if missing := set(rdm_cans) - set(iform_cans):
        msg = f"""
        invenio-rdm's permission-policy has fields unhandled by I-Form's: {missing}
        if this is intentional, add to ALLOWED_DIFFERENCES
        otherwise set the corresponding fields in IformRDMRecordPermissionPolicy
        """
        raise KeyError(msg)

    # check whether same permission-generators used for same `can_<action>`
    for can_name in rdm_cans.keys() & iform_cans.keys():
        if can_name in ALLOWED_DIFFERENCES:
            continue

        iform_can = iform_cans[can_name]
        rdm_can = rdm_cans[can_name]

        # permission-Generators don't implement equality checks for their instances
        # we can however compare which types (classes) of Generators are used...
        if {type(gen) for gen in iform_can} != {type(gen) for gen in rdm_can}:
            msg = f"""
            permission-policy for `{can_name}` differs between I-Form and invenio-rdm
            if this is intentional, add to ALLOWED_DIFFERENCES in test-file
            otherwise fix IformRDMRecordPermissionPolicy
            """
            raise ValueError(msg)

    # check whether same `NEED_LABEL_TO_ACTION`
    iform_label_to_action = IformRDMRecordPermissionPolicy.NEED_LABEL_TO_ACTION
    rdm_label_to_action = RDMRecordPermissionPolicy.NEED_LABEL_TO_ACTION

    for label in iform_label_to_action.keys() & rdm_label_to_action.keys():
        if label in ALLOWED_DIFFERENCES:
            continue

        if iform_label_to_action.get(label) != rdm_label_to_action.get(label):
            msg = f"""
            invenio-rdm's NEED_LABEL_TO_ACTION differs from I-Form's in {label}
            if this is intentional, add to ALLOWED_DIFFERENCES in test-file
            otherwise fix IformRDMRecordPermissionPolicy.NEED_LABEL_TO_ACTION
            """
            raise ValueError(msg)
