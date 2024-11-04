{ buildPythonPackage, tkinter, setuptools }:

buildPythonPackage {
  pname = "compsoc-calculator";
  version = "0.1.0";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = [
    setuptools
  ];

  propagatedBuildInputs = [
    tkinter
  ];

  meta = {
    description = "A calculator program to demonstrate open source development";
    mainProgram = "ccalculator";
  };
}
