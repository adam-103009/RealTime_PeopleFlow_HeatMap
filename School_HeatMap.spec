# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['School_HeatMap.py','Take_data.py','campus_data_monitor.py'],
             pathex=['C:\\Users\\88690\\Documents\\School_HeatMap_Dynamic_NewVersion\\CampusDataMonitor'],
             binaries=[],
             datas=[("C:\\Users\\88690\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\branca\\*.json","branca"),
             ("C:\\Users\\88690\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\branca\\templates","templates"),
             ("C:\\Users\\88690\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\folium\\templates","templates")],
             hiddenimports=['C:\\Users\\88690\\Documents\\School_HeatMap_Dynamic_NewVersion\\CampusDataMonitor'],
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
          [],
          exclude_binaries=True,
          name='School_HeatMap',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='School_HeatMap')
