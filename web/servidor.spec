# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['servidor.py'],
    pathex=['C:\\Users\\Lucas\\Desktop\\projetos_atvs_escola_facu\\sesi_metade_2025\\finalizacao_2_tri_meia\\web'],
    binaries=[],
    datas=[
        ('static', 'static'),
        ('templates', 'templates'),
        ('..\\database', 'database'),
    ],
    hiddenimports=['sqlalchemy'],  # <-- Adicione esta linha
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='servidor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_window_redirects=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)