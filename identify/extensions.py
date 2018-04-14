# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


EXTENSIONS = {
    'apinotes': {'text', 'apinotes'},
    'asar': {'binary', 'asar'},
    'bash': {'text', 'shell', 'bash'},
    'bat': {'text', 'batch'},
    'bmp': {'binary', 'image', 'bitmap'},
    'bz2': {'binary', 'bzip2'},
    'c': {'text', 'c'},
    'cc': {'text', 'c++'},
    'cfg': {'text'},
    'cmake': {'text', 'cmake'},
    'cnf': {'text'},
    'coffee': {'text', 'coffee'},
    'conf': {'text'},
    'cpp': {'text', 'c++'},
    'crt': {'text', 'pem'},
    'cson': {'text', 'cson'},
    'css': {'text', 'css'},
    'csv': {'text', 'csv'},
    'cxx': {'text', 'c++'},
    'def': {'text', 'def'},
    'dtd': {'text', 'dtd'},
    'ear': {'binary', 'zip', 'jar'},
    'ejs': {'text', 'ejs'},
    'eot': {'binary', 'eot'},
    'eps': {'binary', 'eps'},
    'erb': {'text', 'erb'},
    'exe': {'binary'},
    'eyaml': {'text', 'yaml'},
    'feature': {'text', 'gherkin'},
    'fish': {'text', 'fish'},
    'gemspec': {'text', 'ruby'},
    'gif': {'binary', 'image', 'gif'},
    'go': {'text', 'go'},
    'gotmpl': {'text', 'gotmpl'},
    'gradle': {'text', 'groovy'},
    'groovy': {'text', 'groovy'},
    'gyb': {'text', 'gyb'},
    'gyp': {'text', 'gyp', 'python'},
    'gypi': {'text', 'gyp', 'python'},
    'gz': {'binary', 'gzip'},
    'h': {'text', 'header', 'c', 'c++'},
    'hpp': {'text', 'header', 'c++'},
    'htm': {'text', 'html'},
    'html': {'text', 'html'},
    'hxx': {'text', 'header', 'c++'},
    'icns': {'binary', 'icns'},
    'ico': {'binary', 'icon'},
    'idl': {'text', 'idl'},
    'inc': {'text', 'inc'},
    'ini': {'text', 'ini'},
    'jade': {'text', 'jade'},
    'jar': {'binary', 'zip', 'jar'},
    'java': {'text', 'java'},
    'jenkinsfile': {'text', 'groovy'},
    'jinja': {'text', 'jinja'},
    'jinja2': {'text', 'jinja'},
    'jpeg': {'binary', 'image', 'jpeg'},
    'jpg': {'binary', 'image', 'jpeg'},
    'js': {'text', 'javascript'},
    'json': {'text', 'json'},
    'jsx': {'text', 'jsx'},
    'key': {'text', 'pem'},
    'kt': {'text', 'kotlin'},
    'less': {'text', 'less'},
    'm': {'text', 'c'},
    'manifest': {'text', 'manifest'},
    'map': {'text', 'map'},
    'markdown': {'text', 'markdown'},
    'md': {'text', 'markdown'},
    'mk': {'text', 'makefile'},
    'mm': {'text', 'c++'},
    'modulemap': {'text', 'modulemap'},
    'ngdoc': {'text', 'ngdoc'},
    'otf': {'binary', 'otf'},
    'p12': {'binary', 'p12'},
    'patch': {'text', 'diff'},
    'pdf': {'binary', 'pdf'},
    'pem': {'text', 'pem'},
    'php': {'text', 'php'},
    'php4': {'text', 'php'},
    'php5': {'text', 'php'},
    'pl': {'text', 'perl'},
    'plist': {'text', 'plist'},
    'png': {'binary', 'image', 'png'},
    'po': {'text', 'pofile'},
    'pp': {'text', 'puppet'},
    'proto': {'text', 'proto'},
    'purs': {'text', 'purescript'},
    'py': {'text', 'python'},
    'r': {'text', 'r'},
    'rb': {'text', 'ruby'},
    'rs': {'text', 'rust'},
    'rst': {'text', 'rst'},
    's': {'text', 'asm'},
    'scss': {'text', 'scss'},
    'sh': {'text', 'shell'},
    'sls': {'text', 'salt'},
    'so': {'binary'},
    'spec': {'text', 'spec'},
    'sql': {'text', 'sql'},
    'svg': {'text', 'svg'},
    'swf': {'binary', 'swf'},
    'swift': {'text', 'swift'},
    'swiftdeps': {'text', 'swiftdeps'},
    'tac': {'text', 'twisted', 'python'},
    'tar': {'binary', 'tar'},
    'tgz': {'binary', 'gzip'},
    'thrift': {'text', 'thrift'},
    'tiff': {'binary', 'image', 'tiff'},
    'toml': {'text', 'toml'},
    'tf': {'text', 'terraform'},
    'ts': {'text', 'ts'},
    'tsx': {'text', 'tsx'},
    'ttf': {'binary', 'ttf'},
    'txt': {'text', 'plain-text'},
    'vdx': {'text', 'vdx'},
    'vim': {'text', 'vim'},
    'war': {'binary', 'zip', 'jar'},
    'wav': {'binary', 'audio', 'wav'},
    'whl': {'binary', 'wheel', 'zip'},
    'woff': {'binary', 'woff'},
    'woff2': {'binary', 'woff2'},
    'wsgi': {'text', 'wsgi', 'python'},
    'xml': {'text', 'xml'},
    'xsd': {'text', 'xml', 'xsd'},
    'xsl': {'text', 'xml', 'xsl'},
    'yaml': {'text', 'yaml'},
    'yml': {'text', 'yaml'},
    'zip': {'binary', 'zip'},
    'zsh': {'text', 'shell', 'zsh'},
}

NAMES = {
    '.babelrc': {'text', 'json', 'babelrc'},
    '.bowerrc': {'text', 'json', 'bowerrc'},
    '.coveragerc': {'text', 'ini', 'coveragerc'},
    '.dockerignore': {'text', 'dockerignore'},
    '.editorconfig': {'text', 'editorconfig'},
    '.gitattributes': {'text', 'gitattributes'},
    '.gitignore': {'text', 'gitignore'},
    '.gitmodules': {'text', 'gitmodules'},
    '.jshintrc': {'text', 'json', 'jshintrc'},
    '.mailmap': {'text', 'mailmap'},
    '.npmignore': {'text', 'npmignore'},
    'AUTHORS': EXTENSIONS['txt'],
    'COPYING': EXTENSIONS['txt'],
    'Dockerfile': {'text', 'dockerfile'},
    'Gemfile': EXTENSIONS['rb'],
    'Jenkinsfile': {'text', 'groovy'},
    'LICENSE': EXTENSIONS['txt'],
    'MAINTAINERS': EXTENSIONS['txt'],
    'Makefile': EXTENSIONS['mk'],
    'NOTICE': EXTENSIONS['txt'],
    'PATENTS': EXTENSIONS['txt'],
    'README': EXTENSIONS['txt'],
    'Rakefile': EXTENSIONS['rb'],
    'setup.cfg': EXTENSIONS['ini'],
}
