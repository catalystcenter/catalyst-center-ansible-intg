#!/usr/bin/env python

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''s
---
'''

EXAMPLES = r'''
---
'''

RETURN = r'''
---
#
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.sda_auth_profile import module_definition



def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")
        
    elif state == "absent":
        dnac.exec("delete")

    elif state == "present":
        # TO DO: Code the logic necessary for determining if an object exists
        # Right now it's not possible as the DNAC instance is returning errors
        # for the /business/sda/authentication-profile endpoint
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
