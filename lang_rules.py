condition = [
    'if', 'start', 'condition', 'end',
    'open-block',
    'instructions...',
    'close-block',
    'else' ':optional',
    'open-block',
    'instructions...',
    'close-block',
]

looops = [
    'for', 'start', 'variable', 'condition', 'do-after-for', 'end',
    'open-block',
    'instructions...',
    'close-block',

    'while', 'start', 'condition', 'end',
    'open-block',
    'instructions...',
    'close-block',

    'do',
    'open-block',
    'instructions...',
    'close-block',
    'while', 'start', 'condition', 'end',
]
