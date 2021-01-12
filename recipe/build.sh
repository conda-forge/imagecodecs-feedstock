# Overwrite the setup.py with ours while we patch things upstream
# Upstream likes to use crlf, which is really annoying to patch for
# hmaarrfk
# Patch included as reference
cp $RECIPE_DIR/imagecodecs_distributor_setup.py .
# Need to add the openjpeg2 cflags
export CFLAGS="${CFLAGS} $(pkg-config --cflags libopenjp2)"

# Build in parallel otherwise pypy + aarch doesn't complete in time
$PYTHON setup.py build_ext -j ${CPU_COUNT}
$PYTHON -m pip install . -vv
