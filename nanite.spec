# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['nanite.py'],
             pathex=['/REPLACE-WITH-PATH/Project-Nanite', '/REPLACE-WITH-PATH/Project-Nanite/venv/lib/python3.9/site-packages', '/REPLACE-WITH-PATH/Project-Nanite/database', '/REPLACE-WITH-PATH/Project-Nanite/file_access', '/REPLACE-WITH-PATH/Project-Nanite/front_end', '/REPLACE-WITH-PATH/Project-Nanite'],
             binaries=[],
             datas=[
                ('nanite.icns', '.'),
                ('file_access/file_access_ui/file_access.html','./file_access/file_acces_ui'),
                ('front_end/favicon.ico', './front_end'),
                ('front_end/templates/base.html', './front_end/templates'),
                ('front_end/templates/bodyopen-nosidebar.html', './front_end/templates'),
                ('front_end/templates/bodyopen-sidebar.html', './front_end/templates'),
                ('front_end/templates/charts.html', './front_end/templates'),
                ('front_end/templates/home.html', './front_end/templates'),
                ('front_end/templates/modal.html', './front_end/templates'),
                ('front_end/templates/projects.html', './front_end/templates'),
                ('front_end/templates/sidebar-info-list.html', './front_end/templates'),
                ('front_end/templates/stats-single.html', './front_end/templates'),
                ('front_end/templates/stats.html', './front_end/templates'),
                ('front_end/templates/welcome.html', './front_end/templates'),
                ('front_end/static/css/Archivo/Archivo-Italic-VariableFont_wdth,wght.ttf', './front_end/static/css/Archivo'),
                ('front_end/static/css/Archivo/Archivo-VariableFont_wdth,wght.ttf', './front_end/static/css/Archivo'),

                ('front_end/static/css/Archivo/static/Archivo/Archivo-Black.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Bold.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Italic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Light.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Medium.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Regular.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-Thin.ttf', './front_end/static/css/Archivo/static/Archivo'),
                ('front_end/static/css/Archivo/static/Archivo/Archivo-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo'),

                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Black.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Bold.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Italic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Light.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Medium.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Regular.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-Thin.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),
                ('front_end/static/css/Archivo/static/Archivo_Condensed/Archivo_Condensed-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Condensed'),

                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Black.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Bold.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Italic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Light.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Medium.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Regular.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-Thin.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_ExtraCondensed/Archivo_ExtraCondensed-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo_ExtraCondensed'),

                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Black.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Bold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Italic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Light.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Medium.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Regular.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-Thin.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),
                ('front_end/static/css/Archivo/static/Archivo_SemiCondensed/Archivo_SemiCondensed-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiCondensed'),

                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Black.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Bold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Italic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Light.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Medium.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Regular.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-Thin.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),
                ('front_end/static/css/Archivo/static/Archivo_SemiExpanded/Archivo_SemiExpanded-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo_SemiExpanded'),

                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Black.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-BlackItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Bold.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-BoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-ExtraBold.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-ExtraBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-ExtraLight.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-ExtraLightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Italic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Light.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-LightItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Medium.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-MediumItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Regular.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-SemiBold.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-SemiBoldItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-Thin.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),
                ('front_end/static/css/Archivo/static/Archivo_Expanded/Archivo_Expanded-ThinItalic.ttf', './front_end/static/css/Archivo/static/Archivo_Expanded'),

                ('front_end/static/css/colors.css', './front_end/static/css'),
                ('front_end/static/css/colors.less', './front_end/static/css'),
                ('front_end/static/css/debug_style.css', './front_end/static/css'),
                ('front_end/static/css/explanation-on-hover.css', './front_end/static/css'),
                ('front_end/static/css/meyer-reset.css', './front_end/static/css'),
                ('front_end/static/css/proj-form.css', './front_end/static/css'),
                ('front_end/static/css/sanitize.css', './front_end/static/css'),
                ('front_end/static/css/stats-modal.css', './front_end/static/css'),
                ('front_end/static/css/style.css', './front_end/static/css'),
                ('front_end/static/css/style.less', './front_end/static/css'),
                ('front_end/static/imgs/creative_process_.svg', './front_end/static/imgs'),
                ('front_end/static/imgs/data_analysis_.svg', './front_end/static/imgs'),
                ('front_end/static/imgs/innovation_.svg', './front_end/static/imgs'),
                ('front_end/static/imgs/instruction_img.png', './front_end/static/imgs'),
                ('front_end/static/imgs/nanite-icon.svg', './front_end/static/imgs'),
                ('front_end/static/imgs/new-user.png', './front_end/static/imgs'),
                ('front_end/static/imgs/icons/add-circle.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/bell--v2.png', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/bell.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/download.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/green-tick.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/home.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/logout.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/nanite-outline-web.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/pencil.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/settings.png', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/settings.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/trash.svg', './front_end/static/imgs/icons'),
                ('front_end/static/imgs/icons/svg_work/logo-dummy_v3_web.svg', './front_end/static/imgs/icons/svg_work'),
                ('front_end/static/imgs/icons/svg_work/logo-dummy_v3.svg', './front_end/static/imgs/icons/svg_work'),
                ('front_end/static/imgs/icons/svg_work/logo-dummy.svg', './front_end/static/imgs/icons/svg_work'),
                ('front_end/static/imgs/icons/svg_work/logo-dummy_v3_web.svg', './front_end/static/imgs/icons/svg_work'),
                ('front_end/static/js/d3/d3.js', './front_end/static/js/d3'),
                ('front_end/static/js/d3/LICENSE', './front_end/static/js/d3'),
                ('front_end/static/js/body-scripts.js', './front_end/static/js'),
                ('front_end/static/js/head-scripts.js', './front_end/static/js'),
                ('front_end/static/js/project-modals.js', './front_end/static/js'),
                ('front_end/static/js/setup.js', './front_end/static/js'),
                ('front_end/static/js/stats-modal.js', './front_end/static/js'),
                ('front_end/static/js/viewport-scripts.js', './front_end/static/js')
                ],
             hiddenimports=["sqlite3"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='nanite',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
app = BUNDLE(exe,
             name='nanite.app',
             icon='./nanite.icns',
             bundle_identifier=None,
             )
