#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Chris Marquardt <chris.marquardt2@vzw.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Create C&D configuration or append
# Need: dbname, tablename, colnames, datafile, uid, pwd
#

from __future__ import absolute_import, division, print_function
__metaclass = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: omnisci
version_added: "1.0"
short_description: This is my test omnisci module

description:
    - "This is my longer description explaining my test module"

options:
    platform:
        description:
            - This is the message to send to the test module
        required: true
    group:
        description:
            - Control to demo if the result of this module is changed or not
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - chris.marquardt2@vzw.com
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  omnisci:
    platform: spc
    group: nrb

# pass in a message and have changed true
- name: Test with a message and changed output
  omnisci:
    platform: spc
    group: nrb
    new: true

# fail the module
- name: Test failure of the module
  omnisci:
    platform: spc
    group: spg
'''

RETURN = '''
entered_platform:
    description: The entered platform param that was passed in
    type: str
    returned: always
entered_group_value:
    description: The entered group param that was passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

import traceback

from ansible.module_utils.basic import AnsibleModule

# The OmnisciModule object
module = None


class AnsibleModuleError(Exception):
    def __inti__(self, results):
        self.results = results


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        platform=dict(type='str', required=True),
        group=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        entered_platform_value='',
        entered_group_value='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['entered_platform_value'] = module.params['platform']
    result['message'] = 'goodbye'

    result['entered_group_value'] = module.params['group']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['new']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    platforms = ['simota','spc']
    if module.params['platform'] not in platforms:
        module.fail_json(msg='Invalid platform was entered', **result)

    groups = ['devif','nrb','rdcs','wifi']
    if module.params['group'] not in groups:
        module.fail_json(msg='Invalid group was entered', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

