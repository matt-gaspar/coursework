env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"
virtualenv $env_dir
. $env_dir/bin/activate
echo `which pip`
echo `pip --version`
#install -r requirements.txt
