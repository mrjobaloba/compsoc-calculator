{ buildPythonPackage, gobject-introspection, gtk4, pygobject3, setuptools, wrapGAppsHook4 }:

buildPythonPackage {
  pname = "compsoc-calculator";
  version = "0.1.0";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = [
    wrapGAppsHook4
    gobject-introspection
    setuptools
  ];

  buildInputs = [
    gtk4
  ];

  propagatedBuildInputs = [
    pygobject3
  ];

  preFixup = ''
    makeWrapperArgs+=("''${gappsWrapperArgs[@]}")
  '';

  meta = {
    description = "A calculator program to demonstrate open source development";
    mainProgram = "ccalculator";
  };
}
