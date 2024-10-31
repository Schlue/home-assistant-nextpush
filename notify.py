"""NextPush notification service."""

from __future__ import annotations

import http.client
from urllib.parse import urlparse

from typing import Any, cast

import logging

import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_TARGET,
    ATTR_TITLE,
    ATTR_TITLE_DEFAULT,
    PLATFORM_SCHEMA as NOTIFY_PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONF_URL
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = NOTIFY_PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_URL): vol.All(cv.url),
    }
)

def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> NextPushNotificationService | None:
    """Get the NextPush notification service."""
    return NextPushNotificationService(config.get(CONF_URL))

class NextPushNotificationService(BaseNotificationService):
    """Implement the notification service for NextPush."""

    def __init__(self, url) -> None:
        """Initialize the service."""
        self.url = url
        parse_object = urlparse(url)
        self.server = parse_object.netloc
        self.path = parse_object.path

    def send_message(self, message: str = "", **kwargs: Any) -> None:
        targets = kwargs.get(ATTR_TARGET)
        if not targets:
          _LOGGER.warning("No target")
          return
        title = kwargs.get(ATTR_TITLE, ATTR_TITLE_DEFAULT)
        text = f"{title}- {message}" if title else message
        conn = http.client.HTTPSConnection(self.server)
        conn.request("POST", url = self.path + targets[0], body=text)
        conn.getresponse()
        conn.close()
