#!/usr/bin/env python3
"""guard-publicacao.py — porteiro fail-closed de publicacao do arkar-wiki.

Reprova (exit 1) se, em content/:
  1. nota com publish:true SEM (status:revisado + verificado_em + fontes)
  2. link de content/ -> interno/
  3. arquivo nao-Markdown em content/
  4. PII no texto (CPF / CNPJ / JWT / chave privada)

Aviso (NAO reprova): verificado_em com mais de 180 dias.

Sem dependencias externas (stdlib only) — roda na imagem de build do Vercel.
"""
import os
import re
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

errors = []
warnings = []
notas = 0
publicaveis = 0

CPF = re.compile(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b')
CNPJ = re.compile(r'\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b')
JWT = re.compile(r'\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]+')
PKEY = re.compile(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----')
MDLINK = re.compile(r'\]\(([^)]+)\)')
WIKILINK = re.compile(r'\[\[([^\]]+)\]\]')


def split_fm(text):
    if text.startswith('---'):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.DOTALL)
        if m:
            return m.group(1), m.group(2)
    return '', text


def fm_get(fm, key):
    m = re.search(r'^%s:\s*(.*)$' % re.escape(key), fm, re.MULTILINE)
    return m.group(1).strip() if m else None


def fontes_ok(fm):
    v = fm_get(fm, 'fontes')
    if v is not None:
        v = v.strip()
        if v and v not in ('[]', 'null', '~'):
            return True
    return bool(re.search(r'^fontes:\s*\n(?:\s*-\s*.+\n?)+', fm, re.MULTILINE))


if not os.path.isdir(CONTENT):
    print("guard: content/ nao encontrado em %s" % ROOT)
    sys.exit(1)

for dirpath, dirnames, filenames in os.walk(CONTENT):
    for fn in sorted(filenames):
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        if not fn.endswith('.md'):
            errors.append("[nao-MD em content/] %s" % rel)
            continue
        notas += 1
        with open(path, encoding='utf-8') as f:
            text = f.read()
        fm, _body = split_fm(text)

        for label, rx in (('CPF', CPF), ('CNPJ', CNPJ), ('JWT', JWT), ('chave privada', PKEY)):
            if rx.search(text):
                errors.append("[PII:%s] %s" % (label, rel))

        for rx in (MDLINK, WIKILINK):
            for tgt in rx.findall(text):
                t = tgt.strip()
                if 'interno/' in t or t.startswith('interno'):
                    errors.append("[link content->interno] %s -> %s" % (rel, t))

        pub = (fm_get(fm, 'publish') or '').strip().lower() == 'true'
        if pub:
            publicaveis += 1
            status = (fm_get(fm, 'status') or '').strip()
            vem = (fm_get(fm, 'verificado_em') or '').strip()
            if status != 'revisado' or not vem or not fontes_ok(fm):
                errors.append(
                    "[publish sem revisao completa] %s (status=%r verificado_em=%r fontes_ok=%s)"
                    % (rel, status, vem, fontes_ok(fm)))

        vem = (fm_get(fm, 'verificado_em') or '').strip()
        if vem:
            try:
                d = datetime.date.fromisoformat(vem)
                if (datetime.date.today() - d).days > 180:
                    warnings.append("[verificado_em > 180d] %s (%s)" % (rel, vem))
            except ValueError:
                pass

print("arkar-wiki guard | notas em content/: %d | publicaveis: %d | erros: %d | avisos: %d"
      % (notas, publicaveis, len(errors), len(warnings)))
for w in warnings:
    print("  AVISO", w)
for e in errors:
    print("  ERRO ", e)
sys.exit(1 if errors else 0)
