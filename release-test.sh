#!/bin/bash

set -e
set -x

package=cwltool
module=cwltool
repo=https://github.com/common-workflow-language/cwltool.git
run_tests="py.test --ignore ${module}/schemas/ --pyarg cwltool"
pipver=7.0.2 # minimum required version of pip

rm -Rf testenv? || /bin/true

export HEAD=`git rev-parse HEAD`
virtualenv testenv1
virtualenv testenv2
virtualenv testenv3
virtualenv testenv4

# First we test the head
source testenv1/bin/activate
rm testenv1/lib/python-wheels/setuptools* \
	&& pip install --force-reinstall -U pip==${pipver} \
        && pip install setuptools==20.10.1 wheel
make install-dep
make test
pip uninstall -y ${package} || true; pip uninstall -y ${package} || true; make install
mkdir testenv1/not-${module}
# if there is a subdir named '${module}' py.test will execute tests
# there instead of the installed module's tests
pushd testenv1/not-${module}; ../bin/${run_tests}; popd


# Secondly we test via pip

cd testenv2
source bin/activate
rm lib/python-wheels/setuptools* \
	&& pip install --force-reinstall -U pip==${pipver} \
        && pip install setuptools==20.10.1 wheel
pip install -e git+${repo}@${HEAD}#egg=${package}
cd src/${package}
make install-dep
make dist
make test
cp dist/${package}*tar.gz ../../../testenv3/
pip uninstall -y ${package} || true; pip uninstall -y ${package} || true; make install
cd ../.. # no subdir named ${proj} here, safe for py.testing the installed module
bin/${run_tests}

# Is the distribution in testenv2 complete enough to build another
# functional distribution?

cd ../testenv3/
source bin/activate
rm lib/python-wheels/setuptools* \
	&& pip install --force-reinstall -U pip==${pipver} \
        && pip install setuptools==20.10.1 wheel
pip install ${package}*tar.gz
pip install pytest mock
mkdir out
tar --extract --directory=out -z -f ${package}*.tar.gz
cd out/${package}*
make dist
make test
pip uninstall -y ${package} || true; pip uninstall -y ${package} || true; make install
mkdir ../not-${module}
pushd ../not-${module} ; ../../bin/${run_tests}; popd
