#!/bin/sh
# This overwrites yumwat's config file so that yumwat is disabled.
# I wrote it to easy enable and disable yumwat during development.
# Requires root privs.

# Rewrite config so plugin is enabled
printf "[main]\nenabled=0\ntimid=0" > /etc/yum/pluginconf.d/yumwat.conf
