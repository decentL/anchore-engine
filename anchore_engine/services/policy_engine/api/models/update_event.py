# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class UpdateEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, event_type=None, event_content=None):  # noqa: E501
        """UpdateEvent - a model defined in Swagger

        :param event_type: The event_type of this UpdateEvent.  # noqa: E501
        :type event_type: str
        :param event_content: The event_content of this UpdateEvent.  # noqa: E501
        :type event_content: object
        """
        self.swagger_types = {
            'event_type': str,
            'event_content': object
        }

        self.attribute_map = {
            'event_type': 'event_type',
            'event_content': 'event_content'
        }

        self._event_type = event_type
        self._event_content = event_content

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateEvent of this UpdateEvent.  # noqa: E501
        :rtype: UpdateEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_type(self):
        """Gets the event_type of this UpdateEvent.

        Type identifier for the event content section for parsing  # noqa: E501

        :return: The event_type of this UpdateEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this UpdateEvent.

        Type identifier for the event content section for parsing  # noqa: E501

        :param event_type: The event_type of this UpdateEvent.
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def event_content(self):
        """Gets the event_content of this UpdateEvent.


        :return: The event_content of this UpdateEvent.
        :rtype: object
        """
        return self._event_content

    @event_content.setter
    def event_content(self, event_content):
        """Sets the event_content of this UpdateEvent.


        :param event_content: The event_content of this UpdateEvent.
        :type event_content: object
        """

        self._event_content = event_content
