{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { nixpkgs, self }:
  let inherit (nixpkgs) legacyPackages lib;
  in {
    packages = lib.mapAttrs (system: pkgs: {
      default = pkgs.python3Packages.callPackage ./package.nix { };
    }) legacyPackages;
  };
}
