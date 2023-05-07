{ pkgs }: {
    deps = [
        pkgs.python39Packages.conda
        pkgs.sudo
        pkgs.python39Packages.pip
        pkgs.qtile
        pkgs.cowsay
    ];
}