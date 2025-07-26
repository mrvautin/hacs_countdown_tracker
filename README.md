# Countdown tracker

A Home Assistant HACS addon which can track multiple countdowns to important dates.

<p align="center">
  <img src="https://raw.githubusercontent.com/mrvautin/hacs_countdown_tracker/refs/heads/main/images/card_screenshot.png" height="200px" />
</p>

## Install

1. Follow the HACS guide adding a [custom repo](https://hacs.xyz/docs/faq/custom_repositories/).
2. Add this repo `https://github.com/mrvautin/hacs_countdown_tracker`
3. Go to `Settings > Devices & services`
4. Click `ADD INTEGRATION`
5. Enter `Countdown Tracker` and pick the matching integration
6. Enter the `Name` of the date you want to track - Eg: `Wedding Anniversary`
7. Enter the `Due date` of the date - Format: `YYYY-MM-DD`
8. When happy, select `SUBMIT` to create the tracker

You will now have a sensor created to track your date - `sensor.countdown_<name>`

## Adding new events

Adding new events is easy.

1. Go to `Settings > Devices & services`
2. Select `Countdown Tracker`
3. Click `ADD HUB`
4. Fill in the form as per above and click `SUBMIT`

## Removing events

Removing events is easy.

1. Go to `Settings > Devices & services`
2. Select `Countdown Tracker`
3. Find the event to remove
4. Click the 3 dots on the right of the event
5. Click `Delete` and confirm

## Card display

You can then add this to a card. Yaml for your card could look like this:

```yaml
type: entities
title: Countdowns!
entities:
  - type: attribute
    entity: sensor.countdown_wedding_anniversary
    attribute: countdown_days
    name: Wedding Anniverary
    icon: mdi:ring
  - type: attribute
    entity: sensor.countdown_christmas
    attribute: countdown_human
    name: Christmas!!
    icon: mdi:gift
```

The `attribute` of `countdown_days` will display `x days` until the due date. You will notice in the sensor you have a few attribute options:

- `countdown_days` will display `x days` until the event
- `countdown_human` will display in months/weeks/days until the even - Eg: `3 weeks, 6 days`
- `due_date` Simply the date of the event
