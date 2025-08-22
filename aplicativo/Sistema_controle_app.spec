# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Sistema_controle_app.py'],
    pathex=['C:\\Users\\Lucas\\Desktop\\projetos_atvs_escola_facu\\sesi_metade_2025\\finalizacao_2_tri_meia'],
    binaries=[],
    datas=[
        ('..\\database', 'database')
    ],
    hiddenimports=['sqlalchemy', 'kivy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data,
        cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Sistema_controle_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_window_redirects=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)