# NextPush from Home-Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacs-shield]][hacs]
[![Project Maintenance][maintainer-shield]][maintainer]

[![Community Forum][forum-shield]][forum]


**This component will set up the following notifier.**



## Installation

### Precodition

1. Nextcloud server
3. Install this Nextcloud application from the store: https://apps.nextcloud.com/apps/uppush
4. App on mobile device: https://codeberg.org/NextPush/nextpush-android
5. Add notification channel 

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`)
2. If you do not have a `custom_components` directory (folder) there, you need to create it
3. In the `custom_components` directory (folder) create a new folder called `vaillant_vsmart`
4. Download _all_ the files from this directory (folder) in this repository
5. Place the files you downloaded in the new directory (folder) you created
6. Restart Home Assistant

## Configuration

configuration.yaml
notify:
  - name: "NextPush"
    platform: nextpush
    url: "https://nextcloud.domain.tld/index.php/apps/uppush/push/"

action:
    - action: notify.nextpush
      metadata: {}
      data:
        target: <the notificaton channel ID>
        title: Door
        message: was closed


[maintainer]: https://github.com/Schlue
