# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup file for Instance Validator."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='instance-validator',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='(in alphabatical order)'
    'Keith Berkoben,'
    'Raymond Li,'
    'Charbel Kaed,'
    'Nigel Kilmer',
    packages=find_packages(),
    install_requires=[
        'protobuf==3.20.1', 'proto-plus<1.19.7',
        'ruamel.yaml==0.17.4', 'strictyaml==1.4.2',
        'google-cloud-pubsub==2.6.1', 'google-auth<2.0',
        'googleapis-common-protos==1.56.0'
    ],
    python_requires='>=3.9',
)
