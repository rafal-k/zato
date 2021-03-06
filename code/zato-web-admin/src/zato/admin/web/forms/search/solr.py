# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Django
from django import forms

# Zato
from zato.common import SEARCH

class CreateForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    address = forms.CharField(initial=SEARCH.SOLR.DEFAULTS.ADDRESS.value,
        widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    timeout = forms.CharField(
        initial=SEARCH.SOLR.DEFAULTS.TIMEOUT.value, widget=forms.TextInput(attrs={'class':'required', 'style':'width:15%'}))
    pool_size = forms.CharField(
        initial=SEARCH.SOLR.DEFAULTS.POOL_SIZE.value, widget=forms.TextInput(attrs={'class':'required', 'style':'width:15%'}))
    ping_path = forms.CharField(
        initial=SEARCH.SOLR.DEFAULTS.PING_PATH.value, widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    options = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%', 'class':'required'}))

class EditForm(CreateForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput())
