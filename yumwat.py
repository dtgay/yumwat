from yum.plugins import TYPE_INTERACTIVE

requires_api_version = '2.6'
plugin_type = (TYPE_INTERACTIVE, )


def config_hook(conduit):
    """Add a command line option to yum, --nowat, which,
    if specified, will cause yumwat to restrain itself
    from printing package descriptions."""
    parser = conduit.getOptParser()
    parser.add_option('', '--nowat', dest='nowat',
            action='store_true', default=False,
            help="don't print package description via yumwat")


def predownload_hook(conduit):
    for package in conduit.getDownloadPackages():
        print package
