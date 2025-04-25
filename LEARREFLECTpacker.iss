; MyAppInstaller.iss

[Setup]
AppName=Video Enhancer App
AppVersion=1.0
DefaultDirName={pf}\VideoEnhancer
DefaultGroupName=Video Enhancer
OutputBaseFilename=VideoEnhancerInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "dist\local_model\*"; DestDir: "{app}\local_model"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\Video Enhancer"; Filename: "{app}\app.exe"
Name: "{userdesktop}\Video Enhancer"; Filename: "{app}\app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked
