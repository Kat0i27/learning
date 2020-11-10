
class Handler:
    '''
        方法callback负责根据指定的前缀（如'start_'）和名称（如'paragraph'）查找相应的方
        法。这是通过使用getattr并将默认值设置为None实现的。
        如果getattr返回的对象是可调用的，就使用额外提供的参数调用它。
        例如，调用handler.callback('start_', 'paragraph')时，将调用方法handler.start_paragraph且不提供任何参数——如果start_paragraph存在的话
    '''
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)

    def start(self, name):self.callback('start_', name)

    def end(self, name):self.callback('end_', name)

    def sub(self, name):#eg.name:emphasis
        def substitution(match):
            result = self.callback('sub_', name, match)#调用函数sub_emphasis
            if result is None: match.group(0)
            return result
        return substitution#返回一个函数，调用函数将调用函数sub_emphasis


class HTMLRenderer(Handler):
    """
    用于渲染HTML的具体处理程序
    HTMLRenderer的方法可通过超类Handler的方法start()、end()和sub()来访问。这些方法实现了HTML文档使用的基本标记
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))
    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))
    def feed(self, data):
        print(data)