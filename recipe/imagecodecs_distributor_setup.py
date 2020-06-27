import os
import sys


def customize_build(EXTENSIONS, OPTIONS):
    """Customize build for conda-forge."""
    del EXTENSIONS['jpeg12']
    del EXTENSIONS['jpegxl']
    # del EXTENSIONS['lerc']
    # del EXTENSIONS['zfp']

    # build jpeg8 or jpeg9 against libjpeg instead of libjpeg_turbo
    OPTIONS['cythonize'] = True
    EXTENSIONS['jpeg8']['cython_compile_env']['HAVE_LIBJPEG_TURBO'] = False
    EXTENSIONS['lerc']['libraries'] = ['Lerc']

    if sys.platform == 'win32':
        library_inc = os.environ.get('LIBRARY_INC', '')
        EXTENSIONS['bz2']['libraries'] = ['bzip2']
        EXTENSIONS['jpeg2k']['include_dirs'] = [
            os.path.join(
                library_inc, 'openjpeg-' + os.environ.get('openjpeg', '2.3')
            )
        ]
        EXTENSIONS['jpegls']['libraries'] = ['charls-2-x64']
        EXTENSIONS['lz4']['libraries'] = ['liblz4']
        EXTENSIONS['lzma']['libraries'] = ['liblzma']
        EXTENSIONS['png']['libraries'] = ['libpng', 'z']
        EXTENSIONS['webp']['libraries'] = ['libwebp']
        EXTENSIONS['jpegxr']['include_dirs'] = [
            os.path.join(os.environ['LIBRARY_INC'], 'jxrlib')
        ]
        EXTENSIONS['jpegxr']['libraries'] = ['libjpegxr', 'libjxrglue']
    else:
        EXTENSIONS['jpegxr']['include_dirs'] = [
            os.path.join(os.environ['PREFIX'], 'include', 'jxrlib')
        ]
        EXTENSIONS['jpegxr']['libraries'] = ['jpegxr', 'jxrglue']
