from system.init import initialize_app
import subprocess
application = initialize_app()

if __name__ == "__main__":
	application.run(host='127.0.0.1')
