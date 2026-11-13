"""Build-time helpers that derive platform metadata from app_info.py."""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import app_info  # noqa: E402


def version_tuple():
    parts = [int(p) for p in app_info.APP_VERSION.split(".")]
    return tuple((parts + [0, 0, 0, 0])[:4])


def write_windows_version_file(path):
    """Generate the PyInstaller VSVersionInfo file for the Windows exe."""
    vt = version_tuple()
    vs = ".".join(map(str, vt))
    a = app_info
    text = f'''# UTF-8
# GENERATED from app_info.py by build_meta.py - do not edit.
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={vt},
    prodvers={vt},
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', {a.APP_AUTHOR!r}),
        StringStruct(u'FileDescription', {a.APP_DESCRIPTION!r}),
        StringStruct(u'FileVersion', {vs!r}),
        StringStruct(u'InternalName', u'ProjectTester'),
        StringStruct(u'LegalCopyright', {a.APP_COPYRIGHT!r}),
        StringStruct(u'OriginalFilename', u'ProjectTester.exe'),
        StringStruct(u'ProductName', {a.APP_NAME!r}),
        StringStruct(u'ProductVersion', {vs!r}),
        StringStruct(u'Author', {a.APP_AUTHOR!r})])
      ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
