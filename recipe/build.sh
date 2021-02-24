# Need to add the openjpeg2 cflags
export CFLAGS="${CFLAGS} $(pkg-config --cflags libopenjp2)"

$PYTHON -m pip install . -vv
