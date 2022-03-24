# 将隔离的环境保存到什么地方
# windows 默认 D:/.vscode/env
# linux 默认 $HOME/.vscode/env
VSCODE_ENV_DIR = None

RECOMMENDED_EXTENSIONS = {
    'base': {
        'desc': '新建隔离环境时默认且必装的扩展',
        'extensions': [
            {'id': 'MS-CEINTL.vscode-language-pack-zh-hans', 'desc': '微软官方提供的简体中文扩展'},
            {'id': 'PKief.material-icon-theme', 'desc': '资源管理器图标样式'},
            {'id': 'Gruntfuggly.todo-tree', 'desc': 'FIXME, TODO, ...'},
            {'id': 'alefragnani.project-manager', 'desc': '提供多项目管理功能，切换项目更方便'}
        ]
    },
    'python': {
        'desc': 'Python 项目推荐扩展',
        'extensions': [
            {'id': 'njpwerner.autodocstring', 'desc': '快速添加注释文档'},
            # also ms-python.vscode-pylance， ms-toolsai.jupyter
            {'id': 'ms-python.python', 'desc': '微软官方提供的扩展'}
        ]
    },
    'web': {
        'desc': 'Web 开发推荐扩展',
        'extensions': [
            {'id': 'dbaeumer.vscode-eslint', 'desc': '代码格式检查'},
            {'id': 'esbenp.prettier-vscode', 'desc': '代码格式校正'},
            {'id': 'stylelint.vscode-stylelint', 'desc': '样式代码检查'},
            {'id': 'mikestead.dotenv', 'desc': '.env 文件语法高亮'},
            {'id': 'formulahendry.auto-rename-tag', 'desc': '同时重命名开始标签和结束标签'},
            {'id': 'vincaslt.highlight-matching-tag', 'desc': '高亮配对的标签'}
        ]
    },
    'git': {
        'desc': 'Git 相关插件',
        'extensions': [
            {'id': 'eamodio.gitlens', 'desc': '快速查看每一行的提交信息'},
            {'id': 'mhutchie.git-graph', 'desc': '展示提交树'}
        ]
    }
}

PRE_EXTENSIONS = {
    # 下面是按个性化的扩展
    'vue2': [
        'octref.vetur'
    ],
    'vue3': [
        'johnsoncodehk.volar',
    ],
    # 第三方增强工具
    'ext': [
        # 流程图工具
        'hediet.vscode-drawio',
        # 脑图
        'eightHundreds.vscode-mindmap'
    ],
    'asist': [
        # 页面内快速跳转，不用切换鼠标点击
        'metaseed.MetaJump'
    ],
    'windi': [
        'voorjaar.windicss-intellisense'
    ]
}

###############################################################################
