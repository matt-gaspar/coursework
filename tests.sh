env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"
pyvenv $env_dir
. $env_dir/bin/activate
echo `which pip`
echo `pip --version`
#install -r requirements.txt
