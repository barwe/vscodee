# 将隔离的环境保存到什么地方
VSCODE_ENV_DIR = 'D:/.vscode/env'

PRE_EXTENSIONS = {
    # base 是创建环境时必装的扩展
    'base': [
        'MS-CEINTL.vscode-language-pack-zh-hans',
        'PKief.material-icon-theme',
        'Gruntfuggly.todo-tree',
        # 多项目管理插件，这下可以把同类型的项目放在一起了
        'alefragnani.project-manager',
    ],
    # 下面是按个性化的扩展
    'vue2': [],
    'python': [
        'njpwerner.autodocstring',
        'ms-python.python',
        'ms-python.vscode-pylance',
        'ms-toolsai.jupyter-renderers',
        'ms-toolsai.jupyter',
        'ms-toolsai.jupyter-keymap'
    ],
    'vue3': [
        'stylelint.vscode-stylelint',
        'johnsoncodehk.volar',
    ]
}