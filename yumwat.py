from yum.plugins import TYPE_INTERACTIVE

requires_api_version = '2.6'
plugin_type = (TYPE_INTERACTIVE, )


def config_hook(conduit):
    # Add a command line option to yum, --nowat, which,
    # if specified, will cause yumwat to restrain itself
    # from printing package descriptions.
    parser = conduit.getOptParser()
    parser.add_option('', '--nowat', dest='nowat',
            action='store_true', default=False,
            help="don't print package description via yumwat")

    # Add a command line option to yum, --wat, which,
    # if specified, will cause yumwat to print package
    # descriptions, even if the timid option turned on.
    parser.add_option('', '--wat', dest='wat',
            action='store_true', default=False,
            help="print yumwat package info even if set to timid")

def postresolve_hook(conduit):
    opts, args = conduit.getCmdLine()
    timid = conduit.confString('main', 'timid', default='0')
    ts = conduit.getTsInfo()

    sep = '-' * 10
    main_sep = '=' * 10

    if (opts and not opts.nowat and not timid) or (timid and opts and opts.wat):
        conduit.info(2, "\nYUMWAT\n" + main_sep)
        conduit.info(2, sep)
        for tsmem in ts.getMembers():
            output = tsmem.po.name + "\n" + tsmem.po.description + "\n" + sep
            conduit.info(2, output)
        conduit.info(2, "END YUMWAT\n" + main_sep)

if __name__ == "__main__":
    import sys, argparse
    if sys.version_info < (3, 0):
        import ConfigParser as configparser
    else:
        import configparser
    parser = argparse.ArgumentParser(description="don't wat when you yum")
    subs = parser.add_subparsers(dest='enable')
    subs.add_parser('enable'); subs.add_parser('disable')
    args = parser.parse_args()
    config = configparser.ConfigParser()
    with open('yumwat.conf', 'r') as conf_file:
        config.readfp(conf_file)
    if 'main' not in config.sections():
        config.add_section('main')
    if args.enable == 'enable':
        config.set('main', 'enabled', '1')
    elif args.enable == 'disable':
        config.set('main', 'enabled', '0')
    else:
        parser.error("'round these parts we enable or disable our plugins")
    with open('yumwat.conf', 'w') as conf_file:
        config.write(conf_file)
