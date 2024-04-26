tokens_name = [
    ' ', '\n',
    '#', '&', '%',
    '+', '-', '*',
    '=',
    '\"', '\'',
    '\\', '|', '/',
    ',', '.', ';',
    '<', '>',
    '{', '}',
    '(', ')',
    '[', ']',
    '^', ':'
]

tokens_value = [
    "space", "new line",
    'sharp', 'ampersand', 'percent',
    'plus', 'minus', 'multiply',
    "equal",
    "quotation mark", "single quote",
    "back slash", "vertical bar", 'forward slash',
    "comma", "dot", "semicolon",
    "left angle bracket", "right angle bracket",
    "left curly brace", "right curly brace",
    "left parenthesis", "right parenthesis",
    "left square bracket", "right square bracket",
    "circumflex", "colon"
]

lexems_list = [
    ["comments", [
        "one line comment", "//",
        "open multi-line comment", "/*",
        "close multi-line comment", "*/"
    ]],
    ["preprocessor", [
        "begin preprocessor instruction", "#",
        "preprocessor include", "include", [
            "open include bracket base libs", "<", "close include bracket base libs", ">",
            "open include bracket user libs", "\"", "close include bracket user libs", "\""
        ],
        "preprocessor define", "define"
    ]],
    ["string", [
        "string open bracket", "\"", "string close bracket", "\""
    ]],
    ["code block open bracket", "{", "code block close bracket", "}"],
    ["base datatypes", [
        "char", "unsigned char", "short", "unsigned short", "int", "unsigned int", "long", "unsigned long",
        "long long", "unsigned long long", "float", "double"
    ]],
    ["language keywords", [
        ["if statement", "if"],
        ["switch statement", "switch", "into", [
            "name", "case", "into", [
                "name", "break"
            ]
        ]],
        ["cycle statement", "for", "into", [
            "name", "continue",
            "name", "break"
        ]],
        ["cycle statement", "while", "into", [
            "name", "continue",
            "name", "break"
        ]],
        ["special", "extern"],
        ["name", "namespace"],
        ["name", "class"],
        ["name", "object"],
        ["name", "sizeof"],
        ["name", "register"],
        ["name", "public"],
        ["name", "private"]
    ]],
    ["base operators", [
        "plus", "+",
        "minus", "-",
        "multiply", "*",
        "divide", "/",
        "plus and =", "+=",
        "minus and =", "-=",
        "multiply and =", "*=",
        "divide and =", "/=",
        "equal", "==",
        "more", ">",
        "more or equal", ">=",
        "less", "<",
        "less or equal", "<="
    ]]
]
