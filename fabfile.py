from fabric import Connection, task
@task
def remote_task():
    # Connect to the remote server via SSH
    with Connection('ubuntu@100.26.167.149'):
        # Run remote commands
        result = run('ls -l')
        print(result.stdout)
