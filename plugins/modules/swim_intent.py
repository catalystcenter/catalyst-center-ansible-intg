#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Rishita Chowdhary, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: swim_intent
short_description: Intent module for SWIM related functions
description:
- Manage operation related to image importation, distribution, activation and tagging image as golden
- API to fetch a software image from remote file system using URL for HTTP/FTP and upload it to DNA Center.
  Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
- API to fetch a software image from local file system and upload it to DNA Center
  Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
- API to tag/untag image as golen for a given family of devices
- API to distribute a software image on a given device. Software image must be imported successfully into
  DNA Center before it can be distributed.
- API to activate a software image on a given device. Software image must be present in the device flash.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Abhishek Maheshwari (@abmahesh)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged ]
    default: merged
  config:
    description: List of details of SWIM image being managed
    type: list
    elements: dict
    required: True
    suboptions:
      importImageDetails:
        description: Details of image being imported
        type: dict
        suboptions:
          type:
            description: The source of import, supports url import or local import.
            type: str
          localImageDetails:
            description: Details of the local path of the image to be imported.
            type: dict
            suboptions:
              filePath:
                description: File absolute path.
                type: str
              isThirdParty:
                description: IsThirdParty query parameter. Third party Image check.
                type: bool
              thirdPartyApplicationType:
                description: ThirdPartyApplicationType query parameter. Third Party Application Type.
                type: str
              thirdPartyImageFamily:
                description: ThirdPartyImageFamily query parameter. Third Party image family.
                type: str
              thirdPartyVendor:
                description: ThirdPartyVendor query parameter. Third Party Vendor.
                type: str
          urlDetails:
            description: URL details for SWIM import
            type: dict
            suboptions:
              payload:
                description: Swim Import Via Url's payload.
                type: list
                elements: dict
                suboptions:
                  applicationType:
                    description: Swim Import Via Url's applicationType.
                    type: str
                  imageFamily:
                    description: Swim Import Via Url's imageFamily.
                    type: str
                  sourceURL:
                    description: Swim Import Via Url's sourceURL.
                    type: str
                  thirdParty:
                    description: ThirdParty flag.
                    type: bool
                  vendor:
                    description: Swim Import Via Url's vendor.
                    type: str
              scheduleAt:
                description: ScheduleAt query parameter. Epoch Time (The number of milli-seconds since
                  January 1 1970 UTC) at which the distribution should be scheduled (Optional).
                type: str
              scheduleDesc:
                description: ScheduleDesc query parameter. Custom Description (Optional).
                type: str
              scheduleOrigin:
                description: ScheduleOrigin query parameter. Originator of this call (Optional).
                type: str
      imageName:
        description: SWIM Image name.
        type: str
      taggingDetails:
        description: Details for tagging or untagging an image as golden
        type: dict
        suboptions:
          imageName:
            description: SWIM image name which will be tagged or untagged as golden.
            type: str
          deviceRole:
            description: Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER,
              DISTRIBUTION and CORE.
            type: str
          deviceFamilyName:
            description: Device family name
            type: str
          siteName:
            description: Site name for which SWIM image will be tagged/untagged as golden.
              If not provided, SWIM image will be mapped to global site.
            type: str
          tagging:
            description: Booelan value to tag/untag SWIM image as golden
              If True then the given image will be tagged as golden.
              If False then the given image will be un-tagged as golden.
            type: bool
      imageDistributionDetails:
        description: Details for SWIM image distribution. Device on which the image needs to distributed
          can be speciifed using any of the following parameters - deviceSerialNumber,
          deviceIPAddress, deviceHostname or deviceMacAddress.
        type: dict
        suboptions:
          imageName:
            description: SWIM image's name
            type: str
          deviceSerialNumber:
            description: Device serial number where the image needs to be distributed
            type: str
          deviceIPAddress:
            description: Device IP address where the image needs to be distributed
            type: str
          deviceHostname:
            description: Device hostname where the image needs to be distributed
            type: str
          deviceMacAddress:
            description: Device MAC address where the image needs to be distributed
            type: str
      imageActivationDetails:
        description: Details for SWIM image activation. Device on which the image needs to activated
          can be speciifed using any of the following parameters - deviceSerialNumber,
          deviceIPAddress, deviceHostname or deviceMacAddress.
        type: dict
        suboptions:
          activateLowerImageVersion:
            description: ActivateLowerImageVersion flag.
            type: bool
          deviceUpgradeMode:
            description: Swim Trigger Activation's deviceUpgradeMode.
            type: str
          distributeIfNeeded:
            description: DistributeIfNeeded flag.
            type: bool
          imageName:
            description: SWIM image's name
            type: str
          deviceSerialNumber:
            description: Device serial number where the image needs to be activated
            type: str
          deviceIPAddress:
            description: Device IP address where the image needs to be activated
            type: str
          deviceHostname:
            description: Device hostname where the image needs to be activated
            type: str
          deviceMacAddress:
            description: Device MAC address where the image needs to be activated
            type: str
          scheduleValidate:
            description: ScheduleValidate query parameter. ScheduleValidate, validates data
              before schedule (Optional).
            type: bool
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.import_software_image_via_url,
    software_image_management_swim.SoftwareImageManagementSwim.tag_as_golden_image,
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_distribution,
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_activation,

  - Paths used are
    post /dna/intent/api/v1/image/importation/source/url,
    post /dna/intent/api/v1/image/importation/golden,
    post /dna/intent/api/v1/image/distribution,
    post /dna/intent/api/v1/image/activation/device,

