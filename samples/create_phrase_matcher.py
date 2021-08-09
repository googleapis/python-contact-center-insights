# -*- coding: utf-8 -*-
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.contact_center_insights_v1.types import resources
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client


# [START contactcenterinsights_create_phrase_matcher_phone_or_cellphone]
def create_phrase_matcher_phone_or_cellphone(project_id: str) -> resources.PhraseMatcher:
    # Construct a parent resource.
    parent = "projects/{}/locations/us-central1".format(project_id)

    # Construct a phrase matcher that matches any of its rule groups.
    phrase_matcher = resources.PhraseMatcher()
    phrase_matcher.display_name = "PHONE_SERVICE"
    phrase_matcher.type_ = resources.PhraseMatcher.PhraseMatcherType.ANY_OF
    phrase_matcher.active = True

    # Construct a rule group to match any of the words "PHONE" or "CELLPHONE", ignoring case sensitivity.
    rule_group = resources.PhraseMatchRuleGroup()
    rule_group.type_ = resources.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ANY_OF

    for word in ["PHONE", "CELLPHONE"]:
        rule = resources.PhraseMatchRule()
        rule.query = word
        rule.config.exact_match_config = resources.ExactMatchConfig()
        rule_group.phrase_match_rules.append(rule)
    phrase_matcher.phrase_match_rule_groups.append(rule_group)

    # Call the Insights client to create a phrase matcher.
    insights_client = client.ContactCenterInsightsClient()
    phrase_matcher = insights_client.create_phrase_matcher(parent=parent, phrase_matcher=phrase_matcher)

    print("Created a phrase matcher named {}".format(phrase_matcher.name))
    return phrase_matcher


# [END contactcenterinsights_create_phrase_matcher_phone_or_cellphone]

# [START contactcenterinsights_create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery]
def create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(project_id: str) -> resources.PhraseMatcher:
    # Construct a parent resource.
    parent = "projects/{}/locations/us-central1".format(project_id)

    # Construct a phrase matcher that matches all of its rule groups.
    phrase_matcher = resources.PhraseMatcher()
    phrase_matcher.display_name = "NON_SHIPPING_PHONE_SERVICE"
    phrase_matcher.type_ = resources.PhraseMatcher.PhraseMatcherType.ALL_OF
    phrase_matcher.active = True

    # Construct a rule group to match any of the words "PHONE" or "CELLPHONE", ignoring case sensitivity.
    rule_group1 = resources.PhraseMatchRuleGroup()
    rule_group1.type_ = resources.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ANY_OF

    for word in ["PHONE", "CELLPHONE"]:
        rule = resources.PhraseMatchRule()
        rule.query = word
        rule.config.exact_match_config = resources.ExactMatchConfig()
        rule_group1.phrase_match_rules.append(rule)
    phrase_matcher.phrase_match_rule_groups.append(rule_group1)

    # Construct another rule group to not match any of the words "SHIPPING" or "DELIVERY", ignoring case sensitivity.
    rule_group2 = resources.PhraseMatchRuleGroup()
    rule_group2.type_ = resources.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ALL_OF

    for word in ["SHIPPING", "DELIVERY"]:
        rule = resources.PhraseMatchRule()
        rule.query = word
        rule.negated = True
        rule.config.exact_match_config = resources.ExactMatchConfig()
        rule_group2.phrase_match_rules.append(rule)
    phrase_matcher.phrase_match_rule_groups.append(rule_group2)

    # Call the Insights client to create a phrase matcher.
    insights_client = client.ContactCenterInsightsClient()
    phrase_matcher = insights_client.create_phrase_matcher(parent=parent, phrase_matcher=phrase_matcher)

    print("Created a phrase matcher named {}".format(phrase_matcher.name))
    return phrase_matcher

# [END contactcenterinsights_create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery]
