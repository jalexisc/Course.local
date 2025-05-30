@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=docs

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
IF "%1"=="html" (
    echo Renaming _static to static...
    IF EXIST "%BUILDDIR%\_static" (
        move "%BUILDDIR%\_static" "%BUILDDIR%\static"
    ) ELSE IF EXIST "%BUILDDIR%\html\_static" (
        move "%BUILDDIR%\html\_static" "%BUILDDIR%\html\static"
    )
    echo Updating static links in HTML files...
    powershell -Command "(Get-ChildItem '%BUILDDIR%\*.html') | ForEach-Object { $content = Get-Content $_.FullName -Raw; $content = $content -replace '_static/', 'static/'; Set-Content -Path $_.FullName -Value $content }"
    IF EXIST "%BUILDDIR%\html" (
        powershell -Command "(Get-ChildItem '%BUILDDIR%\html\*.html') | ForEach-Object { $content = Get-Content $_.FullName -Raw; $content = $content -replace '_static/', 'static/'; Set-Content -Path $_.FullName -Value $content }"
    )
)
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