"""

EXAMPLES = r"""
- name: Import an image from a URL, tag it as golden and load it on device
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    config:
    - importImageDetails:
        type: string
        urlDetails:
          payload:
          - sourceURL: string
            isThirdParty: bool
            imageFamily: string
            vendor: string
            applicationType: string
          scheduleAt: string
          scheduleDesc: string
          scheduleOrigin: string
      imageName: string
      taggingDetails:
        imageName: string
        deviceRole: string
        deviceFamilyName: string
        siteName: string
        tagging: bool
      imageDistributionDetails:
        imageName: string
        deviceSerialNumber: string
      imageActivationDetails:
        scheduleValidate: bool
        activateLowerImageVersion: bool
        distributeIfNeeded: bool
        deviceSerialNumber: string
        imageName: string
"""

RETURN = r"""
#Case: SWIM image is successfully imported, tagged as golden, distributed and activated on a device
response:
  description: A dictionary with activation details as returned by the DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
                        "additionalStatusURL": String,
                        "data": String,
                        "endTime": 0,
                        "id": String,
                        "instanceTenantId": String,
                        "isError": bool,
                        "lastUpdate": 0,
                        "progress": String,
                        "rootId": String,
                        "serviceType": String,
                        "startTime": 0,
                        "version": 0
                  },
      "msg": String
    }

