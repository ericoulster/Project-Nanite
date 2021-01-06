# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['nanite.py'],
             pathex=['C:\\Users\\Eric\\Documents\\Data Projects\\Project-Nanite\\Project-Nanite-dev_deploy'],
             binaries=[],
             datas=[('front_end', 'front_end')],
             hiddenimports=[],
             hookspath=[],
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
          console=False )
