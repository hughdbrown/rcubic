from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(name = 'RCubic',
      version = '1.0',
      description = 'RCubic',
      # Required packages
      requires = ['MiniREST', 'lxml', 'simplejson'],
      # List what we provide and obolete for updates
      provides = ['RCubic'],
      obsoletes = ['RCubic'],
      # Main packages
      packages = ['RCubic'],
      # Command line scripts
      scripts = [
          'rcubic', 'rcubic-cli', 'rcubic-checkin',
          ],
      # Config files
      data_files = [
          ('RCubic/', [ "RCubic/rcubic.xml.template" ]),
          ('RCubic/web/', [ "RCubic/web/index.html" ]),
          ('RCubic/web/css/', [
            "RCubic/web/css/jquery.qtip.min.css" ]),
          ('RCubic/web/css/syntax/', [
            "RCubic/web/css/syntax/shCore.css",
            "RCubic/web/css/syntax/shCoreFadeToGrey.css"]),
          ('RCubic/web/js/', [
            "RCubic/web/js/jquery.min.js",
            "RCubic/web/js/jquery.ui.min.js",
            "RCubic/web/js/jquery.qtip.min.js"]),
          ('RCubic/web/js/syntax/', [
            "RCubic/web/js/syntax/shCore.js",
            "RCubic/web/js/syntax/shBrushBash.js"]),
          ('RCubic/web/css/vader/', [
            "RCubic/web/css/vader/jquery-ui-1.8.21.custom.css" ]),
          ('RCubic/web/css/vader/images/', [
            "RCubic/web/css/vader/images/ui-bg_glass_95_fef1ec_1x400.png",
            "RCubic/web/css/vader/images/ui-icons_aaaaaa_256x240.png",
            "RCubic/web/css/vader/images/ui-icons_cccccc_256x240.png",
            "RCubic/web/css/vader/images/ui-icons_bbbbbb_256x240.png",
            "RCubic/web/css/vader/images/ui-bg_flat_0_aaaaaa_40x100.png",
            "RCubic/web/css/vader/images/ui-bg_inset-soft_15_121212_1x100.png",
            "RCubic/web/css/vader/images/ui-bg_highlight-hard_15_888888_1x100.png",
            "RCubic/web/css/vader/images/ui-icons_c98000_256x240.png",
            "RCubic/web/css/vader/images/ui-icons_666666_256x240.png",
            "RCubic/web/css/vader/images/ui-icons_f29a00_256x240.png",
            "RCubic/web/css/vader/images/ui-bg_highlight-soft_35_adadad_1x100.png",
            "RCubic/web/css/vader/images/ui-bg_highlight-soft_60_dddddd_1x100.png",
            "RCubic/web/css/vader/images/ui-icons_cd0a0a_256x240.png",
            "RCubic/web/css/vader/images/ui-bg_gloss-wave_16_121212_500x100.png",
            "RCubic/web/css/vader/images/ui-bg_highlight-hard_55_555555_1x100.png"]),
        ]
    )
