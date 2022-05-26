import ping


def test_ping():
    assert ping.check_server_status() == True
