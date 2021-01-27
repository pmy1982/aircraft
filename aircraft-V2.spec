# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['aircraft-V2.py'],
             pathex=['D:\\Peng Albert\\0. 工具资料和其他\\5. 学习\\python\\学习过程\\Crossin编程教室'],
             binaries=[],
             datas=[('res','res')],
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
          name='aircraft-V2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='plane.ico')
