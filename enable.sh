#!/bin/sh
# This overwrites yumwat's config file so that yumwat is enabled.
# I wrote it to easy enable and disable yumwat during development.
# Probably requires root privs.

# Rewrite config so plugin is enabled
printf "[main]\nenabled=1" > /etc/yum/pluginconf.d/yumwat.conf
