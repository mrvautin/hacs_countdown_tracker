from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from datetime import datetime

DOMAIN = "countdown_tracker"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback
) -> None:
    """Set up countdown sensors from config entry."""
    name = entry.data.get("name")
    due_date = entry.data.get("due_date")
    if not name or not due_date:
        return

    async_add_entities([CountdownSensor(name, due_date)])


class CountdownSensor(SensorEntity):
    def __init__(self, name: str, due_date: str) -> None:
        self._attr_name = f"Countdown: {name}"
        self._due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self._attr_unique_id = f"countdown_{name.lower().replace(' ', '_')}"
        self._attr_icon = "mdi:calendar-clock"
        self._update_countdown()

    def update(self):
        self._update_countdown()

    def _update_countdown(self):
        now = datetime.now()
        delta = self._due_date - now.date()
        days_remaining = delta.days

        weeks = days_remaining // 7
        days = days_remaining % 7

        countdown_str = f"{weeks} week{'s' if weeks != 1 else ''}, {days} day{'s' if days != 1 else ''}"

        self._attr_state = days_remaining
        self._attr_extra_state_attributes = {
            "countdown_days": str(days_remaining) + " days",
            "countdown_human": countdown_str,
            "updated": now.isoformat(),
            "due_date": self._due_date.isoformat()
        }

    @property
    def native_value(self) -> int:
        return self._attr_state

    @property
    def extra_state_attributes(self) -> dict:
        return self._attr_extra_state_attributes
