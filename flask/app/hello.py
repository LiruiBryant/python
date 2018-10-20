from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

manager = Manager(app)
bootstrap = Bootstrap(app)

if __name__ == '__main__':
    manager.run()
