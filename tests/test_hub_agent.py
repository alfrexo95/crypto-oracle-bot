import json
import unittest
from unittest.mock import patch
from hub_agent import register_and_heartbeat

class HubAgentTests(unittest.TestCase):
    def test_skip_without_token(self):
        with patch.dict("os.environ", {"INFRA_HUB_TOKEN": ""}, clear=False):
            self.assertFalse(register_and_heartbeat("oracle", "github-actions", ["oracle"]))

    @patch("hub_agent.urlopen")
    def test_register_and_heartbeat_calls_authenticated_api(self, mocked):
        class Resp:
            def read(self): return b"{}"
            def __enter__(self): return self
            def __exit__(self, *a): return False
        mocked.side_effect = [Resp(), Resp()]
        with patch.dict("os.environ", {"INFRA_HUB_TOKEN": "secret", "INFRA_HUB_URL": "https://hub.test"}, clear=False):
            self.assertTrue(register_and_heartbeat("oracle", "github-actions", ["oracle"]))
        req1, req2 = [call.args[0] for call in mocked.call_args_list]
        self.assertEqual(req1.headers["Authorization"], "Bearer secret")
        self.assertEqual(json.loads(req1.data)["agent_id"], "oracle")
        self.assertIn("/heartbeat", req2.full_url)

if __name__ == "__main__":
    unittest.main()
