# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['..\\lineToLocal.py'],
             pathex=['C:\\Users\\admin\\Desktop\\面试-ZD\\笔记全\\1.数据结构与算法每周总结\\数据结构与算法程序调试\\_0\\_9tool\\mdOnlinepictureToLocal\\exe'],
             binaries=[],
             datas=[],
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
          name='lineToLocal',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
