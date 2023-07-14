rmdir dist /S /Q
rmdir NamingExe /S /Q
pyinstaller -F .\Naming_Main.py --noconsole
mkdir NamingExe
xcopy .\dist\Naming_Main.exe .\NamingExe\
mkdir .\NamingExe\Data
xcopy .\Data .\NamingExe\Data /e
xcopy Readme.txt .\NamingExe
rmdir dist /S /Q
del /Q Naming_Main.spec