"""

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    log,
    get_dict_result,
)
from ansible.module_utils.basic import AnsibleModule


class DnacSwims(DnacBase):
    """Class containing member attributes for Swim intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
          - self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
          If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
          will contain the validated configuration. If it fails, 'self.status' will be 'failed',
          'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = dict(
            importImageDetails=dict(type='dict'),
            taggingDetails=dict(type='dict'),
            imageDistributionDetails=dict(type='dict'),
            imageActivationDetails=dict(type='dict'),
            imageName=dict(type=str),
        )

        # Validate swim params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def site_exists(self):
        """
        Parameters:
        - self: The reference to the class instance.
        Returns:
        - tuple: A tuple containing two values:
            - site_exists (bool): A boolean indicating whether the site exists (True) or not (False).
            - site_id (str or None): The ID of the site if it exists, or None if the site is not found.
        Description:
            This method checks the existence of a site in the DNAC. If the site is found,it sets 'site_exists' to True,
            retrieves the site's ID, and returns both values in a tuple. If the site does not exist, 'site_exists' is set
            to False, and 'site_id' is None. If an exception occurs during the site lookup, an exception is raised.
        """

        site_exists = False
        site_id = None
        response = None
        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": self.want.get('tagging_details').get('siteName')},
            )
        except Exception as e:
            self.module.fail_json(msg="Site not found")

        if response:
            log(str(response))

            site = response.get("response")
            site_id = site[0].get("id")
            site_exists = True

        return (site_exists, site_id)

    def get_image_id(self, name):
        """
        Retrieve the unique image ID based on the provided image name.
        Parameters:
            name (str): The name of the software image to search for.
        Returns:
            str: The unique image ID (UUID) corresponding to the given image name.
        Raises:
            AnsibleFailJson: If the image is not found in the response.
        Description:
            This function sends a request to Cisco DNAC to retrieve details about a software image based on its name.
            It extracts and returns the image ID if a single matching image is found. If no image or multiple
            images are found with the same name, it raises an exception.
        """

        image_response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_software_image_details',
            params={"image_name": name},
        )

        log(str(image_response))

        image_list = image_response.get("response")
        if (len(image_list) == 1):
            image_id = image_list[0].get("imageUuid")
            log("Image Id: " + str(image_id))
        else:
            error_message = "Image {0} not found".format(name)
            self.module.fail_json(msg="Image not found", response=image_response)

        return image_id

    def is_image_exist(self, name):
        """
        Retrieve the unique image ID based on the provided image name.
        Parameters:
            name (str): The name of the software image to search for.
        Returns:
            str: The unique image ID (UUID) corresponding to the given image name.
        Raises:
            AnsibleFailJson: If the image is not found in the response.
        Description:
            This function sends a request to Cisco DNAC to retrieve details about a software image based on its name.
            It extracts and returns the image ID if a single matching image is found. If no image or multiple
            images are found with the same name, it raises an exception.
        """
        image_exist = False
        image_response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_software_image_details',
            params={"image_name": name},
        )
        log(str(image_response))
        image_list = image_response.get("response")
        if (len(image_list) == 1):
            image_exist = True

        return image_exist

    def get_device_id(self, params):
        """
        Retrieve the unique device ID based on the provided parameters.
        Parameters:
            params (dict): A dictionary containing parameters to filter devices.
        Returns:
            str: The unique device ID corresponding to the filtered device.
        Raises:
            AnsibleFailJson: If the device is not found in the response.
        Description:
            This function sends a request to Cisco DNA Center to retrieve a list of devices based on the provided
            filtering parameters. If a single matching device is found, it extracts and returns the device ID. If
            no device or multiple devices match the criteria, it raises an exception.
        """

        response = self.dnac._exec(
            family="devices",
            function='get_device_list',
            params=params,
        )
        log(str(response))

        device_list = response.get("response")
        if (len(device_list) == 1):
            device_id = device_list[0].get("id")
            log("Device Id: " + str(device_id))
        else:
            self.module.fail_json(msg="Device not found", response=response)

        return device_id

    def get_device_family_identifier(self, family_name):
        """
        Retrieve and store the device family identifier based on the provided family name.
        Parameters:
            family_name (str): The name of the device family for which to retrieve the identifier.
        Returns:
            None
        Raises:
            AnsibleFailJson: If the family name is not found in the response.
        Description:
            This function sends a request to Cisco DNA Center to retrieve a list of device family identifiers.It then
            searches for a specific family name within the response and stores its associated identifier. If the family
            name is found, the identifier is stored; otherwise, an exception is raised.
        """

        have = {}
        response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_device_family_identifiers',
        )
        log(str(response))
        device_family_db = response.get("response")
        if device_family_db:
            device_family_details = get_dict_result(device_family_db, 'deviceFamily', family_name)
            if device_family_details:
                device_family_identifier = device_family_details.get("deviceFamilyIdentifier")
                have["device_family_identifier"] = device_family_identifier
                log("Family device indentifier:" + str(device_family_identifier))
            else:
                self.module.fail_json(msg="Family Device Name not found", response=[])
            self.have.update(have)

    def get_have(self):
        """
        Retrieve and store various software image and device details based on user-provided information.
        Returns:
            self: The current instance of the class with updated 'have' attributes.
        Raises:
            AnsibleFailJson: If required image or device details are not provided.
        Description:
            This function populates the 'have' dictionary with details related to software images, site information,
            device families, distribution devices, and activation devices based on user-provided data in the 'want' dictionary.
            It validates and retrieves the necessary information from Cisco DNAC to support later actions.
        """

        if self.want.get("tagging_details"):
            have = {}
            tagging_details = self.want.get("tagging_details")
            if tagging_details.get("imageName"):
                image_id = self.get_image_id(tagging_details.get("imageName"))
                have["tagging_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["tagging_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for tagging not provided", response=[])

            # check if given site exists, store siteid
            # if not then use global site
            site_name = tagging_details.get("siteName")
            if site_name:
                site_exists = False
                (site_exists, site_id) = self.site_exists()
                if site_exists:
                    have["site_id"] = site_id
                    log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))
            else:
                # For global site, use -1 as siteId
                have["site_id"] = "-1"
                log("Site Name not given by user. Using global site.")

            self.have.update(have)
            # check if given device family name exists, store indentifier value
            family_name = tagging_details.get("deviceFamilyName")
            self.get_device_family_identifier(family_name)

        if self.want.get("distribution_details"):
            have = {}
            distribution_details = self.want.get("distribution_details")
            # check if image for distributon is available
            if distribution_details.get("imageName"):
                image_id = self.get_image_id(distribution_details.get("imageName"))
                have["distribution_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["distribution_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for distribution not provided", response=[])

            device_params = dict(
                hostname=distribution_details.get("deviceHostname"),
                serial_number=distribution_details.get("deviceSerialNumber"),
                management_ip_address=distribution_details.get("deviceIPAddress"),
                mac_address=distribution_details.get("deviceMacAddress"),
            )
            device_id = self.get_device_id(device_params)
            have["distribution_device_id"] = device_id
            self.have.update(have)

        if self.want.get("activation_details"):
            have = {}
            activation_details = self.want.get("activation_details")
            # check if image for activation is available
            if activation_details.get("imageName"):
                image_id = self.get_image_id(activation_details.get("imageName"))
                have["activation_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["activation_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for activation not provided", response=[])

            device_params = dict(
                hostname=activation_details.get("deviceHostname"),
                serial_number=activation_details.get("deviceSerialNumber"),
                management_ip_address=activation_details.get("deviceIPAddress"),
                mac_address=activation_details.get("deviceMacAddress"),
            )
            device_id = self.get_device_id(device_params)
            have["activation_device_id"] = device_id
            self.have.update(have)

        return self

    def get_want(self, config):
        """
        Retrieve and store import, tagging, distribution, and activation details from playbook configuration.
        Parameters:
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.
        Description:
            This function parses the playbook configuration to extract information related to image
            import, tagging, distribution, and activation. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """

        want = {}
        if config.get("importImageDetails"):
            want["import_image"] = True
            want["import_type"] = config.get("importImageDetails").get("type").lower()
            if want["import_type"] == "url":
                want["url_import_details"] = config.get("importImageDetails").get("urlDetails")
            elif want["import_type"] == "local":
                want["local_import_details"] = config.get("importImageDetails").get("localImageDetails")
            else:
                self.module.fail_json(msg="Incorrect import type. Supported Values: local or url")

        want["tagging_details"] = config.get("taggingDetails")
        want["distribution_details"] = config.get("imageDistributionDetails")
        want["activation_details"] = config.get("imageActivationDetails")

        self.want = want
        log(str(self.want))

        return self

    def get_diff_import(self):
        """
        Check the image import type and fetch the image ID for the imported image for further use.
        Parameters:
            None
        Returns:
            self: The current instance of the class with updated 'have' attributes.
        Description:
            This function checks the type of image import (URL or local) and proceeds with the import operation accordingly.
            It then monitors the import task's progress and updates the 'result' dictionary. If the operation is successful,
            'changed' is set to True.
            Additionally, if tagging, distribution, or activation details are provided, it fetches the image ID for the
            imported image and stores it in the 'have' dictionary for later use.
        """

        if not self.want.get("import_image"):
            image_name = self.want.get("image_name")
            image_id = self.get_image_id(image_name)
            self.have["imported_image_id"] = image_id
            return self

        if self.want.get("import_type") == "url":
            image_name = self.want.get("url_import_details").get("payload")[0].get("sourceURL")

            # Code to check if image already exist in the DNAC
            name = image_name.split('/')[-1]
            image_exist = self.is_image_exist(name)
            if image_exist:
                image_id = self.get_image_id(image_name)
                self.have["imported_image_id"] = image_id
                log_msg = "Image {0} already exists in the Cisco DNA Center".format(name)
                self.result['msg'] = log_msg
                log(log_msg)
                self.result['changed'] = False
                return self

            url_import_params = dict(
                payload=self.want.get("url_import_details").get("payload"),
                schedule_at=self.want.get("url_import_details").get("scheduleAt"),
                schedule_desc=self.want.get("url_import_details").get("scheduleDesc"),
                schedule_origin=self.want.get("url_import_details").get("scheduleOrigin"),
            )
            response = self.dnac._exec(
                family="software_image_management_swim",
                function='import_software_image_via_url',
                op_modifies=True,
                params=url_import_params,
            )
        else:
            image_name = self.want.get("local_import_details").get("filePath")
            # Code to check if image already exist in the DNAC
            name = image_name.split('/')[-1]
            image_exist = self.is_image_exist(name)
            if image_exist:
                image_id = self.get_image_id(name)
                self.have["imported_image_id"] = image_id
                log_msg = "Image {0} already exists in the Cisco DNA Center".format(name)
                self.result['msg'] = log_msg
                log(log_msg)
                self.result['changed'] = False
                return self

            local_import_params = dict(
                is_third_party=self.want.get("local_import_details").get("isThirdParty"),
                third_party_vendor=self.want.get("local_import_details").get("thirdPartyVendor"),
                third_party_image_family=self.want.get("local_import_details").get("thirdPartyImageFamily"),
                third_party_application_type=self.want.get("local_import_details").get("thirdPartyApplicationType"),
                file_path=self.want.get("local_import_details").get("filePath"),
            )
            response = self.dnac._exec(
                family="software_image_management_swim",
                function='import_local_software_image',
                op_modifies=True,
                params=local_import_params,
                file_paths=[('file_path', 'file')],
            )

        log(str(response))

        task_details = {}
        task_id = response.get("response").get("taskId")
        while (True):
            task_details = self.get_task_details(task_id)
            name = image_name.split('/')[-1]
            if task_details and \
                    ("completed successfully" in task_details.get("progress").lower()):
                self.result['changed'] = True
                log_msg = "Swim Image {0} imported successfully".format(name)
                self.result['msg'] = log_msg
                log(log_msg)
                break

            if task_details and task_details.get("isError"):
                if "already exists" in task_details.get("failureReason"):
                    log_msg = "SWIM Image {0} already exists in the Cisco DNA Center".format(name)
                    self.result['msg'] = log_msg
                    log(log_msg)
                    self.result['changed'] = False
                    break
                else:
                    self.module.fail_json(msg=task_details.get("failureReason"),
                                          response=task_details)

        self.result['response'] = task_details if task_details else response

        # Fetch image_id for the imported image for further use
        image_name = image_name.split('/')[-1]
        image_id = self.get_image_id(image_name)
        self.have["imported_image_id"] = image_id

        return self

    def get_diff_tagging(self):
        """
        Tag or untag a software image as golden based on provided tagging details.
        Parameters:
            None
        Returns:
            None
        Description:
            This function tags or untags a software image as a golden image in Cisco DNAC based on the provided
            tagging details. The tagging action is determined by the value of the 'tagging' attribute
            in the 'tagging_details' dictionary.If 'tagging' is True, the image is tagged as golden, and if 'tagging'
            is False, the golden tag is removed. The function sends the appropriate request to Cisco DNAC and updates the
            task details in the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        tagging_details = self.want.get("tagging_details")
        tag_image_golden = tagging_details.get("tagging")

        if tag_image_golden:
            image_params = dict(
                imageId=self.have.get("tagging_image_id"),
                siteId=self.have.get("site_id"),
                deviceFamilyIdentifier=self.have.get("device_family_identifier"),
                deviceRole=tagging_details.get("deviceRole")
            )
            log("Image params for tagging image as golden:" + str(image_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='tag_as_golden_image',
                op_modifies=True,
                params=image_params
            )

        else:
            image_params = dict(
                image_id=self.have.get("tagging_image_id"),
                site_id=self.have.get("site_id"),
                device_family_identifier=self.have.get("device_family_identifier"),
                device_role=tagging_details.get("deviceRole")
            )
            log("Image params for un-tagging image as golden:" + str(image_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='remove_golden_tag_for_image',
                op_modifies=True,
                params=image_params
            )

        if response:
            task_details = {}
            task_id = response.get("response").get("taskId")
            task_details = self.get_task_details(task_id)
            if not task_details.get("isError"):
                self.result['changed'] = True
                self.result['msg'] = task_details.get("progress")

            self.result['response'] = task_details if task_details else response

    def get_diff_distribution(self):
        """
        Get image distribution parameters from the playbook and trigger image distribution.
        Parameters:
            None
        Returns:
            None
        Description:
            This function retrieves image distribution parameters from the playbook's 'distribution_details' and triggers
            the distribution of the specified software image to the specified device. It monitors the distribution task's
            progress and updates the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        distribution_details = self.want.get("distribution_details")
        distribution_params = dict(
            payload=[dict(
                deviceUuid=self.have.get("distribution_device_id"),
                imageUuid=self.have.get("distribution_image_id")
            )]
        )
        log("Distribution Params: " + str(distribution_params))

        response = self.dnac._exec(
            family="software_image_management_swim",
            function='trigger_software_image_distribution',
            op_modifies=True,
            params=distribution_params,
        )
        if response:
            task_details = {}
            task_id = response.get("response").get("taskId")
            while (True):
                task_details = self.get_task_details(task_id)
                if not task_details.get("isError") and \
                        ("completed successfully" in task_details.get("progress")):
                    self.result['changed'] = True
                    self.result['msg'] = "Image with Id {0} Distributed Successfully".format(self.have.get("distribution_image_id"))
                    break

                if task_details.get("isError"):
                    error_msg = "Image with Id {0} Distribution Failed".format(self.have.get("distribution_image_id"))
                    self.module.fail_json(msg=error_msg,
                                          response=task_details)

            self.result['response'] = task_details if task_details else response

    def get_diff_activation(self):
        """
        Get image activation parameters from the playbook and trigger image activation.
        Parameters:
            None
        Returns:
            None
        Description:
            This function retrieves image activation parameters from the playbook's 'activation_details' and triggers the
            activation of the specified software image on the specified device. It monitors the activation task's progress and
            updates the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        activation_details = self.want.get("activation_details")
        payload = [dict(
            activateLowerImageVersion=activation_details.get("activateLowerImageVersion"),
            deviceUpgradeMode=activation_details.get("deviceUpgradeMode"),
            distributeIfNeeded=activation_details.get("distributeIfNeeded"),
            deviceUuid=self.have.get("activation_device_id"),
            imageUuidList=[self.have.get("activation_image_id")]
        )]

        activation_params = dict(
            schedule_validate=activation_details.get("scehduleValidate"),
            payload=payload
        )
        log("Activation Params: " + str(activation_params))

        response = self.dnac._exec(
            family="software_image_management_swim",
            function='trigger_software_image_activation',
            op_modifies=True,
            params=activation_params,
        )
        task_details = {}
        task_id = response.get("response").get("taskId")
        while (True):
            task_details = self.get_task_details(task_id)
            if not task_details.get("isError") and \
                    ("completed successfully" in task_details.get("progress")):
                self.result['changed'] = True
                self.result['msg'] = "Image activated successfully"
                break

            if task_details.get("isError"):
                self.module.fail_json(msg="Image Activation Failed",
                                          response=task_details)

        self.result['response'] = task_details if task_details else response

    def get_diff_merged(self, config):
        """
        Get tagging details and then trigger distribution followed by activation if specified in the playbook.
        Parameters:
            config (dict): The configuration dictionary containing tagging, distribution, and activation details.
        Returns:
            self: The current instance of the class with updated 'result' and 'have' attributes.
        Description:
            This function checks the provided playbook configuration for tagging, distribution, and activation details. It
            then triggers these operations in sequence if the corresponding details are found in the configuration.The
            function monitors the progress of each task and updates the 'result' dictionary accordingly. If any of the
            operations are successful, 'changed' is set to True.
        """

        if config.get("taggingDetails"):
            self.get_diff_tagging()

        if config.get("imageDistributionDetails"):
            self.get_diff_distribution()

        if config.get("imageActivationDetails"):
            self.get_diff_activation()

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_swims = DnacSwims(module)
    state = dnac_swims.params.get("state")

    if state not in dnac_swims.supported_states:
        dnac_swims.status = "invalid"
        dnac_swims.msg = "State {0} is invalid".format(state)
        dnac_swims.check_return_status()

    dnac_swims.validate_input().check_return_status()
    for config in dnac_swims.validated_config:
        dnac_swims.reset_values()
        dnac_swims.get_want(config).check_return_status()
        dnac_swims.get_diff_import().check_return_status()
        dnac_swims.get_have().check_return_status()
        dnac_swims.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_swims.result)


if __name__ == '__main__':
    main()
