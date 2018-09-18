#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ckan.common import _, ungettext
import ckan.plugins.toolkit as t
from ckan.plugins import PluginImplementations
from ckanext.faociok.models import Vocabulary, VocabularyTerm, VocabularyLabel


def _get_package_schema():
    # name - field name
    # validators - list of validator instances
    # element - type of html element (may be arbitrary)
    # label - localized field label
    # vocabulary_name - name of vocabulary in faociok.Vocabulary
    # description - field description
    # additional_module - additional ckan js module to add to element
    # autocomplete - use autocomplete module (nam
    return [
        {'name': 'fao_datatype',
         'validators': [t.get_validator('fao_datatype')],
         'element': 'select',
         'label': _("Data type"),
         'vocabulary_name': Vocabulary.VOCABULARY_DATATYPE,
         'description': _("Select data type of dataset"),
         'multiple': False,
         'additional_module': None,
         'vocabulary_filters': {},
         'is_required': True,
         },
         {'name': 'fao_m49_regions',
          'validators': [t.get_validator('fao_m49_regions')],
          'element': 'select',
          'multiple': True,
          'autocomplete': 'autocomplete',
          'label': _("M49 Regions"),
          'additional_module': 'autocomplete m49_regions',
          'vocabulary_remote': False,
          'vocabulary_name': Vocabulary.VOCABULARY_M49_REGIONS,
          'vocabulary_filters': [VocabularyTerm.depth == 1],
          'vocabulary_order_by': [VocabularyLabel.label],
          'description': _("Regions according to UN M.49 Standard"),
          'is_required': False},
         {'name': 'fao_agrovoc',
          'validators': [t.get_validator('fao_agrovoc')],
          'element': 'agrovoc',
          'multiple': True,
          'label': _("AGROVOC terms"),
          'additional_module': 'fao-autocomplete',
          'vocabulary_url': t.url_for('fao_autocomplete', _vocabulary='agrovoc'),
          'vocabulary_name': Vocabulary.VOCABULARY_AGROVOC,
          'vocabulary_filters': {},
          'vocabulary_order_by': None,
          'description': _("AGROVOC terms"),
          'is_required': False},
    ]

def get_create_package_schema():
    return dict( (i['name'], i['validators'],) for i in _get_package_schema())

def get_update_package_schema():
    return dict( (i['name'], i['validators'],) for i in _get_package_schema())

def get_show_package_schema():
    return dict( (i['name'], i['validators'],) for i in _get_package_schema())
