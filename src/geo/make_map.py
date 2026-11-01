# -*- coding: utf-8 -*-
"""Regions of France (IGN Admin Express via france-geojson, Licence ouverte) -> compact SVG paths.
Lambert conformal conic (Lambert-93 parameters, spherical), integer coordinates, relative path commands."""
import json, math, sys
SRC = sys.argv[1]; SRC_OM = sys.argv[2]; OUT = sys.argv[3]
CODE = {'11': 'idf', '24': 'cvl', '27': 'bfc', '28': 'nor', '32': 'hdf', '44': 'ges', '52': 'pdl',
        '53': 'bre', '75': 'naq', '76': 'occ', '84': 'ara', '93': 'pac', '94': 'cor', '04': 'reu'}
R = math.radians
p1, p2, p0, l0 = R(44), R(49), R(46.5), R(3)
n = math.log(math.cos(p1) / math.cos(p2)) / math.log(math.tan(math.pi/4 + p2/2) / math.tan(math.pi/4 + p1/2))
F = math.cos(p1) * math.tan(math.pi/4 + p1/2) ** n / n
rho0 = F / math.tan(math.pi/4 + p0/2) ** n
def proj(lon, lat):
    rho = F / math.tan(math.pi/4 + R(lat)/2) ** n
    t = n * (R(lon) - l0)
    return rho * math.sin(t), rho0 - rho * math.cos(t)

def rings(geom):
    polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
    return [ring for poly in polys for ring in poly]

def dp(pts, tol):
    if len(pts) < 4: return pts
    keep = [False] * len(pts); keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = pts[a]; bx, by = pts[b]
        dx, dy = bx - ax, by - ay; L = math.hypot(dx, dy) or 1e-12
        best, bi = -1, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            d = abs(dy * px - dx * py + bx * ay - by * ax) / L if L > 1e-12 else math.hypot(px - ax, py - ay)
            if d > best: best, bi = d, i
        if best > tol:
            keep[bi] = True; stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]

meta = json.load(open(SRC))
om = json.load(open(SRC_OM))
feats = [(CODE[f['properties']['code']], f['properties']['nom'], f['geometry']) for f in meta['features']]
reu = [f for f in om['features'] if f['properties']['code'] == '04'][0]

# bounds of metropole
allp = [proj(*c) for _, _, g in feats for r in rings(g) for c in r]
minx = min(p[0] for p in allp); maxx = max(p[0] for p in allp)
miny = min(p[1] for p in allp); maxy = max(p[1] for p in allp)
W = 1000.0; S = W / (maxx - minx); H = (maxy - miny) * S
PAD = 6
def to_px(p):
    return (round((p[0] - minx) * S) + PAD, round((maxy - p[1]) * S) + PAD)

def path_of(rs, xf, min_area=0.0):
    out = []
    for r in rs:
        pts = [xf(c) for c in r]
        clean = [pts[0]]
        for q in pts[1:]:
            if q != clean[-1]: clean.append(q)
        if len(clean) < 4: continue
        area = abs(sum(clean[i][0] * clean[i+1][1] - clean[i+1][0] * clean[i][1] for i in range(len(clean) - 1))) / 2
        if area < min_area: continue
        s = 'M%d %d' % clean[0]
        for i in range(1, len(clean)):
            dx, dy = clean[i][0] - clean[i-1][0], clean[i][1] - clean[i-1][1]
            s += 'l%d %d' % (dx, dy)
        out.append(s + 'z')
    return ''.join(out)

regions = {}
labels = {}
for key, nom, g in feats:
    rs = rings(g)
    regions[key] = {'nom': nom, 'd': path_of(rs, lambda c: to_px(proj(*c)), min_area=6)}
    # label: area-weighted centroid of the largest ring
    big = max(rs, key=lambda r: len(r))
    pts = [to_px(proj(*c)) for c in big]
    A = cx = cy = 0.0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i+1]
        cr = x0 * y1 - x1 * y0; A += cr; cx += (x0 + x1) * cr; cy += (y0 + y1) * cr
    A /= 2; labels[key] = [round(cx / (6 * A)), round(cy / (6 * A))]

# La Réunion: inset box bottom-left, local equirectangular projection, 1.5x the metropole scale, simplified
rr = rings(reu['geometry'])
lat0 = R(-21.1); lon0 = R(55.5)
def reu_proj(c):
    return ((R(c[0]) - lon0) * math.cos(lat0), R(c[1]))
rp = [reu_proj(c) for r in rr for c in r]
rminx = min(p[0] for p in rp); rmaxx = max(p[0] for p in rp); rminy = min(p[1] for p in rp); rmaxy = max(p[1] for p in rp)
RS = S * 1.5
BW, BH = 124, 100
BOX = [PAD + 4, int(H) + PAD - BH - 2, BW, BH]
w = (rmaxx - rminx) * RS; h = (rmaxy - rminy) * RS
def reu_px(c):
    x, y = reu_proj(c)
    return (BOX[0] + (BW - w) / 2 + (x - rminx) * RS, BOX[1] + (BH - h) / 2 + (rmaxy - y) * RS)
rr_s = [dp([reu_px(c) for c in r], 0.5) for r in rr]
regions['reu'] = {'nom': 'La Réunion', 'd': path_of(rr_s, lambda c: (int(round(c[0])), int(round(c[1]))), min_area=4)}
labels['reu'] = [BOX[0] + BW // 2, BOX[1] + BH // 2]
print('reunion px size', round(w), round(h))

vb = [0, 0, int(W) + 2 * PAD, int(math.ceil(H)) + 2 * PAD]
out = {'vb': vb, 'reuBox': BOX, 'regions': regions, 'labels': labels,
       'src': {'t': "Contours des régions : IGN Admin Express (Licence ouverte), via france-geojson", 'u': 'https://github.com/gregoiredavid/france-geojson'}}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
print('viewBox', vb, 'bytes', len(json.dumps(out, ensure_ascii=False, separators=(',', ':'))))
for k, v in regions.items(): print(k, len(v['d']), labels[k])
