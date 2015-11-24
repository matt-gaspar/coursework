env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"
virtualenv $env_dir
. $env_dir/bin/activate
pip install -r requirements.txt
