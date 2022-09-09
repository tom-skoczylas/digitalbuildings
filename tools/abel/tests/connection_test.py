# Copyright 2022 Google LLC
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
"""Tests for States class."""

from absl.testing import absltest

from model.connection import Connection
from model.connection_type import ConnectionType
from model.constants import CONNECTION_TYPE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_GUID


_TEST_CONNECTION_DICT = {
    SOURCE_ENTITY_GUID: 'source_guid',
    TARGET_ENTITY_GUID: 'target_guid',
    CONNECTION_TYPE: 'CONTROLS'
}


class ConnectionTest(absltest.TestCase):

  def testFromDict(self):
    test_connection = Connection.FromDict(_TEST_CONNECTION_DICT)

    self.assertEqual(test_connection.source_entity_guid,
                     _TEST_CONNECTION_DICT[SOURCE_ENTITY_GUID])
    self.assertEqual(test_connection.target_entity_guid,
                     _TEST_CONNECTION_DICT[TARGET_ENTITY_GUID])
    self.assertEqual(test_connection.connection_type,
                     ConnectionType[_TEST_CONNECTION_DICT[CONNECTION_TYPE]])


if __name__ == '__main__':
  absltest.main()
