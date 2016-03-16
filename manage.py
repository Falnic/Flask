from app import app
from db_module import DbCreate, DbDowngrade, DbMigrate, DbUpgrade
from flask_script import Manager


manager = Manager(app)
manager.add_command('create', DbCreate)
manager.add_command('downgrade', DbDowngrade)
manager.add_command('migrate', DbMigrate)
manager.add_command('upgrade', DbUpgrade)


@manager.command
def runserver():
    app.run(debug=True)

if __name__ == "__main__":
    manager.run()
