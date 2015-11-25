env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"
virtualenv $env_dir
. $env_dir/bin/activate
pip install -r requirements.txt

# Run Unit tests
./run_tests.sh

# Code coverage
coverage xml
coverage erase

# Code analysis
pep8 --ignore=E501 hello.py > pep8_output.txt
