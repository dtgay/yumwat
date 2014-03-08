#!/bin/sh
# This script installs yumwat on Fedora 18 and 19.
# Not tested on other platforms.
# Requires root privs.

# Install config file
cp yumwat/yumwat.conf /etc/yum/pluginconf.d/

# TODO: make sure pluginpath is set in /etc/yum.conf
# ... there has to be a better way to do that.

# Install plugin
cp yumwat/yumwat.py /usr/lib/yum-plugins

# Set yum plugin directory
echo 'pluginpath=/usr/lib/yum-plugins' >> /etc/yum.conf
