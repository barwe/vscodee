from typing import Sequence, Union


class Column:
    def __init__(self, key: str, width: int=None, align='center') -> None:
        self.key = key
        self.width = width
        self.align = align


class SmartTable:
    def __init__(self, columns: Sequence[Union[Column, str]]) -> None:

        columnConfigs = []
        columnWidths = {}
        for column in columns:
            if isinstance(column, str):
                columnConfigs.append(Column(column))
                columnWidths[column] = 50
            else:
                columnConfigs.append(column)
                columnWidths[column['key']] = column['width']
        
        self.columns = columnConfigs
        self.columnWidths = columnWidths

        self.rows = []

    def add_row_arr(self, arr: Sequence[any]):
        self.rows.append({d[0]['key']: d[1] for i,d in enumerate(zip(self.columns, arr))})

    def add_row_obj(self, obj):
        self.rows.append(obj)

    def clear_rows(self):
        self.rows = []

    def col_text(self, k, v):
        return "{:{}}".format(v, self.columnWidths[k])

    def draw(self, show_title=True):
        cs = self.columns
        nc = len(cs)
        cw = sum([d['width'] for d in cs])
        tw = cw + nc - 1

        lines = []
        # 顶线
        # lines.append(f"┌{'─'*tw}┐")
        lines.append(f"┌{'┬'.join('─' * c['width'] for c in cs)}┐")

        if show_title:
            rows = [{c['key']: c['key'] for c in cs}]
        else:
            rows = []
        rows.extend(self.rows)

        for r in rows:
            lines.append('│' + '│'.join(self.col_text(c['key'], r[c['key']]) for c in cs) + '│')
            lines.append(f"├{'┼'.join('─' * c['width'] for c in cs)}┤")

        lines = lines[:-1]
        lines.append('└' + '┴'.join('─' * c['width'] for c in cs) + '┘')

        print('\n'.join(lines))

if __name__ == '__main__':
    st = SmartTable([
        {'key':'id','width':40},
        {'key':'desc','width':80}
    ])
    st.add_row(['wwwww', 'ssssssssssssssss'])
    st.draw(show_title=False)