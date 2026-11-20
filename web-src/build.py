"""Builds www/index.html (one self-contained file) from web-src/app.html.
Usage: python3 web-src/build.py [output] [maptiler_key]"""
import base64, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nm = os.path.join(root, 'node_modules') + '/'
src = open(os.path.join(root, 'web-src/app.html')).read()
def js(p): return open(nm + p).read().replace('</script', '<\\/script')
parts = {
    '/*LEAFLET_CSS*/': open(nm + 'leaflet/dist/leaflet.css').read(),
    '/*CAPACITOR_JS*/': js('@capacitor/core/dist/capacitor.js'),
    '/*LEAFLET_JS*/': js('leaflet/dist/leaflet.js'),
    '/*PROJ4_JS*/': js('proj4/dist/proj4.js'),
    '/*SQLJS_JS*/': js('sql.js/dist/sql-wasm.js'),
    '__SQL_WASM_B64__': base64.b64encode(open(nm + 'sql.js/dist/sql-wasm.wasm', 'rb').read()).decode(),
}
for k, v in parts.items():
    assert src.count(k) == 1, k
    src = src.replace(k, v)
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'www/index.html')
key = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('MAPTILER_KEY', '')
if key: src = src.replace('__MAPTILER_KEY__', key)
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(src)
print('built', out, len(src), 'bytes', '(MapTiler key set)' if key else '(no map key: using OpenStreetMap tiles)')
