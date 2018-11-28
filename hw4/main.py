import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>JS九九乘法表</title>
<meta name="keywords" content="JS,JavaScript,九九乘法表" />
<meta name="decoration" content="《 JavaScript 面向对象编程指南 》课后作业，九九乘法表" />
</head>

<body>
<h1>九九乘法表</h1>
<script type="text/javascript">
for(var i=1;i<=9;i++){
    for(var j=1;j<=i;j++){
        document.write(j+"*"+i+"="+i*j+"&nbsp;&nbsp;&nbsp;&nbsp;");
    }
    document.write('<br/>');
}
</script>
</body>
<ml>
''')
class MinHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>JS九九乘法表</title>
<meta name="keywords" content="JS,JavaScript,九九乘法表" />
<meta name="decoration" content="《 JavaScript 面向对象编程指南 》课后作业，九九乘法表" />
</head>

<body>
<h1>九九乘法表</h1>
<script type="text/javascript">
for(var i=1;i<=4;i++){
    for(var j=1;j<=i;j++){
        document.write(j+"*"+i+"="+i*j+"&nbsp;&nbsp;&nbsp;&nbsp;");
    }
    document.write('<br/>');
}
</script>
</body>
<ml>
''')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
         (r"/4", MinHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
